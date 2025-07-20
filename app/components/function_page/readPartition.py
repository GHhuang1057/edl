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

from qfluentwidgets import CheckBox, PushButton, TableWidget


class ReadPartitionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("readPartition")
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.selectAllCheckBox = CheckBox("选中所有分区", self)
        self.backupsCheckBox = CheckBox("备份GPT(分区表)", self)
        self.readPartitionButton = PushButton("读取分区", self)
        self.tableWidget = TableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["分区名", "大小", "类型"])

        self.hBoxLayout.addWidget(self.selectAllCheckBox, 0, Qt.AlignmentFlag.AlignLeft)
        self.hBoxLayout.addWidget(self.backupsCheckBox, 0, Qt.AlignmentFlag.AlignLeft)
        self.hBoxLayout.addSpacerItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )
        self.hBoxLayout.addWidget(
            self.readPartitionButton, 0, Qt.AlignmentFlag.AlignRight
        )
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addWidget(self.tableWidget)
