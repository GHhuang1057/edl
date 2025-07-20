# coding:utf-8
# 主程序
# 在这里感谢@630，虽然中途因事退出了GUI部分的开发
# 但是在他的指导下，我重新开始开发了GUI部分的代码（但是有相当一部分还是TA写的）
# 在这里感谢TA的贡献！


import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication
from app.common.config import cfg
from app.view.main_window import MainWindow


# enable dpi scale
if cfg.get(cfg.dpiScale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

# create application
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)



# create main window
w = MainWindow()
w.show()

app.exec()
