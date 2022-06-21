# cfw
# 2022.6.22

import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Config import Config
from ui_SettingW import Ui_Dialog
from PIL import Image
from Common import messagebox


class SettingWindow(QDialog, Ui_Dialog):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.setupUi(self)
        self.setup_connect()
        self.create_dict()
        self.config_obj = config
        self.config_dict = self.config_obj.get_config_dict()
        self.load_setting()

    def setup_connect(self):
        self.change_head_btn.clicked.connect(self.change_head)
        self.ok_btn.clicked.connect(self.ok_fun)
        self.cancel_btn.clicked.connect(self.cancel_fun)
        self.apply_btn.clicked.connect(self.apply_fun)

    def create_dict(self):
        self.labels_dict = {
            "user_name": self.user_edit,
            "user_sign": self.sign_edit,
            "user_folder": self.folder_path_edit,
            "ncd_path": self.ncd_folder_edit,
        }
        self.checkbox_dict = {
            "waifu": self.waifu2x_checkbox,
        }

    def load_setting(self):
        user_name = self.config_dict["user_name"]
        head_path = user_name + ".jpg"
        # 载入labels,linedit
        for key, labels in self.labels_dict.items():
            labels.setText(self.config_dict[key])
        # 载入checkbox
        for key, checkbox in self.checkbox_dict.items():
            checkbox.setChecked(self.config_dict[key])
        # 载入用户名
        self.user_label.setText(user_name)
        # 载入用户头像
        if os.path.exists(head_path):
            self.head_label.setPixmap(QPixmap(head_path))

    def save_setting(self) -> bool:
        # 检查用户名是否为空
        if self.user_label.text() == "":
            messagebox(self, QMessageBox.Critical, "错误!", "用户名称不得为空!")
            return False
        # 写入
        for key, label in self.labels_dict.items():
            self.config_obj.save_config(key, label.text())
        for key, checkbox in self.checkbox_dict.items():
            self.config_obj.save_config(key, checkbox.isChecked())
        return True

    def change_head(self):
        new_head_path = QFileDialog.getOpenFileName(
            self, "请选择头像图片...", filter="图片文件 (*.png *.jpg *.jpeg)"
        )
        new_head_path = os.path.normpath(new_head_path[0])
        if new_head_path == ".":
            return
        head_image = Image.open(new_head_path)
        proc_image = head_image.resize((150, 150), Image.ANTIALIAS)
        save_path = self.config_dict["user_name"] + ".jpg"
        proc_image.save(save_path)
        self.load_setting()

    def ok_fun(self):
        if self.save_setting():
            self.close()

    def cancel_fun(self):
        self.close()

    def apply_fun(self):
        self.save_setting()
        self.load_setting()
