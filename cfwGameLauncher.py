# cfw
# 2022.6.23
# 需要修复currentItemChanged产生的信号嵌套触发问题

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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, config: Config, gamedata: GameData) -> None:
        super().__init__()
        self.config_obj = config
        self.game_data_obj = gamedata
        self.setupUi(self)
        self.setup_ui()
        self.setup_connect()
        self.load_game()

    def setup_ui(self):
        print("setup ui")

    def setup_connect(self):
        self.gamelist_widget.currentItemChanged.connect(self.load_game_data)
        self.gamelist_widget.itemDoubleClicked.connect(self.attributes)
        self.scan_game_btn.clicked.connect(self.scan_game)
        self.setting_btn.clicked.connect(self.setting)
        self.playgame_btn.clicked.connect(self.play_game)
        self.home_btn.clicked.connect(self.attributes)

    def load_game(self):
        self.gamelist_widget.clear()
        game_list = self.game_data_obj.get_game_list()
        for i in game_list:
            item = QListWidgetItem()
            item.setText(i)
            self.gamelist_widget.addItem(item)
        self.gamelist_widget.setCurrentRow(0)

    def load_game_data(self, item: QListWidgetItem = None):
        if item is None:
            selcet_item = self.gamelist_widget.selectedItems()[0]
            key_value = selcet_item.text()
        else:
            key_value = item.text()
        game_info = self.game_data_obj.get_game_data(key_value)
        # 显示游戏译名
        self.game_name = game_info["nick_name"]
        self.gamename_label.setText(self.game_name)
        # 设置游戏文件夹路径
        self.game_path = game_info["game_path"]
        # 设置游戏程序路径
        self.exe_path = game_info["exe_path"]
        # 获取最后运行时间
        self.last_run_label.setText(game_info["last_time"])
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

    def scan_game(self):
        # 批量扫描游戏
        scan_game_path = QFileDialog.getExistingDirectory(self, "请选择需要扫描的文件夹...")
        scan_game_path = os.path.normpath(scan_game_path)
        if scan_game_path == ".":
            return
        dir = os.scandir(scan_game_path)
        for i in dir:
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
                "ncd_path": "N\A",
            }
            self.game_data_obj.create_game(i.name, game_info_dict)
        self.load_game()

    def play_game(self):
        # 运行游戏
        if os.path.exists(self.exe_path):
            os.startfile(self.exe_path)
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

    def attributes(self, item):
        # 打开属性窗口
        game_name = item.text()
        attributes_win = AttributesWindow(
            self.config_obj, self.game_data_obj, game_name
        )
        attributes_win.exec()
        self.load_game()
        self.load_game_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = Config("userdata\config.json")
    gamedata = GameData("userdata\gamedata.json")
    main_window = MainWindow(config, gamedata)
    main_window.show()
    app.exec()
