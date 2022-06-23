# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttributesWQUtsqb.ui'
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
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ok_btn = QPushButton(Dialog)
        self.ok_btn.setObjectName(u"ok_btn")

        self.horizontalLayout_3.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_3.addWidget(self.cancel_btn)

        self.apply_btn = QPushButton(Dialog)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout_3.addWidget(self.apply_btn)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.norm_tab = QWidget()
        self.norm_tab.setObjectName(u"norm_tab")
        self.gridLayout_5 = QGridLayout(self.norm_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_folder_btn = QPushButton(self.norm_tab)
        self.open_folder_btn.setObjectName(u"open_folder_btn")

        self.horizontalLayout.addWidget(self.open_folder_btn)

        self.change_path_btn = QPushButton(self.norm_tab)
        self.change_path_btn.setObjectName(u"change_path_btn")

        self.horizontalLayout.addWidget(self.change_path_btn)

        self.change_icon_btn = QPushButton(self.norm_tab)
        self.change_icon_btn.setObjectName(u"change_icon_btn")

        self.horizontalLayout.addWidget(self.change_icon_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 9, 0, 1, 2)

        self.label_8 = QLabel(self.norm_tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 14, 0, 1, 1)

        self.last_run_label = QLabel(self.norm_tab)
        self.last_run_label.setObjectName(u"last_run_label")

        self.gridLayout_2.addWidget(self.last_run_label, 13, 1, 1, 1)

        self.ps_edit = QLineEdit(self.norm_tab)
        self.ps_edit.setObjectName(u"ps_edit")

        self.gridLayout_2.addWidget(self.ps_edit, 7, 1, 1, 1)

        self.line_4 = QFrame(self.norm_tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 12, 0, 1, 2)

        self.total_time_label = QLabel(self.norm_tab)
        self.total_time_label.setObjectName(u"total_time_label")

        self.gridLayout_2.addWidget(self.total_time_label, 14, 1, 1, 1)

        self.label_3 = QLabel(self.norm_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_7 = QLabel(self.norm_tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)

        self.nick_name_edit = QLineEdit(self.norm_tab)
        self.nick_name_edit.setObjectName(u"nick_name_edit")

        self.gridLayout_2.addWidget(self.nick_name_edit, 4, 1, 1, 1)

        self.line_3 = QFrame(self.norm_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 10, 0, 1, 2)

        self.game_folder_edit = QLineEdit(self.norm_tab)
        self.game_folder_edit.setObjectName(u"game_folder_edit")

        self.gridLayout_2.addWidget(self.game_folder_edit, 5, 1, 1, 1)

        self.label_4 = QLabel(self.norm_tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)

        self.label = QLabel(self.norm_tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 13, 0, 1, 1)

        self.label_2 = QLabel(self.norm_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.line = QFrame(self.norm_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)

        self.game_name_label = QLabel(self.norm_tab)
        self.game_name_label.setObjectName(u"game_name_label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.game_name_label.setFont(font)
        self.game_name_label.setAlignment(Qt.AlignCenter)
        self.game_name_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.game_name_label, 1, 0, 1, 2)

        self.game_name_edit = QLineEdit(self.norm_tab)
        self.game_name_edit.setObjectName(u"game_name_edit")

        self.gridLayout_2.addWidget(self.game_name_edit, 3, 1, 1, 1)

        self.exe_path_edit = QLineEdit(self.norm_tab)
        self.exe_path_edit.setObjectName(u"exe_path_edit")

        self.gridLayout_2.addWidget(self.exe_path_edit, 6, 1, 1, 1)

        self.line_2 = QFrame(self.norm_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 8, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 15, 0, 1, 2)

        self.icon_label = QLabel(self.norm_tab)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.icon_label, 0, 0, 1, 2)

        self.label_6 = QLabel(self.norm_tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.change_bg_btn = QPushButton(self.norm_tab)
        self.change_bg_btn.setObjectName(u"change_bg_btn")

        self.horizontalLayout_4.addWidget(self.change_bg_btn)

        self.edit_metadata_btn = QPushButton(self.norm_tab)
        self.edit_metadata_btn.setObjectName(u"edit_metadata_btn")

        self.horizontalLayout_4.addWidget(self.edit_metadata_btn)

        self.edit_txt_btn = QPushButton(self.norm_tab)
        self.edit_txt_btn.setObjectName(u"edit_txt_btn")

        self.horizontalLayout_4.addWidget(self.edit_txt_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 11, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 2)

        self.tabWidget.addTab(self.norm_tab, "")
        self.ncd_tab = QWidget()
        self.ncd_tab.setObjectName(u"ncd_tab")
        self.gridLayout_4 = QGridLayout(self.ncd_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_5 = QFrame(self.ncd_tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 5, 0, 1, 2)

        self.label_10 = QLabel(self.ncd_tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.use_ncd_checkbox = QCheckBox(self.ncd_tab)
        self.use_ncd_checkbox.setObjectName(u"use_ncd_checkbox")

        self.gridLayout_3.addWidget(self.use_ncd_checkbox, 0, 0, 1, 2)

        self.label_14 = QLabel(self.ncd_tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 7, 0, 1, 2)

        self.save_date_label = QLabel(self.ncd_tab)
        self.save_date_label.setObjectName(u"save_date_label")

        self.gridLayout_3.addWidget(self.save_date_label, 4, 1, 1, 1)

        self.sync_savepath_label = QLabel(self.ncd_tab)
        self.sync_savepath_label.setObjectName(u"sync_savepath_label")

        self.gridLayout_3.addWidget(self.sync_savepath_label, 3, 1, 1, 1)

        self.sync_status_label = QLabel(self.ncd_tab)
        self.sync_status_label.setObjectName(u"sync_status_label")

        self.gridLayout_3.addWidget(self.sync_status_label, 1, 1, 1, 1)

        self.label_5 = QLabel(self.ncd_tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.savedata_edit = QLineEdit(self.ncd_tab)
        self.savedata_edit.setObjectName(u"savedata_edit")

        self.gridLayout_3.addWidget(self.savedata_edit, 2, 1, 1, 1)

        self.label_12 = QLabel(self.ncd_tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.open_savedata_btn = QPushButton(self.ncd_tab)
        self.open_savedata_btn.setObjectName(u"open_savedata_btn")

        self.horizontalLayout_2.addWidget(self.open_savedata_btn)

        self.change_savedata_btn = QPushButton(self.ncd_tab)
        self.change_savedata_btn.setObjectName(u"change_savedata_btn")

        self.horizontalLayout_2.addWidget(self.change_savedata_btn)

        self.fix_ncd_btn = QPushButton(self.ncd_tab)
        self.fix_ncd_btn.setObjectName(u"fix_ncd_btn")

        self.horizontalLayout_2.addWidget(self.fix_ncd_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.ncd_tab, "")
        self.adva_tab = QWidget()
        self.adva_tab.setObjectName(u"adva_tab")
        self.gridLayout_7 = QGridLayout(self.adva_tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.line_6 = QFrame(self.adva_tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_6, 1, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 2, 0, 1, 2)

        self.run_arg_edit = QLineEdit(self.adva_tab)
        self.run_arg_edit.setObjectName(u"run_arg_edit")

        self.gridLayout_6.addWidget(self.run_arg_edit, 0, 1, 1, 1)

        self.label_9 = QLabel(self.adva_tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.adva_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5c5e\u6027...", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.apply_btn.setText(QCoreApplication.translate("Dialog", u"\u5e94\u7528", None))
        self.open_folder_btn.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.change_path_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u8def\u5f84", None))
        self.change_icon_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u56fe\u6807", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u65f6\u95f4:", None))
        self.last_run_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.total_time_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u8bd1\u540d:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u5939\u8def\u5f84:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6700\u540e\u8fd0\u884c\u65e5\u671f:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u540d\u79f0:", None))
        self.game_name_label.setText(QCoreApplication.translate("Dialog", u"game_name", None))
        self.icon_label.setText(QCoreApplication.translate("Dialog", u"\u65e0\u56fe\u6807", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u8def\u5f84:", None))
        self.change_bg_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u80cc\u666f\u56fe\u7247", None))
        self.edit_metadata_btn.setText(QCoreApplication.translate("Dialog", u"\u7f16\u8f91\u6e38\u620f\u4ecb\u7ecd", None))
        self.edit_txt_btn.setText(QCoreApplication.translate("Dialog", u"\u7f16\u8f91\u653b\u7565", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.norm_tab), QCoreApplication.translate("Dialog", u"\u5e38\u89c4", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u4e91\u540c\u6b65\u72b6\u6001\uff1a", None))
        self.use_ncd_checkbox.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528\u5b58\u6863\u4e91\u540c\u6b65", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u4e91\u540c\u6b65\u8def\u5f84:", None))
        self.save_date_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.sync_savepath_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.sync_status_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u672c\u5730\u5b58\u6863\u8def\u5f84:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u4e91\u5b58\u6863\u65e5\u671f:", None))
        self.open_savedata_btn.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u5b58\u6863\u76ee\u5f55", None))
        self.change_savedata_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u672c\u5730\u5b58\u6863\u8def\u5f84", None))
        self.fix_ncd_btn.setText(QCoreApplication.translate("Dialog", u"\u4fee\u590d\u4e91\u540c\u6b65\u8fde\u63a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ncd_tab), QCoreApplication.translate("Dialog", u"\u5b58\u6863\u4e91\u540c\u6b65", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8fd0\u884c\u53c2\u6570:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adva_tab), QCoreApplication.translate("Dialog", u"\u9ad8\u7ea7", None))
    # retranslateUi

