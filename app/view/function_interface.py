# coding: utf-8

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from qfluentwidgets import SegmentedWidget, PopUpAniStackedWidget, TableWidget, TextEdit

from ..components.connectionCard import ConnectionCard
from ..components.function_page.readPartition import ReadPartitionWidget
from ..components.function_page.writeToPartition import WritePartitionWidget
from ..components.function_page.erasePartition import ErasePartitionWidget
from ..components.function_page.flashTools import FlashToolsWidget


class KeysWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("keys")
        self.vBoxLayout = QVBoxLayout(self)

        self.keysTable = TableWidget(self)
        self.keysTable.setColumnCount(2)
        self.keysTable.setHorizontalHeaderLabels(["类型", "值"])

        self.vBoxLayout.addWidget(self.keysTable)


class DebugLogWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("debugLog")
        self.vBoxLayout = QVBoxLayout(self)

        self.debugLog = TextEdit(self)
        self.debugLog.setPlaceholderText("调试日志")
        self.debugLog.setReadOnly(True)
        self.vBoxLayout.addWidget(self.debugLog)


class FunctionInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("FunctionInterface")

        self.connectionCard = ConnectionCard(self)
        self.pivot = SegmentedWidget(self)
        self.stackedWidget = PopUpAniStackedWidget(self)

        self.readPartitionWidget = ReadPartitionWidget(self.stackedWidget)
        self.writeToPartitionWidget = WritePartitionWidget(self.stackedWidget)
        self.erasePartitionWidget = ErasePartitionWidget(self.stackedWidget)
        self.flashToolsWidget = FlashToolsWidget(self.stackedWidget)
        self.keysWidget = KeysWidget(self.stackedWidget)
        self.debugLogWidget = DebugLogWidget(self.stackedWidget)

        self.__initWidget()

    def __initWidget(self):

        self.pivot.addItem(routeKey="readPartition", text="读取分区")
        self.pivot.addItem(routeKey="writeToPartition", text="写入分区")
        self.pivot.addItem(routeKey="erasePartition", text="擦除分区")
        self.pivot.addItem(routeKey="flashTools", text="刷机工具")
        self.pivot.addItem(routeKey="keys", text="Keys")
        self.pivot.addItem(routeKey="debugLog", text="调试日志")
        self.pivot.setCurrentItem("readPartition")

        self.stackedWidget.addWidget(self.readPartitionWidget)
        self.stackedWidget.addWidget(self.writeToPartitionWidget)
        self.stackedWidget.addWidget(self.erasePartitionWidget)
        self.stackedWidget.addWidget(self.flashToolsWidget)
        self.stackedWidget.addWidget(self.keysWidget)
        self.stackedWidget.addWidget(self.debugLogWidget)

        self.pivot.currentItemChanged.connect(self._changePage)
        self.__initLayout()

    def __initLayout(self):
        self.vBoxLayout = QVBoxLayout(self)

        self.vBoxLayout.addWidget(self.connectionCard, 0, Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.addWidget(self.stackedWidget)

    def _changePage(self, routeKey):
        self.stackedWidget.setCurrentWidget(
            self.stackedWidget.findChild(QWidget, routeKey)
        )
