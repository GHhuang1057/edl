# coding: utf-8
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QApplication

from qfluentwidgets import NavigationItemPosition, MSFluentWindow, SplashScreen
from qfluentwidgets import FluentIcon as FIF

from .home_interface import HomeInterface
from .function_interface import FunctionInterface
from .setting_interface import SettingInterface
from ..common.config import cfg
from ..common.signal_bus import signalBus
from ..common import resource


class MainWindow(MSFluentWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

        self.homeInterface = HomeInterface(self)
        self.functionInterface = FunctionInterface(self)
        self.settingInterface = SettingInterface(self)

        self.connectSignalToSlot()

        self.initNavigation()

    def connectSignalToSlot(self):
        signalBus.micaEnableChanged.connect(self.setMicaEffectEnabled)

    def initNavigation(self):
        self.addSubInterface(
            self.functionInterface,
            FIF.APPLICATION,
            "功能",
            FIF.APPLICATION,
            NavigationItemPosition.TOP,
        )
        self.addSubInterface(
            self.homeInterface, FIF.HOME, "主页", FIF.HOME, NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.settingInterface,
            FIF.SETTING,
            "设置",
            FIF.SETTING,
            NavigationItemPosition.BOTTOM,
        )

        self.splashScreen.finish()

    def initWindow(self):
        self.resize(960, 780)
        self.setMinimumWidth(760)
        self.setWindowIcon(QIcon(":/app/images/logo.png"))
        self.setWindowTitle("QC-EDL Flash Tool")

        self.setCustomBackgroundColor(QColor(240, 244, 249), QColor(32, 32, 32))
        self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, "splashScreen"):
            self.splashScreen.resize(self.size())
