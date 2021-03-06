# cfw
# 2022.6.28

# ToDo:
# 添加托盘模块
# 实装 运行参数 功能
# metadata爬取,攻略爬取模块
# 在线爬取图片模块
# 缩放图片的算法需要重写
# 云存档管理器

# bug list:
# shutil.copytree路径问题

# tips:
# noramlpath函数后空字符串会变成"."


import os
import sys
import time
from glob import glob

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Attributes import AttributesWindow
from Common import messagebox
from Config import Config, GameData
from Setting import SettingWindow
from ui.ui_MainW import Ui_MainWindow
import subprocess


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, config: Config, gamedata: GameData) -> None:
        super().__init__()
        self.config_obj = config
        self.game_data_obj = gamedata
        self.setupUi(self)
        self.setup_connect()
        self.load_game_list()

    def setup_connect(self):
        self.gamelist_widget.currentItemChanged.connect(self.load_game_info)
        self.gamelist_widget.itemDoubleClicked.connect(self.attributes)
        self.add_game_btn.clicked.connect(self.add_game)
        self.scan_game_btn.clicked.connect(self.scan_game)
        self.sort_btn.clicked.connect(self.sort_game_list)
        self.setting_btn.clicked.connect(self.setting)
        self.playgame_btn.clicked.connect(self.play_game)

    def load_game_list(self, current_row: int = 0):
        self.gamelist_widget.clear()
        game_list = self.game_data_obj.get_game_list()
        self.cache_game_list = game_list
        for i in game_list:
            item = QListWidgetItem()
            item.setText(i)
            icon_path = os.path.join("image", i + "_ico.png")
            if os.path.exists(icon_path):
                item.setIcon(QPixmap(icon_path))
            self.gamelist_widget.addItem(item)
        self.gamelist_widget.setCurrentRow(current_row)

    def update_game_list(self):
        cache_list_set = set(self.cache_game_list)
        game_list = self.game_data_obj.get_game_list()
        game_list_set = set(game_list)
        old_game_set = cache_list_set.difference(game_list_set)
        new_game_set = game_list_set.difference(cache_list_set)
        old_game_list = list(old_game_set)
        new_game_list = list(new_game_set)
        if len(old_game_list) != 0:
            for i in old_game_list:
                item = self.gamelist_widget.findItems(i, Qt.MatchExactly)[0]
                item_row = self.gamelist_widget.row(item)
                self.gamelist_widget.takeItem(item_row)
        if len(new_game_list) != 0:
            for i in new_game_list:
                item = QListWidgetItem()
                item.setText(i)
                self.gamelist_widget.addItem(item)
        self.cache_game_list = game_list

    def load_game_info(self, item: QListWidgetItem = None):
        if item is None:
            selcet_item = self.gamelist_widget.selectedItems()[0]
            key_value = selcet_item.text()
        else:
            key_value = item.text()
        game_info = self.game_data_obj.get_game_info(key_value)
        # 显示游戏译名
        self.game_name = game_info["nick_name"]
        self.gamename_label.setText(self.game_name)
        # 设置游戏文件夹路径
        self.game_path = game_info["game_path"]
        # 设置游戏程序路径
        self.exe_path: str = game_info["exe_path"]
        # 设置最后运行日期
        last_run_text = "最后运行日期\n" + game_info["last_time"]
        self.last_run_label.setText(last_run_text)
        # 设置游戏时间
        total_time_text = "游戏时间\n" + game_info["total_time"]
        self.total_time_label.setText(total_time_text)
        # 显示元数据
        self.metadata_browser.clear()
        self.metadata_path = os.path.join("metadata", key_value + ".txt")
        if os.path.exists(self.metadata_path):
            with open(self.metadata_path, "r", encoding="utf-8") as f:
                metadata = f.read()
            self.metadata_browser.setText(metadata)
        # 显示攻略
        self.txt_browser.clear()
        self.txt_path = os.path.join("metadata", key_value + "_txt.txt")
        if os.path.exists(self.txt_path):
            with open(self.txt_path, "r", encoding="utf-8") as f:
                text = f.read()
            self.txt_browser.setText(text)
        # 设置background
        bg_path = os.path.join("image", key_value + ".jpg")
        if not os.path.exists(bg_path):
            bg_path = r"image\background.jpg"
        pale = self.palette()
        pale.setBrush(QPalette.Window, QBrush(QPixmap(bg_path)))
        self.setPalette(pale)
        # 其他变量获取
        self.run_args: str = game_info["run_args"]

    def add_game(self):
        # 添加游戏
        game_folder_path = self.config_obj.confdata_dict["user_folder"]
        if os.path.exists(game_folder_path):
            folder = game_folder_path
        else:
            folder = ""
        game_path = QFileDialog.getExistingDirectory(self, "请选择游戏文件夹...", folder)
        if game_path == "":
            return
        game_name = os.path.basename(game_path)
        if game_name in self.game_data_obj._gamedata_dict:
            messagebox(
                self, QMessageBox.Critical, "错误!", f"该游戏:'{game_name}'已存在!无法重复添加!"
            )
            return
        exe_path = QFileDialog.getOpenFileName(self, "请选择游戏程序文件...", game_path, "*.exe")
        if exe_path[0] == "":
            return
        game_info_dict = {
            "nick_name": game_name,
            "game_path": game_path,
            "exe_path": exe_path[0],
            "savedata_path": "N\A",
            "last_time": "N\A",
            "total_time": "N\A",
            "ps": "",
            "run_args": "",
            "enable_sync": False,
        }
        self.game_data_obj.create_game(game_name, game_info_dict)
        self.update_game_list()

    def scan_game(self):
        # 批量扫描游戏
        # 需要进行重名处理
        scan_game_path = QFileDialog.getExistingDirectory(self, "请选择需要扫描的文件夹...")
        if scan_game_path == "":
            return
        dir = os.scandir(scan_game_path)
        for i in dir:
            if i.name in self.game_data_obj._gamedata_dict:
                continue
            exe_path_list = glob(os.path.join(i.path, "*.exe"))
            if len(exe_path_list) == 1:
                exe_path = exe_path_list[0]
            else:
                exe_path = "N\A"
            game_info_dict = {
                "nick_name": i.name,
                "game_path": i.path,
                "exe_path": exe_path,
                "savedata_path": "N\A",
                "last_time": "N\A",
                "total_time": "N\A",
                "ps": "",
                "run_args": "",
                "enable_sync": False,
            }
            self.game_data_obj.create_game(i.name, game_info_dict)
        # 断开信号连接防止出现信号回环
        self.gamelist_widget.currentItemChanged.disconnect(self.load_game_info)
        self.load_game_list()
        self.gamelist_widget.currentItemChanged.connect(self.load_game_info)

    def sort_game_list(self):
        self.game_data_obj.sort_game()
        self.gamelist_widget.currentItemChanged.disconnect(self.load_game_info)
        self.load_game_list()
        self.gamelist_widget.currentItemChanged.connect(self.load_game_info)

    def play_game(self):
        # 运行游戏
        if os.path.exists(self.exe_path):
            # 需要UAC提权
            subprocess.call([self.exe_path, self.run_args])
            self.edit_last_runtime()
        else:
            messagebox(self, QMessageBox.Critical, "错误！", "未找到游戏文件，请检查该游戏属性！")

    def edit_last_runtime(self):
        # 计算最后运行时间
        selcet_item = self.gamelist_widget.selectedItems()[0]
        game_name = selcet_item.text()
        now_time = time.localtime()
        format_time = time.strftime("%Y-%m-%d %H:%M", now_time)
        self.game_data_obj.save_game_data(game_name, "last_time", format_time)

    def setting(self):
        # 打开设置窗口
        setting_win = SettingWindow(self.config_obj)
        setting_win.exec()

    def attributes(self, item: QListWidgetItem):
        # 打开属性窗口
        game_name = item.text()
        current_row = self.gamelist_widget.row(item)
        attributes_win = AttributesWindow(
            self.config_obj, self.game_data_obj, game_name
        )
        attributes_win.exec()
        self.update_game_list()
        self.load_game_info()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = Config("userdata\config.json")
    gamedata = GameData("userdata\gamedata.json")
    main_window = MainWindow(config, gamedata)
    main_window.show()
    app.exec()
