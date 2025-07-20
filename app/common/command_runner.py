import subprocess
import sys
import threading
import queue
from typing import List, Union, Optional, Callable

class CommandRunner:
    _instance = None
    _thread_pool = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CommandRunner, cls).__new__(cls)
            # 初始化线程池监控线程
            cls._monitor_thread = threading.Thread(target=cls._monitor_workers, daemon=True)
            cls._monitor_thread.start()
        return cls._instance
    
    @classmethod
    def _monitor_workers(cls):
        """监控工作线程，清理已完成的任务"""
        while True:
            completed_ids = []
            for task_id, worker in list(cls._thread_pool.items()):
                if not worker.is_alive():
                    worker.join()  # 确保资源释放
                    completed_ids.append(task_id)
            
            # 清理已完成的任务
            for task_id in completed_ids:
                cls._thread_pool.pop(task_id, None)
            
            # 每0.5秒检查一次
            threading.Event().wait(0.5)
    
    @classmethod
    def run_command(
        cls,
        command: Union[str, List[str]],
        print_output: bool = True,
        capture_output: bool = False,
        callback: Optional[Callable[[str], None]] = None,
        **kwargs
    ) -> Optional[str]:
        """
        执行命令（非阻塞方式），实时显示输出，自动处理GUI线程问题
        
        参数:
            command: 要执行的命令（字符串或参数列表）
            print_output: 是否实时打印输出 (默认 True)
            capture_output: 是否捕获完整输出 (默认 False)
            callback: 自定义回调函数，用于处理实时输出
            kwargs: 传递给 subprocess.Popen 的额外参数
            
        返回:
            如果 capture_output=True 则返回完整输出字符串，否则返回 None
        """
        # 统一处理命令格式
        shell = isinstance(command, str)
        if not shell and sys.platform == "win32":
            command = [str(arg) for arg in command]  # Windows 需要字符串参数
        
        # 创建线程安全的队列用于通信
        output_queue = queue.Queue()
        result = {"output": None, "exception": None}
        
        def worker():
            """工作线程执行命令"""
            try:
                full_output = []
                process = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    shell=shell,
                    text=True,
                    bufsize=1,
                    **kwargs
                )
                
                while True:
                    output_line = process.stdout.readline()
                    if not output_line and process.poll() is not None:
                        break
                    
                    if output_line:
                        # 放入队列供主线程处理
                        output_queue.put(output_line)
                        
                        if capture_output:
                            full_output.append(output_line)
                
                # 捕获完整输出
                if capture_output:
                    result["output"] = ''.join(full_output)
            
            except Exception as e:
                result["exception"] = e
            finally:
                # 结束标志
                output_queue.put(None)
        
        # 启动工作线程
        worker_thread = threading.Thread(target=worker, daemon=True)
        task_id = id(worker_thread)
        cls._thread_pool[task_id] = worker_thread
        worker_thread.start()
        
        # 在主线程中处理输出（非阻塞）
        def process_output():
            """处理输出队列中的内容"""
            try:
                while True:
                    # 非阻塞获取输出
                    try:
                        output_line = output_queue.get_nowait()
                    except queue.Empty:
                        break
                    
                    # 结束标志
                    if output_line is None:
                        break
                    
                    # 处理输出
                    if print_output:
                        sys.stdout.write(output_line)
                        sys.stdout.flush()
                    
                    if callback:
                        callback(output_line)
            except Exception as e:
                result["exception"] = e
            
            # 返回结果或异常
            if result["exception"]:
                raise result["exception"]
            
            return result["output"] if capture_output else None
        
        # 立即返回结果处理函数
        return process_output

# 保持原有函数接口
def run_command(
    command: Union[str, List[str]],
    print_output: bool = True,
    capture_output: bool = False,
    callback: Optional[Callable[[str], None]] = None,
    **kwargs
) -> Optional[str]:
    """
    执行命令并实时显示输出（GUI友好版本）
    
    注意: 此函数立即返回一个可调用对象，需要定期调用它来处理输出
    
    示例:
        output_handler = run_command("ls -la")
        while True:
            result = output_handler()
            if result is not None:
                # 处理完成
                break
            # 短暂暂停，避免过度占用CPU
            time.sleep(0.01)
    """
    runner = CommandRunner()
    return runner.run_command(
        command=command,
        print_output=print_output,
        capture_output=capture_output,
        callback=callback,
        **kwargs
    )