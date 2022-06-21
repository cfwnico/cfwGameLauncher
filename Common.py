# cfw
# 2022.6.21
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


def messagebox(parent, icon: QIcon, title: str, text: str, button="yes", buttons=None):
    """[ 该函数封装一个Qt对话框类方便重复调用 ]

    参数:
        parent (QWindow): [ 该对话框的父窗口 ]
        icon (QIcon): [ 该对话框显示的图标 ]
        图标参数:Warning(惊叹号),Question(问号),Critical(错误)
        title (str): [ 该对话框的标题 ]
        text (str): [ 该对话框的内容 ]
        button (str): [ 指定显示的按钮;默认参数为"yes"->只显示确定按钮;"yesno"->显示确定和取消按钮 ]
        buttons (dict): [ {按钮内容QMessagebox.Role} ]

    返回:int
        确定返回0,
        取消返回1,
        按钮越多返回值根据添加顺序依次类推,
        关闭返回值和最后一个按钮返回值相同.
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
