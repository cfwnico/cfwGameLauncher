# cfw
# 2022.6.22

import os

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Common import get_edit_time, path_is_symlink


def check_sync_status(ncd_savepath: str, local_savepath: str):
    """[ 该函数检查云同步状态并返回相关结果 ]

    参数:
        path (str): [ 路径 ]

    返回:
        dict:{"status": 云同步状态, "time": 云存档最新修改时间, "ncd_savepath": 云存档路径}.
        False:本地存档未启用云同步.
        None:本地存档路径错误.
    """
    # 本地与云端路径相同->错误的路径设置
    if ncd_savepath == local_savepath:
        return None
    result = path_is_symlink(local_savepath)
    # 本地存档路径是符号链接->可能已同步
    if result is True:
        print("本地存档路径是符号链接->可能已同步")
        # 进一步追踪符号连接
        print("进一步追踪符号连接")
        real_local_savepath = os.path.realpath(local_savepath)
        print("real path:" + real_local_savepath)
        if real_local_savepath == ncd_savepath:
            info = get_savedata_info(real_local_savepath)
            return info
    # 本地存档路径不是符号链接->未同步
    elif result is False:
        print("本地存档路径不是符号链接->未同步")
        return False
    # 本地存档路径不存在或指向一个文件->错误的路径设置
    elif result is None:
        print("本地存档路径不存在或指向一个文件->错误的路径设置")
        return None


def get_savedata_info(savedata_path: str):
    edit_time = get_edit_time(savedata_path)
    info = {"status": "已同步", "time": edit_time, "ncd_savepath": savedata_path}
    return info


def create_sync(ncd_savepath: str, local_savepath: str):
    pass


def del_sync(ncd_savepath: str, local_savepath: str):
    pass


def fix_sync(ncd_savepath: str, local_savepath: str):
    pass


def change_name_sync(ncd_savepath: str, local_savepath: str):
    pass
