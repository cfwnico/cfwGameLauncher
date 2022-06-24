# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWMrCSnx.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_game_btn = QPushButton(self.centralwidget)
        self.add_game_btn.setObjectName(u"add_game_btn")

        self.horizontalLayout.addWidget(self.add_game_btn)

        self.scan_game_btn = QPushButton(self.centralwidget)
        self.scan_game_btn.setObjectName(u"scan_game_btn")

        self.horizontalLayout.addWidget(self.scan_game_btn)

        self.setting_btn = QPushButton(self.centralwidget)
        self.setting_btn.setObjectName(u"setting_btn")

        self.horizontalLayout.addWidget(self.setting_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gamelist_widget = QListWidget(self.centralwidget)
        self.gamelist_widget.setObjectName(u"gamelist_widget")
        font = QFont()
        font.setPointSize(14)
        self.gamelist_widget.setFont(font)
        self.gamelist_widget.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);\n"
"border-color: rgba(255, 255, 255, 128);")

        self.gridLayout.addWidget(self.gamelist_widget, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 4, 5, 2, 1)

        self.txt_browser = QTextBrowser(self.frame)
        self.txt_browser.setObjectName(u"txt_browser")
        self.txt_browser.setFont(font)
        self.txt_browser.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);")

        self.gridLayout_2.addWidget(self.txt_browser, 7, 5, 1, 1)

        self.gamename_label = QLabel(self.frame)
        self.gamename_label.setObjectName(u"gamename_label")
        font1 = QFont()
        font1.setPointSize(36)
        self.gamename_label.setFont(font1)
        self.gamename_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);")
        self.gamename_label.setScaledContents(False)

        self.gridLayout_2.addWidget(self.gamename_label, 3, 0, 1, 6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 4, 2, 1)

        self.playgame_btn = QPushButton(self.frame)
        self.playgame_btn.setObjectName(u"playgame_btn")
        self.playgame_btn.setMinimumSize(QSize(0, 64))
        self.playgame_btn.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);")

        self.gridLayout_2.addWidget(self.playgame_btn, 4, 0, 2, 1)

        self.metadata_browser = QTextBrowser(self.frame)
        self.metadata_browser.setObjectName(u"metadata_browser")
        self.metadata_browser.setFont(font)
        self.metadata_browser.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);")

        self.gridLayout_2.addWidget(self.metadata_browser, 7, 0, 1, 5)

        self.last_run_label = QLabel(self.frame)
        self.last_run_label.setObjectName(u"last_run_label")
        self.last_run_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);")
        self.last_run_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.last_run_label, 4, 1, 2, 1)

        self.total_time_label = QLabel(self.frame)
        self.total_time_label.setObjectName(u"total_time_label")
        self.total_time_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.total_time_label, 4, 2, 2, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)

        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"cfwGameLauncher", None))
        self.add_game_btn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6e38\u620f", None))
        self.scan_game_btn.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u626b\u63cf\u6e38\u620f", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.gamename_label.setText(QCoreApplication.translate("MainWindow", u"game_name", None))
        self.playgame_btn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6e38\u620f", None))
        self.last_run_label.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.total_time_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6e38\u620f\u65f6\u95f4</p><p>0\u5206\u949f</p></body></html>", None))
    # retranslateUi

