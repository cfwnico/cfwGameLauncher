# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttributesWYHpvqk.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QWidget)

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
        self.line_2 = QFrame(self.norm_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 9, 0, 1, 2)

        self.label_3 = QLabel(self.norm_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.nick_name_edit = QLineEdit(self.norm_tab)
        self.nick_name_edit.setObjectName(u"nick_name_edit")

        self.gridLayout_2.addWidget(self.nick_name_edit, 5, 1, 1, 1)

        self.label_6 = QLabel(self.norm_tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.label = QLabel(self.norm_tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 14, 0, 1, 1)

        self.game_name_edit = QLineEdit(self.norm_tab)
        self.game_name_edit.setObjectName(u"game_name_edit")

        self.gridLayout_2.addWidget(self.game_name_edit, 4, 1, 1, 1)

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


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 12, 0, 1, 2)

        self.label_7 = QLabel(self.norm_tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)

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


        self.gridLayout_2.addLayout(self.horizontalLayout, 10, 0, 1, 2)

        self.label_8 = QLabel(self.norm_tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 15, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 16, 0, 1, 2)

        self.label_2 = QLabel(self.norm_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.game_folder_edit = QLineEdit(self.norm_tab)
        self.game_folder_edit.setObjectName(u"game_folder_edit")

        self.gridLayout_2.addWidget(self.game_folder_edit, 6, 1, 1, 1)

        self.line = QFrame(self.norm_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 2)

        self.exe_path_edit = QLineEdit(self.norm_tab)
        self.exe_path_edit.setObjectName(u"exe_path_edit")

        self.gridLayout_2.addWidget(self.exe_path_edit, 7, 1, 1, 1)

        self.line_4 = QFrame(self.norm_tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 13, 0, 1, 2)

        self.ps_edit = QLineEdit(self.norm_tab)
        self.ps_edit.setObjectName(u"ps_edit")

        self.gridLayout_2.addWidget(self.ps_edit, 8, 1, 1, 1)

        self.label_4 = QLabel(self.norm_tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.remove_game_btn = QPushButton(self.norm_tab)
        self.remove_game_btn.setObjectName(u"remove_game_btn")

        self.horizontalLayout_5.addWidget(self.remove_game_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 18, 0, 1, 2)

        self.total_time_label = QLabel(self.norm_tab)
        self.total_time_label.setObjectName(u"total_time_label")

        self.gridLayout_2.addWidget(self.total_time_label, 15, 1, 1, 1)

        self.last_run_label = QLabel(self.norm_tab)
        self.last_run_label.setObjectName(u"last_run_label")

        self.gridLayout_2.addWidget(self.last_run_label, 14, 1, 1, 1)

        self.line_7 = QFrame(self.norm_tab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 17, 0, 1, 2)

        self.line_3 = QFrame(self.norm_tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 11, 0, 1, 2)

        self.game_name_label = QLabel(self.norm_tab)
        self.game_name_label.setObjectName(u"game_name_label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.game_name_label.setFont(font)
        self.game_name_label.setAlignment(Qt.AlignCenter)
        self.game_name_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.game_name_label, 2, 1, 1, 1)

        self.icon_label = QLabel(self.norm_tab)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.icon_label, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 2)

        self.tabWidget.addTab(self.norm_tab, "")
        self.ncd_tab = QWidget()
        self.ncd_tab.setObjectName(u"ncd_tab")
        self.gridLayout_4 = QGridLayout(self.ncd_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sync_savepath_label = QLabel(self.ncd_tab)
        self.sync_savepath_label.setObjectName(u"sync_savepath_label")
        self.sync_savepath_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.sync_savepath_label, 6, 1, 1, 1)

        self.sync_enable_label = QLabel(self.ncd_tab)
        self.sync_enable_label.setObjectName(u"sync_enable_label")

        self.gridLayout_3.addWidget(self.sync_enable_label, 0, 1, 1, 1)

        self.savedata_label = QLabel(self.ncd_tab)
        self.savedata_label.setObjectName(u"savedata_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savedata_label.sizePolicy().hasHeightForWidth())
        self.savedata_label.setSizePolicy(sizePolicy)
        self.savedata_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.savedata_label, 4, 1, 1, 1)

        self.line_10 = QFrame(self.ncd_tab)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_10, 7, 0, 1, 2)

        self.line_5 = QFrame(self.ncd_tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 9, 0, 1, 2)

        self.label_10 = QLabel(self.ncd_tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 11, 0, 1, 2)

        self.label_11 = QLabel(self.ncd_tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_5 = QLabel(self.ncd_tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.setting_sync_btn = QPushButton(self.ncd_tab)
        self.setting_sync_btn.setObjectName(u"setting_sync_btn")

        self.horizontalLayout_2.addWidget(self.setting_sync_btn)

        self.open_savedata_btn = QPushButton(self.ncd_tab)
        self.open_savedata_btn.setObjectName(u"open_savedata_btn")

        self.horizontalLayout_2.addWidget(self.open_savedata_btn)

        self.fix_ncd_btn = QPushButton(self.ncd_tab)
        self.fix_ncd_btn.setObjectName(u"fix_ncd_btn")

        self.horizontalLayout_2.addWidget(self.fix_ncd_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 10, 0, 1, 2)

        self.line_8 = QFrame(self.ncd_tab)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 3, 0, 1, 2)

        self.label_12 = QLabel(self.ncd_tab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 8, 0, 1, 1)

        self.sync_status_label = QLabel(self.ncd_tab)
        self.sync_status_label.setObjectName(u"sync_status_label")

        self.gridLayout_3.addWidget(self.sync_status_label, 2, 1, 1, 1)

        self.save_date_label = QLabel(self.ncd_tab)
        self.save_date_label.setObjectName(u"save_date_label")

        self.gridLayout_3.addWidget(self.save_date_label, 8, 1, 1, 1)

        self.line_9 = QFrame(self.ncd_tab)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_9, 5, 0, 1, 2)

        self.label_14 = QLabel(self.ncd_tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 6, 0, 1, 1)

        self.line_11 = QFrame(self.ncd_tab)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_11, 1, 0, 1, 2)


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
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u8bd1\u540d:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u8def\u5f84:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6700\u540e\u8fd0\u884c\u65e5\u671f:", None))
        self.change_bg_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u80cc\u666f\u56fe\u7247", None))
        self.edit_metadata_btn.setText(QCoreApplication.translate("Dialog", u"\u7f16\u8f91\u6e38\u620f\u4ecb\u7ecd", None))
        self.edit_txt_btn.setText(QCoreApplication.translate("Dialog", u"\u7f16\u8f91\u653b\u7565", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8:", None))
        self.open_folder_btn.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.change_path_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u8def\u5f84", None))
        self.change_icon_btn.setText(QCoreApplication.translate("Dialog", u"\u66f4\u6539\u56fe\u6807", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u65f6\u95f4:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6e38\u620f\u540d\u79f0:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u5939\u8def\u5f84:", None))
        self.remove_game_btn.setText(QCoreApplication.translate("Dialog", u"\u79fb\u9664\u6e38\u620f", None))
        self.total_time_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.last_run_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.game_name_label.setText(QCoreApplication.translate("Dialog", u"game_name", None))
        self.icon_label.setText(QCoreApplication.translate("Dialog", u"\u65e0\u56fe\u6807", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.norm_tab), QCoreApplication.translate("Dialog", u"\u5e38\u89c4", None))
        self.sync_savepath_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.sync_enable_label.setText(QCoreApplication.translate("Dialog", u"\u672a\u542f\u7528", None))
        self.savedata_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u4e91\u540c\u6b65\u72b6\u6001\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u4e91\u540c\u6b65:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u672c\u5730\u5b58\u6863\u8def\u5f84:", None))
        self.setting_sync_btn.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528\u5b58\u6863\u4e91\u540c\u6b65", None))
        self.open_savedata_btn.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u5b58\u6863\u76ee\u5f55", None))
        self.fix_ncd_btn.setText(QCoreApplication.translate("Dialog", u"\u4fee\u590d\u4e91\u540c\u6b65\u8fde\u63a5", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u4e91\u5b58\u6863\u65e5\u671f:", None))
        self.sync_status_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.save_date_label.setText(QCoreApplication.translate("Dialog", u"N\\A", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u4e91\u540c\u6b65\u8def\u5f84:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ncd_tab), QCoreApplication.translate("Dialog", u"\u5b58\u6863\u4e91\u540c\u6b65", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8fd0\u884c\u53c2\u6570:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adva_tab), QCoreApplication.translate("Dialog", u"\u9ad8\u7ea7", None))
    # retranslateUi

