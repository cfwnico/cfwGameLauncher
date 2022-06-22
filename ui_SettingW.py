# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingWiworva.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 530)
        Dialog.setMinimumSize(QSize(400, 530))
        Dialog.setMaximumSize(QSize(400, 530))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.norm_tab = QWidget()
        self.norm_tab.setObjectName(u"norm_tab")
        self.gridLayout_3 = QGridLayout(self.norm_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.user_edit = QLineEdit(self.norm_tab)
        self.user_edit.setObjectName(u"user_edit")

        self.gridLayout_2.addWidget(self.user_edit, 3, 1, 1, 1)

        self.label = QLabel(self.norm_tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.label_3 = QLabel(self.norm_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.sign_edit = QLineEdit(self.norm_tab)
        self.sign_edit.setObjectName(u"sign_edit")

        self.gridLayout_2.addWidget(self.sign_edit, 4, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.change_head_btn = QPushButton(self.norm_tab)
        self.change_head_btn.setObjectName(u"change_head_btn")

        self.horizontalLayout_4.addWidget(self.change_head_btn)

        self.open_folder_btn = QPushButton(self.norm_tab)
        self.open_folder_btn.setObjectName(u"open_folder_btn")

        self.horizontalLayout_4.addWidget(self.open_folder_btn)

        self.change_folder_btn = QPushButton(self.norm_tab)
        self.change_folder_btn.setObjectName(u"change_folder_btn")

        self.horizontalLayout_4.addWidget(self.change_folder_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 7, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 8, 0, 1, 2)

        self.label_2 = QLabel(self.norm_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.head_label = QLabel(self.norm_tab)
        self.head_label.setObjectName(u"head_label")
        self.head_label.setScaledContents(False)
        self.head_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.head_label, 0, 0, 1, 2)

        self.line_3 = QFrame(self.norm_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 6, 0, 1, 2)

        self.folder_path_edit = QLineEdit(self.norm_tab)
        self.folder_path_edit.setObjectName(u"folder_path_edit")

        self.gridLayout_2.addWidget(self.folder_path_edit, 5, 1, 1, 1)

        self.user_label = QLabel(self.norm_tab)
        self.user_label.setObjectName(u"user_label")
        font = QFont()
        font.setPointSize(28)
        font.setBold(False)
        self.user_label.setFont(font)
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.user_label, 1, 0, 1, 2)

        self.line_4 = QFrame(self.norm_tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 2, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.norm_tab, "")
        self.ncd_tab = QWidget()
        self.ncd_tab.setObjectName(u"ncd_tab")
        self.gridLayout_5 = QGridLayout(self.ncd_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_2 = QFrame(self.ncd_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 4, 0, 1, 2)

        self.label_7 = QLabel(self.ncd_tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.manage_all_btn = QPushButton(self.ncd_tab)
        self.manage_all_btn.setObjectName(u"manage_all_btn")

        self.horizontalLayout_5.addWidget(self.manage_all_btn)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 7, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 8, 0, 1, 2)

        self.ncd_count_label = QLabel(self.ncd_tab)
        self.ncd_count_label.setObjectName(u"ncd_count_label")

        self.gridLayout_4.addWidget(self.ncd_count_label, 1, 1, 1, 1)

        self.ncd_folder_edit = QLineEdit(self.ncd_tab)
        self.ncd_folder_edit.setObjectName(u"ncd_folder_edit")

        self.gridLayout_4.addWidget(self.ncd_folder_edit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.ncd_tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.ncd_size_label = QLabel(self.ncd_tab)
        self.ncd_size_label.setObjectName(u"ncd_size_label")

        self.gridLayout_4.addWidget(self.ncd_size_label, 3, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.open_ncd_btn = QPushButton(self.ncd_tab)
        self.open_ncd_btn.setObjectName(u"open_ncd_btn")

        self.horizontalLayout_3.addWidget(self.open_ncd_btn)

        self.clu_size_btn = QPushButton(self.ncd_tab)
        self.clu_size_btn.setObjectName(u"clu_size_btn")

        self.horizontalLayout_3.addWidget(self.clu_size_btn)

        self.change_ncd_btn = QPushButton(self.ncd_tab)
        self.change_ncd_btn.setObjectName(u"change_ncd_btn")

        self.horizontalLayout_3.addWidget(self.change_ncd_btn)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)

        self.label_5 = QLabel(self.ncd_tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.line = QFrame(self.ncd_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 6, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.ncd_tab, "")
        self.adva_tab = QWidget()
        self.adva_tab.setObjectName(u"adva_tab")
        self.gridLayout_7 = QGridLayout(self.adva_tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.waifu2x_checkbox = QCheckBox(self.adva_tab)
        self.waifu2x_checkbox.setObjectName(u"waifu2x_checkbox")

        self.gridLayout_6.addWidget(self.waifu2x_checkbox, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.adva_tab, "")
        self.about_tab = QWidget()
        self.about_tab.setObjectName(u"about_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.about_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.about_tab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.tabWidget.addTab(self.about_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_btn = QPushButton(Dialog)
        self.ok_btn.setObjectName(u"ok_btn")

        self.horizontalLayout.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.apply_btn = QPushButton(Dialog)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout.addWidget(self.apply_btn)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u5e93\u76ee\u5f55:", None))
        self.change_head_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u7528\u6237\u5934\u50cf", None))
        self.open_folder_btn.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u6e38\u620f\u5e93\u76ee\u5f55", None))
        self.change_folder_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u6e38\u620f\u5e93\u76ee\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4e2a\u6027\u7b7e\u540d:", None))
        self.head_label.setText(QCoreApplication.translate("Dialog", u"\u65e0\u5934\u50cf", None))
        self.user_label.setText(QCoreApplication.translate("Dialog", u"user_name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.norm_tab), QCoreApplication.translate("Dialog", u"\u5e38\u89c4", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u4e91\u7aef\u5b58\u6863\u4e2a\u6570:", None))
        self.manage_all_btn.setText(QCoreApplication.translate("Dialog", u"\u7ba1\u7406\u6240\u6709\u4e91\u5b58\u6863", None))
        self.ncd_count_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u4e91\u7aef\u5b58\u6863\u5bb9\u91cf:", None))
        self.ncd_size_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.open_ncd_btn.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u4e91\u7aef\u5b58\u6863\u6587\u4ef6\u5939", None))
        self.clu_size_btn.setText(QCoreApplication.translate("Dialog", u"\u8ba1\u7b97\u4e91\u7aef\u5b58\u6863\u5bb9\u91cf", None))
        self.change_ncd_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u4e91\u7aef\u5b58\u6863\u6587\u4ef6\u5939", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u4e91\u7aef\u5b58\u6863\u6587\u4ef6\u5939:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ncd_tab), QCoreApplication.translate("Dialog", u"\u4e91\u540c\u6b65", None))
        self.waifu2x_checkbox.setText(QCoreApplication.translate("Dialog", u"\u5207\u6362\u80cc\u666f\u56fe\u7247\u65f6\u4f7f\u7528waifu2x\u7cbe\u7f29\u653e(\u4f1a\u6d88\u8017\u8f83\u957f\u65f6\u95f4)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adva_tab), QCoreApplication.translate("Dialog", u"\u9ad8\u7ea7", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">cfwGameLauncher</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Ver 0.1.2</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Python 3.10</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">PySide 6.3</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">cfw</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_tab), QCoreApplication.translate("Dialog", u"\u5173\u4e8e", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.apply_btn.setText(QCoreApplication.translate("Dialog", u"\u5e94\u7528", None))
    # retranslateUi

