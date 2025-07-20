# coding: utf-8
# 手机连接状态卡片

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

from qfluentwidgets import CardWidget, ImageLabel, SubtitleLabel, PushButton


class ConnectionCard(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.imageLabel = ImageLabel(self)
        self.phoneInfoLabel = SubtitleLabel(self)

        self.connectButton = PushButton(self)
        self.disconnectButton = PushButton(self)

        self.__initWidget()

    def __initWidget(self):
        self.imageLabel.setImage(":app/images/connection.png")
        self.imageLabel.scaledToHeight(100)
        self.imageLabel.scaledToWidth(100)

        self.phoneInfoLabel.setText(
            "当前连接状态: 未连接\n设备名称: 未知设备\n设备IP: 0.0.0.0\n设备端口: 0"
        )
        self.connectButton.setText("连接手机")
        self.disconnectButton.setText("断开连接")

        self.__initLayout()

    def __initLayout(self):
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.hBoxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.hBoxLayout.addWidget(
            self.imageLabel,
            0,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
        )
        self.hBoxLayout.addSpacing(10)
        self.hBoxLayout.addWidget(
            self.phoneInfoLabel,
            0,
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )

        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.addWidget(self.connectButton)
        self.buttonLayout.addWidget(self.disconnectButton)

        self.hBoxLayout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        )
        self.hBoxLayout.addLayout(self.buttonLayout)
        self.hBoxLayout.addSpacing(20)
