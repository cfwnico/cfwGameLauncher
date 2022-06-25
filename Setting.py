# cfw
# 2022.6.23

import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Config import Config
from ui.ui_SettingW import Ui_Dialog
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
        # 公共按钮
        self.ok_btn.clicked.connect(self.ok_fun)
        self.cancel_btn.clicked.connect(self.cancel_fun)
        self.apply_btn.clicked.connect(self.apply_fun)
        # 常规选项卡
        self.change_head_btn.clicked.connect(self.change_head)
        self.open_folder_btn.clicked.connect(self.open_folder)
        self.change_folder_btn.clicked.connect(self.change_folder)
        # 云同步选项卡
        self.open_ncd_btn.clicked.connect(self.open_ncd)
        self.clu_size_btn.clicked.connect(self.clu_size)
        self.change_ncd_btn.clicked.connect(self.change_ncd)
        self.manage_all_btn.clicked.connect(self.manage_all_cloudsave)

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
        head_filename = user_name + ".jpg"
        head_path = os.path.join("userdata", head_filename)
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
        # 载入云同步信息
        ncd_path = self.config_dict["ncd_path"]
        count = len(os.listdir(ncd_path))
        self.ncd_count_label.setText(str(count))

    def save_setting(self) -> bool:
        # 检查用户名是否为空
        if self.user_label.text() == "":
            messagebox(self, QMessageBox.Critical, "错误!", "用户名称不得为空!")
            return False
        # 检测是否更改了用户名,用于更改头像文件
        user_name = self.config_dict["user_name"]
        old_head_filename = user_name + ".jpg"
        old_head_path = os.path.join("userdata", old_head_filename)
        if self.user_edit.text() != user_name:
            new_head_filename = self.user_edit.text() + ".jpg"
            new_head_path = os.path.join("userdata", new_head_filename)
            os.rename(old_head_path, new_head_path)
        # 检测路径是否存在
        # check_path_dict = {
        #     self.folder_path_edit: "游戏库目录",
        #     self.ncd_folder_edit: "云端存档文件夹",
        # }
        # for widget, name in check_path_dict.items():
        #     path = widget.text()
        #     if not os.path.exists(path):
        #         messagebox(self, QMessageBox.Critical, "错误!", f"{name}路径不存在,请设置正确路径!")
        #         return False
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
        if new_head_path == "":
            return
        head_image = Image.open(new_head_path)
        proc_image = head_image.resize((150, 150), Image.ANTIALIAS)
        save_name = self.config_dict["user_name"] + ".jpg"
        save_path = os.path.join("userdata", save_name)
        proc_image.save(save_path)
        self.load_setting()

    def change_folder(self):
        new_folder_path = QFileDialog.getExistingDirectory(
            self, "请选择游戏文件夹...", self.folder_path_edit.text()
        )
        new_folder_path = os.path.normpath(new_folder_path)
        if new_folder_path != "":
            new_folder_path = new_folder_path
            self.folder_path_edit.setText(new_folder_path)

    def open_folder(self):
        folder_path = self.folder_path_edit.text()
        if os.path.exists(folder_path):
            os.startfile(folder_path)
        else:
            messagebox(self, QMessageBox.Critical, "错误!", "请检查游戏库目录路径是否正确!")

    def open_ncd(self):
        ncd_path = self.ncd_folder_edit.text()
        if os.path.exists(ncd_path):
            os.startfile(ncd_path)
        else:
            messagebox(self, QMessageBox.Critical, "错误!", "请检查云端同步文件夹路径是否正确!")

    def clu_size(self):
        dir_path = self.ncd_folder_edit.text()
        if not os.path.exists(dir_path):
            messagebox(self, QMessageBox.Critical, "错误!", "请检查云端同步文件夹路径是否正确!")
            return
        dir_list = []  # 定义一个空列表,存放文件夹的路径
        Size = 0  # 初始化大小
        dir_list.append(dir_path)  # 将路径参数加入列表,处理开始
        while dir_list:  # 循环,直到文件夹列表为空
            dir_path = dir_list.pop()  # 从列表尾部取出一个路径
            dirs = os.listdir(dir_path)  # 获取该路径下所有文件夹及文件
            for ele in dirs:  # 依次处理
                new_path = os.path.join(dir_path, ele)  # 拼接成新路径
                if os.path.isdir(new_path):  # 是文件夹就加入到列表继续处理
                    dir_list.append(new_path)
                if os.path.isfile(new_path):  # 是文件就统计大小进行累加
                    Size = Size + os.path.getsize(new_path)
        format_size = "{:,.2f}".format(Size / 1024 / 1024) + " MB"
        self.ncd_size_label.setText(format_size)

    def change_ncd(self):
        new_ncd_path = QFileDialog.getExistingDirectory(
            self, "请选择云端存档文件夹...", self.ncd_folder_edit.text()
        )
        new_ncd_path = os.path.normpath(new_ncd_path)
        if new_ncd_path != "":
            new_ncd_path = new_ncd_path
            self.ncd_folder_edit.setText(new_ncd_path)

    def manage_all_cloudsave(self):
        pass

    def ok_fun(self):
        if self.save_setting():
            self.close()

    def cancel_fun(self):
        self.close()

    def apply_fun(self):
        self.save_setting()
        self.load_setting()
