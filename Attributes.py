# cfw
# 2022.6.26

import os

from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Common import messagebox
from Config import Config, GameData
from SavedataSync import *
from ui.ui_AttributesW import Ui_Dialog


class AttributesWindow(QDialog, Ui_Dialog):
    def __init__(self, config: Config, game_data: GameData, game_name: str) -> None:
        super().__init__()
        self.setupUi(self)
        self.setup_connect()
        self.config_obj = config
        self.game_data_obj = game_data
        self.game_name = game_name
        self.ncd_path = self.config_obj.confdata_dict["ncd_path"]
        self.create_dict()
        self.load_game_info()
        self.load_sync_info()

    def setup_connect(self):
        # 公共按钮
        self.ok_btn.clicked.connect(self.ok_func)
        self.cancel_btn.clicked.connect(self.cancel_func)
        self.apply_btn.clicked.connect(self.apply_func)
        # 常规选项卡
        self.open_folder_btn.clicked.connect(self.open_folder)
        self.change_path_btn.clicked.connect(self.change_path)
        self.change_icon_btn.clicked.connect(self.change_icon)
        self.change_bg_btn.clicked.connect(self.change_bg)
        self.edit_metadata_btn.clicked.connect(self.edit_metadata)
        self.edit_txt_btn.clicked.connect(self.edit_txt)
        self.remove_game_btn.clicked.connect(self.remove_game)
        # 存档云同步选项卡
        self.setting_sync_btn.clicked.connect(self.setting_sync)
        self.open_savedata_btn.clicked.connect(self.open_savedata)
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

    def load_game_info(self):
        # 获取游戏信息
        self.game_info = self.game_data_obj.get_game_info(self.game_name)
        # 显示游戏本名
        self.game_name_label.setText(self.game_name)
        self.game_name_edit.setText(self.game_name)
        # 显示游戏图标
        icon_path = os.path.join("image", self.game_name + "_ico.png")
        self.icon_label.setPixmap(QPixmap(icon_path))
        # 显示其余信息
        for key1, widget1 in self.labels_dict.items():
            widget1.setText(self.game_info[key1])
        for key2, widget2 in self.line_edit_dict.items():
            widget2.setText(self.game_info[key2])
            widget2.setCursorPosition(0)
        if self.game_info["enable_sync"]:
            self.sync_enable_label.setText("已启用")
        else:
            self.sync_enable_label.setText("未启用")

    def get_ncd_savepath(self, savedata_path: str):
        save_folder_base_name = os.path.basename(savedata_path)
        ncd_savepath = os.path.join(
            self.ncd_path, self.game_name, save_folder_base_name
        )
        return ncd_savepath

    def load_sync_info(self):
        ncd_savepath = self.get_ncd_savepath(self.game_info["savedata_path"])
        local_savepath = self.game_info["savedata_path"]
        if self.game_info["enable_sync"]:
            result = check_sync_status(local_savepath, ncd_savepath)
            if result is None:
                self.sync_status_label.setText("路径设置错误")
            if result is False:
                self.sync_status_label.setText("未进行同步连接")
            if isinstance(result, dict):
                for key, widget in self.sync_dict.items():
                    widget.setText(result[key])
                self.setting_sync_btn.setText("断开存档云同步")

    def open_folder(self):
        folder_path = self.game_info["game_path"]
        os.startfile(folder_path)

    def change_path(self):
        # 选择游戏文件夹
        new_game_path = QFileDialog.getExistingDirectory(
            self, "请选择游戏文件夹...", self.game_folder_edit.text()
        )
        if new_game_path != "":
            self.game_folder_edit.setText(new_game_path)
        # 选择游戏程序文件
        new_exe_path = QFileDialog.getOpenFileName(self, "请选择游戏程序文件...", filter="*.exe")
        new_exe_path = new_exe_path[0]
        if new_exe_path != "":
            self.exe_path_edit.setText(new_exe_path)

    def change_icon(self):
        new_icon_path = QFileDialog.getOpenFileName(
            self, "请选择游戏图标图片...", filter="图片文件 (*.png *.jpg *.jpeg)"
        )
        new_icon_path = new_icon_path[0]
        if new_icon_path == "":
            return
        icon_image = Image.open(new_icon_path)
        proc_image = icon_image.resize((16, 16))
        save_path = os.path.join("image", self.game_name + "_icon.png")
        proc_image.save(save_path)

    def change_bg(self):
        # 选择一个图片文件，尝试压缩成1600*900
        # 百度\谷歌图片在线？
        # 然后如果存在同名图片，则删除后覆盖
        # emmm
        new_bg_path = QFileDialog.getOpenFileName(
            self, "请选择背景图片...", filter="图片文件 (*.png *.jpg *.jpeg)"
        )
        new_bg_path = new_bg_path[0]
        if new_bg_path == "":
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

    def remove_game(self):
        replay = messagebox(
            self,
            QMessageBox.Warning,
            "警告",
            "移除该游戏会同时移除背景图片、游戏图标、游戏攻略、游戏介绍、云同步存档(您不会丢失您的存档)，是否移除?",
            "yesno",
        )
        if replay == 1:
            return
        self.game_data_obj.del_game(self.game_name)
        # 删除元数据\攻略\背景图片\图标
        bg_path = os.path.join("image", self.game_name + ".jpg")
        metadata_path = os.path.join("metadata", self.game_name + ".txt")
        txt_path = os.path.join("metadata", self.game_name + "_txt.txt")
        icon_path = os.path.join("image", self.game_name + "_icon.png")
        # 断开存档云同步
        self.close()

    def setting_sync(self):
        # 检查同步是否开启
        if self.game_info["enable_sync"]:
            # 检测同步状态
            pass
        else:  # 进入创建流程
            self.init_create_sync()
            self.load_game_info()
            self.load_sync_info()

    def open_savedata(self):
        path = self.game_info["savedata_path"]
        real_path = os.path.realpath(path)
        if os.path.exists(real_path):
            os.startfile(real_path)
        else:
            messagebox(self, QMessageBox.Critical, "错误!", "游戏存档路径错误!")

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
        if new_name in self.game_data_obj._gamedata_dict:
            messagebox(self, QMessageBox.Critical, "错误!", "已存在相同名称的游戏!")
            return False
        old_game_info = self.game_data_obj.get_game_info(old_name)
        self.game_data_obj.del_game(old_name)
        self.game_data_obj.create_game(new_name, old_game_info)
        # 重命名元数据\攻略文件\背景图片\游戏图标
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
        for src, dst in rename_dict.items():
            if os.path.exists(dst):
                continue
            if os.path.exists(src):
                # 重命名
                os.rename(src, dst)
        # 重命名对应的云存档
        if self.game_info["enable_sync"]:
            local_savepath = self.game_info["savedata_path"]
            old_ncd_gamepath = os.path.join(self.ncd_path, old_name)
            new_ncd_gamepath = os.path.join(self.ncd_path, new_name)
            if not del_sync(local_savepath, old_ncd_gamepath):
                messagebox(self, QMessageBox.Critical, "错误!", "重命名云存档时发生错误!")
            if not create_sync(local_savepath, new_ncd_gamepath):
                messagebox(self, QMessageBox.Critical, "错误!", "重命名云存档时发生错误!")
        return True

    def init_create_sync(self):
        # 首先检测云端文件夹合法性
        if not os.path.exists(self.ncd_path):
            messagebox(self, QMessageBox.Critical, "错误!", "请检查设置中的云端存档文件夹路径!")
            return
        # 选择游戏存档文件夹
        local_savepath = QFileDialog.getExistingDirectory(
            self, "请选择游戏存档文件夹...", self.game_folder_edit.text()
        )
        if local_savepath == "":
            return
        else:
            local_savepath = local_savepath
            self.savedata_label.setText(local_savepath)
        # 检测存档路径合法性,防止产生回环云存档
        pre = os.path.commonprefix([self.ncd_path, local_savepath])
        if pre == self.ncd_path:
            messagebox(self, QMessageBox.Critical, "错误!", "本地存档文件夹路径错误!")
            return
        # 获取云端文件夹路径
        ncd_gamepath = os.path.join(self.ncd_path, self.game_name)
        # 创建符号链接
        result = create_sync(local_savepath, ncd_gamepath)
        if isinstance(result, str):
            messagebox(self, QMessageBox.Critical, "错误!", "创建同步连接错误!" + result)
            return
        # 重新写入路径数据
        self.game_data_obj.save_game_data(
            self.game_name, "savedata_path", local_savepath
        )
        self.game_data_obj.save_game_data(self.game_name, "enable_sync", True)

    def init_del_sync(self):
        replay = messagebox(
            self,
            QMessageBox.Warning,
            "警告!",
            "这将会停止云端同步!该操作不可逆,你目前的云端存档会取回本地,不会丢失.",
            "yesno",
        )
        if replay == 1:  # 取消按钮
            return
        local_savepath = self.game_info["savedata_path"]
        ncd_gamepath = os.path.join(self.ncd_path, self.game_name)
        result = del_sync(local_savepath, ncd_gamepath)
        if result:
            self.game_data_obj.save_game_data(self.game_name, "enable_sync", False)
        else:
            messagebox(
                self,
                QMessageBox.Critical,
                "错误!",
                "断开同步连接错误!如果存档丢失请到本程序目录下'backup'文件夹寻找.",
            )

    def ok_func(self):
        if self.save_game_data():
            self.close()

    def cancel_func(self):
        self.close()

    def apply_func(self):
        self.save_game_data()
