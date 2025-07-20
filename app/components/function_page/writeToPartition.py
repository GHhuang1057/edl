# coding: utf-8

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from qfluentwidgets import CheckBox, PushButton, TableWidget, BodyLabel


class WritePartitionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("writeToPartition")
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.selectPartition = BodyLabel("选择需要写入的分区", self)
        self.selectPartButton = PushButton("从文件夹中选择", self)
        self.writePartitionButton = PushButton("写入分区", self)
        self.tableWidget = TableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["分区名", "大小", "类型"])

        self.hBoxLayout.addWidget(self.selectPartition, 0, Qt.AlignmentFlag.AlignLeft)
        self.hBoxLayout.addSpacing(10)
        self.hBoxLayout.addWidget(self.selectPartButton, 0, Qt.AlignmentFlag.AlignLeft)
        self.hBoxLayout.addSpacerItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )
    
        self.hBoxLayout.addWidget(
            self.writePartitionButton, 0, Qt.AlignmentFlag.AlignRight
        )
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addWidget(self.tableWidget)
