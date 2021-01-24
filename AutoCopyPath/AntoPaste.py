# 自动操作剪贴板脚本
import time
import os

import win32con
import win32clipboard

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

cwd = os.getcwd()
last = ""


def get_clipboard_text():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return text


def set_clipboard_text(string):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, string)
    win32clipboard.CloseClipboard()
    print("Set text to clipboard successfully!")


class MyDirEventHandler(FileSystemEventHandler):

    def on_moved(self, event):
        # print("moved", event)
        pass

    def on_created(self, event):
        global last
        # 确保同一操作只触发一次
        if not (last == str(event)):
            last = str(event)
            fileName = str(event.src_path).split("\\")[-1]
            print("created:", fileName)
            res = "![{0}](../assets/{1})".format(fileName, fileName)
            print("res:", res)
            set_clipboard_text(res)

    def on_deleted(self, event):
        # print("deleted", event)
        pass

    def on_modified(self, event):
        # print("modified:", event)
        pass


"""
使用watchdog 监控文件的变化
"""
if __name__ == '__main__':
    # 创建观察者对象
    observer = Observer()
    # 创建事件处理对象
    fileHandler = MyDirEventHandler()

    path = cwd+"\\assets\\"
    # path = "F:\\Desktop\\笔记\\英语\\assets"
    print(path)
    # 为观察者设置观察对象与处理事件对象
    observer.schedule(fileHandler, path, False)
    observer.start()
    print("启动成功：")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
