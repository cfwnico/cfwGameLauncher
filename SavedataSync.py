# cfw
# 2022.6.25

import os
import shutil
import traceback
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Common import get_edit_time, path_is_symlink


def check_sync_status(local_savepath: str, ncd_savepath: str):
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


def create_sync(local_savepath: str, ncd_gamepath: str):
    # ncd_gamepath:such as:D:\cfwcloud\SaveDataSync\Summer Pockets
    # 安全起见再次检查合法性
    if not os.path.exists(local_savepath):
        return "本地游戏存档文件夹不存在,请选择正确的路径!"
    if os.path.exists(ncd_gamepath):
        if len(os.path.dirname(ncd_gamepath)) != 0:
            return "云端文件夹存在该游戏存档,请检查!"
    else:
        os.makedirs(ncd_gamepath)
    shutil.move(local_savepath, ncd_gamepath)
    base_name = os.path.basename(local_savepath)
    ncd_savepath = os.path.join(ncd_gamepath, base_name)
    # 创建符号链接,需要UAC提权
    try:
        os.symlink(ncd_savepath, local_savepath, True)
    except:
        return False
    return True


def del_sync(local_savepath: str, ncd_gamepath: str):
    try:
        base_name = os.path.basename(local_savepath)
        ncd_savepath = os.path.join(ncd_gamepath, base_name)
        os.remove(local_savepath)
        shutil.copytree(ncd_savepath, local_savepath)
        shutil.rmtree(ncd_gamepath)
        return True
    except Exception:
        log = traceback.format_exc()
        print(log)
        return False


def fix_sync(local_savepath: str, ncd_savepath: str):
    pass


def change_name_sync(local_savepath: str, ncd_savepath: str):
    pass


def get_savedata_info(savedata_path: str):
    edit_time = get_edit_time(savedata_path)
    info = {"status": "已同步", "time": edit_time, "ncd_savepath": savedata_path}
    return info
