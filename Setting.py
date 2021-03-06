# cfw
# 2022.6.26

import json
import os
from shutil import copyfile, copytree
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Config import Config, GameData
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
        self.ok_btn.clicked.connect(self.ok_func)
        self.cancel_btn.clicked.connect(self.cancel_func)
        self.apply_btn.clicked.connect(self.apply_func)
        # 常规选项卡
        self.change_head_btn.clicked.connect(self.change_head)
        self.open_folder_btn.clicked.connect(self.open_folder)
        self.change_folder_btn.clicked.connect(self.change_folder)
        # 云同步选项卡
        self.open_ncd_btn.clicked.connect(self.open_ncd)
        self.clu_size_btn.clicked.connect(self.clu_size)
        self.change_ncd_btn.clicked.connect(self.change_ncd)
        self.manage_all_btn.clicked.connect(self.manage_all_cloudsave)
        # 高级选项卡
        self.export_bg_btn.clicked.connect(self.export_bg)
        self.export_save_btn.clicked.connect(self.export_savedata)
        self.edit_json_btn.clicked.connect(self.edit_json)

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
        new_head_path = new_head_path[0]
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
        if new_folder_path != "":
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
        if new_ncd_path != "":
            self.ncd_folder_edit.setText(new_ncd_path)

    def manage_all_cloudsave(self):
        pass

    def export_bg(self):
        self.export_bg_btn.setText("正在导出背景图片...请耐心等待...")
        QApplication.processEvents()
        with open("userdata\\gamedata.json", "r", encoding="utf-8") as f:
            gamedata_dict: dict = json.load(f)
        export_path = "export_bg"
        if not os.path.exists(export_path):
            os.mkdir("export_bg")
        v = 0
        for i in gamedata_dict.keys():
            src = os.path.join("image", i + ".jpg")
            dst = os.path.join("export_bg", i + ".jpg")
            if os.path.exists(src):
                copyfile(src, dst)
                v += 1
        messagebox(self, QMessageBox.Information, "完成", f"共导出{v}张背景图片!")
        self.export_bg_btn.setText("导出所有背景图片")
        os.startfile("export_bg")

    def export_savedata(self):
        self.export_save_btn.setText("正在导出存档...请耐心等待...")
        QApplication.processEvents()
        game_data_obj = GameData("userdata\\gamedata.json")
        export_root_path = "export_savedata"
        if not os.path.exists(export_root_path):
            os.mkdir(export_root_path)
        game_list = game_data_obj.get_game_list()
        v = 0
        for i in game_list:
            game_info = game_data_obj.get_game_info(i)
            src_path = game_info["savedata_path"]
            # 追踪符号链接
            src_path = os.path.normpath(src_path)
            src_path = os.path.realpath(src_path)
            # 检测存档合法性
            if os.path.exists(src_path):
                dst_path = os.path.join("export_savedata", i)
                copytree(src_path, dst_path)
                v += 1
        messagebox(self, QMessageBox.Information, "完成", f"共导出{v}个游戏存档!")
        os.startfile("export_savedata")
        self.export_save_btn.setText("导出所有游戏存档")

    def edit_json(self):
        os.startfile("userdata")

    def ok_func(self):
        if self.save_setting():
            self.close()

    def cancel_func(self):
        self.close()

    def apply_func(self):
        self.save_setting()
        self.load_setting()
