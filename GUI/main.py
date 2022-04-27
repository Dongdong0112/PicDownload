import configparser
import os
import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from maingui import Ui_MainPage


class MyMainForm(QMainWindow, Ui_MainPage):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.Configuration()
        self.setupUi(self)

    # 检测配置文件
    def Configuration(self):
        if os.path.isfile("conf.ini"):
            pass
        else:
            print('[  提示  ]:没有检测到配置文件，生成中!\r')
            try:
                self.cf = configparser.ConfigParser()
                # 往配置文件写入内容
                # 用户主页链接
                self.cf.add_section("uid")
                self.cf.set("uid", "video_url", "https://v.douyin.com/8cp21xg/")
                # 图片链接
                self.cf.add_section("pid")
                self.cf.set("pid", "pic_url", "https://v.douyin.com/FNakbka/")
                # 保存地址
                self.cf.add_section("save")
                self.cf.set("save", "save", ".\\Download\\")
                # 视频保存地址
                self.cf.add_section("video_save")
                self.cf.set("video_save", "video_dir", ".\\Video\\")
                # 图片保存地址
                self.cf.add_section("pic_save")
                self.cf.set("pic_save", "pic_dir", ".\\Picture\\")
                # 音乐保存地址
                self.cf.add_section("music_save")
                self.cf.set("music_save", "music_dir", ".\\Music\\")

                with open("conf.ini", "a+", encoding='utf-8') as f:
                    self.cf.write(f)
                print('[  提示  ]:生成成功!\r')
            except:
                input('[  提示  ]:生成失败,正在为您下载配置文件!\r')
                r = requests.get('https://github.com/Dongdong0112/PicDownload/blob/915776ef3659ed7e57fb92f9140925bfcc18f7b8/conf.ini')
                with open("conf.ini", "a+") as conf:
                    conf.write(r.content)
                sys.exit()


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 去掉窗口标题栏和按钮
    myWin.setWindowFlags(Qt.FramelessWindowHint)
    # 设置窗口真透明
    myWin.setAttribute(Qt.WA_TranslucentBackground)
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
