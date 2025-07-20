# coding:utf-8
# 主页卡片


from PySide6.QtCore import Qt, QSize, QUrl
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)

from qfluentwidgets import (
    BodyLabel,
    CaptionLabel,
    TransparentToolButton,
    FluentIcon,
    ImageLabel,
    SimpleCardWidget,
    HyperlinkLabel,
    PrimaryPushButton,
    TitleLabel,
    PillPushButton,
    VerticalSeparator,
    setFont,
    HeaderCardWidget,
)


class StatisticsWidget(QWidget):
    """Statistics widget"""

    def __init__(self, title: str, value: str, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = CaptionLabel(title, self)
        self.valueLabel = BodyLabel(value, self)
        self.vBoxLayout = QVBoxLayout(self)

        self.vBoxLayout.setContentsMargins(16, 0, 16, 0)
        self.vBoxLayout.addWidget(self.valueLabel, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignBottom)

        setFont(self.valueLabel, 18, QFont.DemiBold)
        self.titleLabel.setTextColor(QColor(96, 96, 96), QColor(206, 206, 206))


class AppInfoCard(SimpleCardWidget):
    """App information card"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.iconLabel = ImageLabel(":app/images/logo.png", self)
        self.iconLabel.setBorderRadius(8, 8, 8, 8)
        self.iconLabel.scaledToWidth(120)

        self.nameLabel = TitleLabel("QEFT CLIENT", self)
        self.installButton = PrimaryPushButton("检查更新", self)
        self.companyLabel = HyperlinkLabel(QUrl("#"), "QEFT开发团队", self)
        self.installButton.setFixedWidth(160)

        self.scoreWidget = StatisticsWidget("更新日期", "2025年7月11日", self)
        self.separator = VerticalSeparator(self)
        self.commentWidget = StatisticsWidget("当前版本", "Dev V0.0.1", self)

        self.descriptionLabel = BodyLabel(
            "QEFT是EDL刷机工具的GUI客户端",
            self,
        )
        self.descriptionLabel.setWordWrap(True)

        self.tagButton = PillPushButton("刷机", self)
        self.tagButton.setCheckable(False)
        setFont(self.tagButton, 12)
        self.tagButton.setFixedSize(80, 32)

        self.shareButton = TransparentToolButton(FluentIcon.SHARE, self)
        self.shareButton.setFixedSize(32, 32)
        self.shareButton.setIconSize(QSize(14, 14))

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.statisticsLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.initLayout()
        self.setBorderRadius(8)

    def initLayout(self):
        self.hBoxLayout.setSpacing(30)
        self.hBoxLayout.setContentsMargins(34, 24, 24, 24)
        self.hBoxLayout.addWidget(self.iconLabel)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)

        # name label and install button
        self.vBoxLayout.addLayout(self.topLayout)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.addWidget(self.nameLabel)
        self.topLayout.addWidget(self.installButton, 0, Qt.AlignRight)

        # company label
        self.vBoxLayout.addSpacing(3)
        self.vBoxLayout.addWidget(self.companyLabel)

        # statistics widgets
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addLayout(self.statisticsLayout)
        self.statisticsLayout.setContentsMargins(0, 0, 0, 0)
        self.statisticsLayout.setSpacing(10)
        self.statisticsLayout.addWidget(self.scoreWidget)
        self.statisticsLayout.addWidget(self.separator)
        self.statisticsLayout.addWidget(self.commentWidget)
        self.statisticsLayout.setAlignment(Qt.AlignLeft)

        # description label
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addWidget(self.descriptionLabel)

        # button
        self.vBoxLayout.addSpacing(12)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addLayout(self.buttonLayout)
        self.buttonLayout.addWidget(self.tagButton, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.shareButton, 0, Qt.AlignRight)


class UserNoticeCard(HeaderCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("用户须知  |  免责声明")

        self.content = BodyLabel(self)
        self.content.setWordWrap(True)
        self.content.setText(
            """欢迎使用我们的刷机软件！在使用本软件之前，请仔细阅读以下用户协议与免责声明。本协议对您使用本软件的权利和义务进行了详细说明，请您务必完全理解并同意本协议的所有条款后再使用本软件。如您不同意本协议的任何条款，请勿使用本软件。
一、协议的适用范围
接受条款：您使用本软件即表示您同意接受本协议的所有条款和条件。如果您不同意本协议的任何部分，请勿使用本软件。
协议修改：我们保留随时修改本协议的权利，修改后的协议将在发布后立即生效。您应定期查看本协议，以了解最新的条款和条件。如果您在协议修改后继续使用本软件，则视为您接受修改后的协议。
二、软件的使用
许可授予：我们授予您个人的、非排他的、不可转让的许可，允许您在遵守本协议的前提下使用本软件。
使用限制：您不得将本软件用于任何非法目的，不得对本软件进行反向工程、反编译或解密，不得复制、分发、出租或转让本软件，不得对本软件进行任何形式的修改或创建衍生作品。
遵守法律法规：您在使用本软件时应遵守所有适用的法律法规，包括但不限于关于数据隐私、知识产权和网络安全的法律法规。
三、风险提示与免责声明
刷机风险：刷机操作可能会导致您的设备出现各种问题，包括但不限于设备故障、数据丢失、保修失效、安全漏洞等。您应充分了解刷机操作的风险，并在进行刷机操作之前备份您的重要数据。
免责声明：我们不对您使用本软件进行刷机操作所导致的任何直接或间接损失承担责任，包括但不限于设备损坏、数据丢失、业务中断、利润损失等。无论这些损失是因何原因导致的，包括但不限于疏忽、违约、侵权或其他原因。
设备兼容性：本软件可能不兼容所有设备或设备型号。我们不保证本软件能够在您的设备上正常运行，也不对因软件与设备不兼容而导致的任何问题承担责任。
第三方责任：您在使用本软件时可能会涉及第三方的产品或服务，我们不对第三方的行为或产品负责。您应自行评估第三方产品或服务的风险，并承担因使用第三方产品或服务而导致的任何损失。
四、知识产权
软件所有权：本软件及其相关的知识产权归我们所有或由我们授权使用。您不得侵犯我们或第三方的知识产权。
商标使用：本软件中可能包含我们或第三方的商标、服务标记或标识。未经所有者的明确书面许可，您不得使用这些商标、服务标记或标识。
五、隐私政策
信息收集：我们可能会收集您使用本软件时的相关信息，包括但不限于设备信息、使用记录等。我们将按照适用的隐私政策处理您的个人信息。
信息使用：我们收集的信息仅用于提供和改进本软件的服务，不会用于其他目的，除非获得您的明确同意。
信息保护：我们将采取合理的安全措施保护您的个人信息，防止信息泄露、丢失或滥用。
六、终止协议
用户终止：您可以随时停止使用本软件，从而终止本协议。
我们终止：如果您违反本协议的任何条款，我们有权立即终止本协议，并禁止您使用本软件。
终止后果：协议终止后，您应立即停止使用本软件，并销毁所有与本软件相关的副本。本协议中关于免责声明、知识产权和争议解决等条款在协议终止后仍然有效。
七、争议解决
适用法律：本协议受中华人民共和国法律管辖。
争议解决方式：如双方就本协议发生争议，应首先通过友好协商解决；协商不成的，任何一方均有权向有管辖权的人民法院提起诉讼。
八、其他条款
完整协议：本协议构成您与我们之间就使用本软件的完整协议，并取代所有先前的口头或书面协议。
可分割性：如果本协议的任何条款被认定为无效或不可执行，该条款的无效或不可执行不影响其他条款的效力。
弃权：我们未行使或延迟行使本协议项下的任何权利或救济，不构成对该权利或救济的放弃。
九、关于刷机的详细风险提示
硬件损坏风险：不正确的刷机操作可能会导致硬件损坏，例如主板故障、电池问题等。这种损坏可能无法修复，导致设备永久无法使用。
数据丢失风险：刷机过程中可能会导致设备上的数据丢失，包括但不限于联系人、短信、照片、视频、文件等。即使您备份了数据，也可能存在备份不完整或恢复失败的风险。
保修失效风险：大多数设备制造商明确表示，刷机将导致设备的保修失效。这意味着如果您的设备在刷机后出现问题，制造商将不会提供免费维修服务。
安全漏洞风险：使用非官方的刷机包或来源不明的软件可能会导致设备存在安全漏洞，使您的个人信息和数据面临被盗取的风险。
系统不稳定风险：刷机后，设备的系统可能会变得不稳定，出现频繁死机、重启、应用程序崩溃等问题，严重影响您的使用体验。
十、用户责任
自行承担风险：您使用本软件进行刷机操作完全出于您的自愿，您应自行承担刷机操作的所有风险。
备份数据：在进行刷机操作之前，您应确保备份了设备上的所有重要数据。我们不对数据丢失承担任何责任。
遵守操作指南：您应严格按照本软件提供的操作指南进行刷机操作。如果您不熟悉刷机过程，建议您寻求专业人士的帮助。"""
        )

        self.viewLayout.addWidget(self.content)
