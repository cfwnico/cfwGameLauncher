# cfw
# 2022.6.22

import os

from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Common import messagebox
from Config import Config, GameData
from ui.ui_AttributesW import Ui_Dialog
from SavedataSync import *


class AttributesWindow(QDialog, Ui_Dialog):
    def __init__(self, config: Config, game_data: GameData, game_name: str) -> None:
        super().__init__()
        self.setupUi(self)
        self.setup_connect()
        self.config_obj = config
        self.game_data_obj = game_data
        self.game_name = game_name
        self.create_dict()
        self.load_game_data()
        self.load_sync_info()

    def setup_connect(self):
        # 公共按钮
        self.ok_btn.clicked.connect(self.ok_fun)
        self.cancel_btn.clicked.connect(self.cancel_fun)
        self.apply_btn.clicked.connect(self.apply_fun)
        # 常规选项卡
        self.open_folder_btn.clicked.connect(self.open_folder)
        self.change_path_btn.clicked.connect(self.change_path)
        self.change_icon_btn.clicked.connect(self.change_icon)
        self.change_bg_btn.clicked.connect(self.change_bg)
        self.edit_metadata_btn.clicked.connect(self.edit_metadata)
        self.edit_txt_btn.clicked.connect(self.edit_txt)
        # 存档云同步选项卡

        self.open_savedata_btn
        self.change_savedata_btn
        self.fix_ncd_btn

    def create_dict(self):
        self.line_edit_dict = {
            "nick_name": self.nick_name_edit,
            "game_path": self.game_folder_edit,
            "exe_path": self.exe_path_edit,
            "ps": self.ps_edit,
        }
        self.labels_dict = {
            "last_time": self.last_run_label,
            "total_time": self.total_time_label,
            "savedata_path": self.savedata_label,
        }
        self.sync_dict = {
            "status": self.sync_status_label,
            "ncd_savepath": self.sync_savepath_label,
            "time": self.save_date_label,
        }

    def load_game_data(self):
        self.game_info = self.game_data_obj.get_game_data(self.game_name)
        # 显示游戏本名
        self.game_name_label.setText(self.game_name)
        self.game_name_edit.setText(self.game_name)
        # 显示其余信息
        for key1, widget1 in self.labels_dict.items():
            widget1.setText(self.game_info[key1])
        for key2, widget2 in self.line_edit_dict.items():
            widget2.setText(self.game_info[key2])
            widget2.setCursorPosition(0)
        self.use_ncd_checkbox.setChecked(self.game_info["enable_sync"])
        self.use_ncd_checkbox.stateChanged.connect(self.use_ncd)

    def load_sync_info(self):
        ncd_path = self.config_obj.confdata_dict["ncd_path"]
        save_folder_base_name = os.path.basename(self.game_info["savedata_path"])
        ncd_savepath = os.path.join(ncd_path, self.game_name, save_folder_base_name)
        local_savepath = self.game_info["savedata_path"]
        if self.game_info["enable_sync"]:
            result = check_sync_status(ncd_savepath, local_savepath)
            print(result)
            if result is None:
                self.sync_status_label.setText("路径设置错误")
            if result is False:
                self.sync_status_label.setText("未进行同步连接")
            if isinstance(result, dict):
                for key, widget in self.sync_dict.items():
                    widget.setText(result[key])

    def open_folder(self):
        folder_path = self.game_info["game_path"]
        os.startfile(folder_path)

    def change_path(self):
        # 选择游戏文件夹
        new_game_path = QFileDialog.getExistingDirectory(
            self, "请选择游戏文件夹...", self.game_folder_edit.text()
        )
        new_game_path = os.path.normpath(new_game_path)
        if new_game_path != ".":
            new_game_path = new_game_path
            self.game_folder_edit.setText(new_game_path)
        # 选择游戏程序文件
        new_exe_path = QFileDialog.getOpenFileName(self, "请选择游戏程序文件...", filter="*.exe")
        new_exe_path = os.path.normpath(new_exe_path[0])
        if new_exe_path != ".":
            new_exe_path = new_exe_path
            self.exe_path_edit.setText(new_exe_path)
        # 选择游戏存档文件夹
        # new_save_path = QFileDialog.getExistingDirectory(
        #     self, "请选择游戏存档文件夹...", self.game_folder_edit.text()
        # )
        # new_save_path = os.path.normpath(new_save_path)
        # if new_save_path != ".":
        #     new_save_path = new_save_path
        #     self.savedata_edit.setText(new_save_path)

    def change_icon(self):
        pass

    def change_bg(self):
        # 选择一个图片文件，尝试压缩成1600*900
        # 百度\谷歌图片在线？
        # 然后如果存在同名图片，则删除后覆盖
        # emmm
        new_bg_path = QFileDialog.getOpenFileName(
            self, "请选择背景图片...", filter="图片文件 (*.png *.jpg *.jpeg)"
        )
        new_bg_path = os.path.normpath(new_bg_path[0])
        if new_bg_path == ".":
            return
        bg_image = Image.open(new_bg_path)
        w, h = bg_image.size
        proc_image = bg_image.resize((1600, int(h * 1600 / w)))
        save_path = os.path.join("image", self.game_name + ".jpg")
        proc_image.save(save_path)

    def edit_metadata(self):
        metadata_path = os.path.join("metadata", self.game_name + ".txt")
        os.startfile(metadata_path)

    def edit_txt(self):
        txt_path = os.path.join("metadata", self.game_name + "_txt.txt")
        os.startfile(txt_path)

    def save_game_data(self) -> bool:
        # 检查游戏名称是否为空
        if self.game_name_edit.text() == "":
            messagebox(self, QMessageBox.Critical, "错误!", "游戏名称不得为空!")
            return False
        # 写入数据
        for key, widget in self.labels_dict.items():
            self.game_data_obj.save_game_data(self.game_name, key, widget.text())
        for key, widget in self.line_edit_dict.items():
            self.game_data_obj.save_game_data(self.game_name, key, widget.text())
        # 更改游戏名称
        if self.game_name_edit.text() != self.game_name:
            if self.change_game_name(self.game_name, self.game_name_edit.text()):
                return True
            else:
                return False
        else:
            return True

    def change_game_name(self, old_name: str, new_name: str) -> bool:
        # 检查新名称
        if new_name in self.game_data_obj.gamedata_dict:
            messagebox(self, QMessageBox.Critical, "错误!", "已存在相同名称的游戏!")
            return False
        old_game_data_dict = self.game_data_obj.get_game_data(old_name)
        self.game_data_obj.del_game(old_name)
        self.game_data_obj.create_game(new_name, old_game_data_dict)
        # 确定路径
        src_bg_path = os.path.join("image", old_name + ".jpg")
        dst_bg_path = os.path.join("image", new_name + ".jpg")
        src_path = os.path.join("metadata", old_name + ".txt")
        dst_path = os.path.join("metadata", new_name + ".txt")
        src_txt_path = os.path.join("metadata", old_name + "_txt.txt")
        dst_txt_path = os.path.join("metadata", new_name + "_txt.txt")
        # 创建对应的dict
        rename_dict = {
            src_bg_path: dst_bg_path,
            src_path: dst_path,
            src_txt_path: dst_txt_path,
        }
        # 检查路径
        for src, tag in rename_dict.items():
            if os.path.exists(tag):
                continue
            if os.path.exists(src):
                os.rename(src, tag)
        return True

    def use_ncd(self, checkbox_stats: int):
        if checkbox_stats == 0:
            print("关闭同步连接，询问是否删除云端存档")
        elif checkbox_stats == 2:
            print("打开同步连接，进入创建流程")
        print(checkbox_stats)

    def ok_fun(self):
        if self.save_game_data():
            self.close()

    def cancel_fun(self):
        self.close()

    def apply_fun(self):
        self.save_game_data()
