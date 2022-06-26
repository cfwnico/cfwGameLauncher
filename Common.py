# cfw
# 2022.6.26
import os
from glob import glob
from time import localtime, strftime

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


def messagebox(parent, icon: QIcon, title: str, text: str, button="yes", buttons=None):
    """[ 封装一个Qt对话框类方便重复调用 ]

    参数:
        parent (QWindow): [ 该对话框的父窗口 ]
        icon (QIcon): [ 该对话框显示的图标 ]
        图标参数 (QMessageBox) : [ Warning(惊叹号),Question(问号),Critical(错误),Information(信息) ]
        title (str): [ 该对话框的标题 ]
        text (str): [ 该对话框的内容 ]
        button (str): [ 指定显示的按钮;默认参数为"yes"->只显示确定按钮;"yesno"->显示确定和取消按钮 ]
        buttons (dict): [ {按钮文字 ：QMessagebox.Role} ]

    返回: int
        确定: [ 0 ]
        取消: [ 1 ]

        按钮越多返回值根据添加顺序依次+1,关闭按钮的返回值和最后一个按钮返回的值相同.
    """
    if parent is None:
        msgbox = QMessageBox()
    else:
        msgbox = QMessageBox(parent)
    msgbox.setWindowTitle(title)
    msgbox.setIcon(icon)
    msgbox.setText(text)
    if button == "yes":
        msgbox.addButton("确定", QMessageBox.YesRole)
    elif button == "yesno":
        msgbox.addButton("确定", QMessageBox.YesRole)
        no = msgbox.addButton("取消", QMessageBox.NoRole)
        msgbox.setDefaultButton(no)
    elif button is None:
        if not buttons is None:
            for i in buttons:
                msgbox.addButton(i, buttons[i])
    replay = msgbox.exec()
    return replay


def path_is_symlink(path: str):
    """[ 该函数判断一个文件夹路径是否为符号链接 ]

    参数:
        path (str): [ 路径 ]

    返回:
        True: 是符号链接.
        False: 不是符号链接.
        None: 该路径不存在或者该路径指向一个文件.
    """
    if not os.path.exists(path):
        return None
    if os.path.isfile(path):
        return None
    if os.path.islink(path):
        return True
    else:
        return False


def get_edit_time(path: str):
    """[ 该函数返回路径下所有文件中最新的修改时间 ]

    参数:
        path (str): [ 路径 ]

    返回:str
        str: 获取最新修改日期失败!
        str: %Y年%m月%d日 %H:%M:%S
    """
    time_list = []
    glob_path = os.path.join(path, "*.*")
    file_list = glob(glob_path)
    for i in file_list:
        time = os.path.getmtime(i)
        time_list.append(time)
    if len(time_list) > 0:
        edit_time = max(time_list)
        edit_time_locale = localtime(edit_time)
        fromat_time = strftime("%Y年%m月%d日 %H:%M:%S", edit_time_locale)
    else:
        fromat_time = "获取最新修改日期失败！"
    return fromat_time
