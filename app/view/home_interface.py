# coding: utf-8

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from qfluentwidgets import ImageLabel, BodyLabel, ScrollArea

from ..components.homeCard import AppInfoCard, UserNoticeCard


class HomeInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("HomeInterface")
        self.widgets = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.widgets)

        self.appInfoCard = AppInfoCard(self.widgets)
        self.userNoticeCard = UserNoticeCard(self.widgets)

        self.__initWidget()

    def __initWidget(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setObjectName("homeInterface")
        self.setWidget(self.widgets)
        self.setStyleSheet("border: none;background: transparent;")
        self.__initLayout()

    def __initLayout(self):

        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.vBoxLayout.addWidget(self.appInfoCard)
        self.vBoxLayout.addWidget(self.userNoticeCard)
