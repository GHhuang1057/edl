# coding: utf-8

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from PySide6.QtCore import Qt, QEasingCurve
from PySide6.QtGui import QIcon

from qfluentwidgets import FlowLayout, PushButton, TableWidget, BodyLabel


class FlashToolsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("flashTools")
        self.flowLayout = FlowLayout(self)
        self.flowLayout.setContentsMargins(0, 0, 0, 0)
        self.flowLayout.setVerticalSpacing(20)
        self.flowLayout.setHorizontalSpacing(10)
        self.flowLayout.setAnimation(250, QEasingCurve.OutQuad)

        self.readFlashMemory = PushButton("读取整盘镜像", self)
        self.writeToFlashMemory = PushButton("写入整盘镜像", self)
        self.SecureBoot = PushButton("安全启动检测", self)
        self.Pbl = PushButton("转储PBL", self)
        self.Qfp = PushButton("转储QFPROM", self)
        self.Xml = PushButton("发送XML文件", self)
        self.RawXml = PushButton("发送XML字符串", self)
        self.QFILFlash = PushButton("QFIL模式刷机", self)
        self.unlockBootloader = PushButton("OEM解锁", self)

        self.flowLayout.addWidget(self.readFlashMemory)
        self.flowLayout.addWidget(self.writeToFlashMemory)
        self.flowLayout.addWidget(self.SecureBoot)
        self.flowLayout.addWidget(self.Pbl)
        self.flowLayout.addWidget(self.Qfp)
        self.flowLayout.addWidget(self.Xml)
        self.flowLayout.addWidget(self.RawXml)
        self.flowLayout.addWidget(self.QFILFlash)
        self.flowLayout.addWidget(self.unlockBootloader)
