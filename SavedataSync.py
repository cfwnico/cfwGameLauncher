# cfw
# 2022.6.22

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Common import messagebox, path_is_symlink
from Config import Config, GameData


class SaveDataSync:
    def __init__(self, ncd_path: str) -> None:
        self.ncd_path = ncd_path

    def check_sync_status(self, savedata_path: str):
        """[ 该函数检查云同步状态并返回相关结果 ]

        参数:
            path (str): [ 路径 ]

        返回:
            True:是符号链接.
            False:本地存档未启用云同步.
            None:本地存档路径错误.
        """
        result = path_is_symlink(savedata_path)
        # 本地存档路径是符号链接->可能已同步
        if result is True:
            pass
        # 本地存档路径不是符号链接->未同步
        elif result is False:
            return False
        # 本地存档路径不存在或指向一个文件->错误的路径设置
        elif result is None:
            return None

    def create_sync(self):
        pass

    def del_sync(self):
        pass

    def fix_sync(self):
        pass
