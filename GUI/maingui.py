# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.4
import configparser
import json
import os
import re
import sys
import time
import requests
import Resource

from PIL import Image as img
from tqdm import tqdm
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QIcon
from PyQt5.QtWidgets import QWidget

from one import Ui_image_download_page
from two import Ui_video_download_page
from three import Ui_history_page
from four import Ui_setting_page


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(1091, 729)
        MainPage.setStyleSheet("")
        self.frame_left = QtWidgets.QFrame(MainPage)
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 276, 720))
        self.frame_left.setStyleSheet("background-color: #D8E2DC;\n"
                                      "color: rgb(16, 16, 16);\n"
                                      "border-bottom-left-radius: 25px;\n"
                                      "border-top-left-radius: 25px;\n"
                                      "font: 16pt \"【慧心】奶酪体\";")
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")

        self.Button_image = QtWidgets.QPushButton(self.frame_left)
        self.Button_image.setGeometry(QtCore.QRect(40, 200, 200, 50))
        self.Button_image.setStyleSheet("background-color: #D7DBCA;\n"
                                        "color: rgb(16, 16, 16);\n"
                                        "border-radius: 15px;")
        self.Button_image.setObjectName("Button_image")

        self.Button_video = QtWidgets.QPushButton(self.frame_left)
        self.Button_video.setGeometry(QtCore.QRect(40, 300, 200, 50))
        self.Button_video.setStyleSheet("background-color: #D7DBCA;\n"
                                        "color: rgb(16, 16, 16);\n"
                                        "border-radius: 15px;")
        self.Button_video.setObjectName("Button_video")

        self.Button_setting = QtWidgets.QPushButton(self.frame_left)
        self.Button_setting.setGeometry(QtCore.QRect(40, 500, 200, 50))
        self.Button_setting.setStyleSheet("background-color: #D7DBCA;\n"
                                          "color: rgb(16, 16, 16);\n"
                                          "border-radius: 15px;")
        self.Button_setting.setObjectName("Button_setting")

        self.Button_history = QtWidgets.QPushButton(self.frame_left)
        self.Button_history.setGeometry(QtCore.QRect(40, 400, 200, 50))
        self.Button_history.setStyleSheet("background-color: #D7DBCA;\n"
                                          "color: rgb(16, 16, 16);\n"
                                          "border-radius: 15px;")
        self.Button_history.setObjectName("Button_history")

        self.frame_right = QtWidgets.QFrame(MainPage)
        self.frame_right.setGeometry(QtCore.QRect(276, 72, 804, 648))
        self.frame_right.setStyleSheet("background-color: #F5F6F2;\n"
                                       "border-bottom-right-radius: 25px;")
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")

        self.frame_Background = QtWidgets.QFrame(MainPage)
        self.frame_Background.setGeometry(QtCore.QRect(276, 0, 804, 72))
        self.frame_Background.setStyleSheet("background-color: #DCD9D1;\n"
                                            "border-top-right-radius: 25px;")
        self.frame_Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Background.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_Background.setObjectName("frame_Background")

        self.Button_Min = QtWidgets.QPushButton(self.frame_Background)
        self.Button_Min.setGeometry(QtCore.QRect(684, 20, 21, 21))
        self.Button_Min.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: #37C847;")
        self.Button_Min.setObjectName("Button_Min")

        self.Button_Max = QtWidgets.QPushButton(self.frame_Background)
        self.Button_Max.setGeometry(QtCore.QRect(720, 20, 21, 21))
        self.Button_Max.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: #FFC32D;")
        self.Button_Max.setObjectName("Button_Max")

        self.Button_Close = QtWidgets.QPushButton(self.frame_Background)
        self.Button_Close.setGeometry(QtCore.QRect(756, 20, 21, 21))
        self.Button_Close.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: rgb(255, 81, 53);")
        self.Button_Close.setObjectName("Button_Close")

        self.one = OneForm()
        self.two = TwoForm()
        self.three = ThreeForm()
        self.four = FourForm()

        self.stack = QtWidgets.QStackedLayout(self.frame_right)
        self.stack.addWidget(self.one)
        self.stack.addWidget(self.two)
        self.stack.addWidget(self.three)
        self.stack.addWidget(self.four)

        self.Button_image.clicked.connect(lambda: self.buttonIsClicked(self.Button_image, self.stack))
        self.Button_video.clicked.connect(lambda: self.buttonIsClicked(self.Button_video, self.stack))
        self.Button_history.clicked.connect(lambda: self.buttonIsClicked(self.Button_history, self.stack))
        self.Button_setting.clicked.connect(lambda: self.buttonIsClicked(self.Button_setting, self.stack))

        self.frame_Background.raise_()
        self.frame_left.raise_()
        self.frame_right.raise_()

        self.retranslateUi(MainPage)
        self.Button_Max.clicked.connect(lambda: self.MaxButton())
        self.Button_Min.clicked.connect(lambda: self.MinButton())
        self.Button_Close.clicked.connect(lambda: self.CloseButton())
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def buttonIsClicked(self, button, stack):
        dic = {
            "图片下载": 0,
            "视频下载": 1,
            "历史记录": 2,
            "设置": 3
        }
        a = button.text()
        index = dic[a]
        stack.setCurrentIndex(index)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            pass

    def mousePressEvent(self, e: QMouseEvent):
        try:
            if e.button() == Qt.LeftButton:
                self._isTracking = True
                self._startPos = QPoint(e.x(), e.y())
        except:
            pass

    def mouseReleaseEvent(self, e: QMouseEvent):
        try:
            if e.button() == Qt.LeftButton:
                self._isTracking = False
                self._startPos = None
                self._endPos = None
        except:
            pass

    # 最大化与还原的切换
    def MaxButton(self):
        if self.isMaximized():
            self.showNormal()
            self.Button_Max.setToolTip('最大化')
        else:
            self.showMaximized()
            self.Button_Max.setToolTip('还原')

    # 切换到最小化按钮
    def MinButton(self):
        self.showMinimized()

    # 关闭
    def CloseButton(self):
        sys.exit(0)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "暂时没想好"))
        MainPage.setWindowIcon(QIcon(":/logo/logo.ico"))
        self.Button_image.setText(_translate("MainPage", "图片下载"))
        self.Button_video.setText(_translate("MainPage", "视频下载"))
        self.Button_setting.setText(_translate("MainPage", "设置"))
        self.Button_history.setText(_translate("MainPage", "历史记录"))
        self.Button_Min.setText(_translate("MainPage", "-"))
        self.Button_Max.setText(_translate("MainPage", "口"))
        self.Button_Close.setText(_translate("MainPage", "X"))
        self.Button_Min.setToolTip('最小化')
        self.Button_Max.setToolTip('最大化')
        self.Button_Close.setToolTip('关闭')


class OneForm(QWidget, Ui_image_download_page):
    def __init__(self):
        super(OneForm, self).__init__()
        self.setupUi(self)
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }
        self.printf("#" * 120)
        self.printf(
            """
                                        TuKuDownload V1.1.3
                    使用说明：
                            1、运行软件前先确认目录中是否有 conf.ini 文件
            """
        )
        self.printf("#" * 120)
        self.printf('\r')

        # 保存路径
        self.save = ''
        self.pic_save = ''
        self.music_save = ''
        self.pic_dir = ''
        self.music_dir = ''
        # 图片地址
        self.pic_url = ''
        # 判断是否跳过
        self.jump = ''
        # 记录图片信息
        self.image_info = ''
        self.image_filename = ''
        self.check_filename = ''
        self.music_filename = ''
        self.cursor = ''

    # 槽函数 run 运行
    def run(self):
        # 实例化读取配置文件
        self.cf = configparser.RawConfigParser()
        # 用utf-8防止出错
        self.cf.read("conf.ini", encoding="utf-8")
        # 读取部分配置文件
        self.save = self.cf.get("save", "save")
        self.pic_save = self.cf.get("pic_save", "pic_dir")
        self.music_save = self.cf.get("music_save", "music_dir")

        if self.checkBox_bgm.isChecked():
            self.music_arg = 'yes'
        else:
            self.music_arg = 'no'

        if self.checkBox_ini.isChecked():
            # 从配置文件读取链接
            self.pic_url = self.cf.get("pid", "pic_url")
            self.plainTextEdit.setPlainText(self.pic_url)
            if self.find(self.pic_url) == '':
                print('[  警告  ]:当前配置文件无链接!\r')
                self.printf('[  警告  ]:当前配置文件无链接!\r')
                self.label_header.setText('[  警告  ]:当前配置文件无链接!')
            else:
                print('[  提示  ]:读取本地配置完成!\r')
                self.printf('[  提示  ]:读取本地配置完成!\r')
                self.label_header.setText('[  提示  ]:读取本地配置完成!')
                self.judge_link()
        else:
            self.pic_url = self.plainTextEdit.toPlainText()
            if self.find(self.pic_url) == '':
                print('[  警告  ]:当前无链接!\r')
                self.printf('[  警告  ]:当前无链接!\r')
            else:
                print('[  提示  ]:开始下载!\r')
                self.printf('[  提示  ]:开始下载!\r')
                self.judge_link()

    # 槽函数 clear 清空
    def clear(self):
        text = ''
        self.progressBar_download.reset()
        self.progressBar_conversion.reset()
        self.plainTextEdit.clear()
        self.label_header.setText("当前暂无链接")
        self.label_post_time_2.setText(text)
        self.label_text_2.setText(text)
        self.label_nickname_2.setText(text)
        self.label_author_id_2.setText(text)
        self.label_pic_num_2.setText(text)

    # 向文本输出框打印
    def printf(self, text):
        self.textBrowser_print.append(text)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser_print.textCursor()
        self.textBrowser_print.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    # 匹配粘贴的url地址
    # 解析抖音分享口令中的地址并返回列表
    def find(self, string):
        # r_string = re.sub(r"\n", "", string)
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url

    # 替换不能用于文件名的字符
    # 文件二次命名 命名方式为 文案+作者id
    def clean_filename(self, string):
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'   # re.sub(r'[\\/:*?"<>|\r\n]
        new_title = re.sub(rstr, " ", string)  # 替换为空格
        filename = new_title
        return filename

    # 判断是否已经下载过
    def check_info(self, check_filename, music_filename):
        try:
            if self.music_arg == 'no':
                already_exists = os.listdir(self.pic_dir)
                if check_filename in already_exists:
                    print('[  提示  ]:', check_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                    for i in range(20):
                        print(">", end='', flush=True)
                        time.sleep(0.01)
                    print('\r')
                    self.jump = "yes"
                else:
                    self.jump = "no"
            else:
                already_exists = os.listdir(self.pic_dir)
                music_already_exists = os.listdir(self.music_dir)
                # print(music_filename)
                new_music_filename = re.findall(re.compile(r'_([^_]*).mp3'), music_filename)
                # print(new_music_filename)
                if new_music_filename[0] == '音频获取错误，无法下载，为您跳过！！！':
                    if check_filename in already_exists:
                        print('[  提示  ]:', check_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                        for i in range(20):
                            print(">", end='', flush=True)
                            time.sleep(0.01)
                        print('\r')
                        self.jump = "yes"
                    else:
                        self.jump = "no"
                else:
                    if check_filename in already_exists and music_filename in music_already_exists:
                        print('[  提示  ]:', check_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                        for i in range(20):
                            print(">", end='', flush=True)
                            time.sleep(0.01)
                        print('\r')
                        print('[  提示  ]:', music_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                        for i in range(20):
                            print(">", end='', flush=True)
                            time.sleep(0.01)
                        print('\r')
                        self.jump = "yes"
                    else:
                        self.jump = "no"
            return self.jump
        except Exception as e:
            print(e)
            value = "self.jump:" + self.jump
            self.error_do(e, 'check_info', value)

    # 将错误记录在logs.txt中
    def error_do(self, e, func_name, value=''):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(date + ":\n" + func_name + ': ' + str(e) + '\n' + "Input value: " + value + '\n' * 2)

    # 保存解析历史记录和作品信息
    def wirte_history(self, image_info):
        try:
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            with open('history.txt', 'a', encoding='utf-8') as f:
                f.write(
                    date + '\n' + '下载类型：\t' + image_info[7] + '\n' + '图片链接:\t' + image_info[
                        8] + '\n' + '作品信息\t' + '\n' + '发布时间：\t' + image_info[6] + '\n'
                    + '文        案：\t' + image_info[0] + '\n' + '作者昵称：\t' + image_info[2] + '\n' + '作者  ID：\t' +
                    image_info[
                        3] + '\n'
                    + '图片数量：\t' + '%d张' % image_info[9] + '\n' + '背景音乐：\t' + image_info[5] + '\n' * 2)
        except Exception as e:
            # self.printf(e)
            self.error_do(e, 'wirte_history', image_info)

    def conversion(self):
        try:
            self.printf('[  提示  ]:转码中......')
            print('[  提示  ]:转码中......')
            img_list = os.listdir(self.pic_dir)
            new_img_list = []
            for m in img_list:
                m_temp = os.path.splitext(m)
                if m_temp[1] != '.png':
                    new_img_list.append(m)
            time.sleep(0.01)
            a = 0
            self.progressBar_conversion.reset()
            for filename in new_img_list:
                a = a + 1
                print(a)
                c = a * 100 / len(new_img_list)
                print(c)
                self.progressBar_conversion.setValue(c)
                info = os.path.splitext(filename)
                if info[1] != '.png':
                    png = img.open(self.pic_dir + filename)
                    png.save(self.pic_dir + info[0] + ".png")
                time.sleep(0.01)
                if info[1] == '.webp':
                    path = self.pic_dir + "\\" + filename
                    os.remove(path)

            print('[  提示  ]:转码完成！')
            self.printf('[  提示  ]:转码完成！')
        except Exception as e:
            print(e)
            value = img_list + '\n' + new_img_list
            self.error_do(e, 'conversion', value)

    # 处理url
    def judge_link(self):
        try:
            url_list = self.find(self.pic_url)
            total_urls = len(url_list)
            self.printf('[  提示  ]:本次共有%d个链接\r' % total_urls)
            print('[  提示  ]:本次共有%d个链接\r' % total_urls)
            for counts in range(len(url_list)):
                count = counts + 1
                time.sleep(0.3)
                print('\n' + '>' * 120)
                print('-' * 120)
                print('当前为%d个链接\r' % count)
                self.printf('\n' + '>' * 120)
                self.printf('-' * 120)
                self.printf('当前为%d个链接\r' % count)
                print_out = '本次共有%d个链接\r' % total_urls + '当前为%d个链接\r' % count
                self.label_header.setText(print_out)
                self.get_info(url_list[counts])
                if self.jump == "yes":
                    continue
                # 存入记录
                self.wirte_history(self.image_info)
                time.sleep(0.01)
                self.conversion()
        except Exception as e:
            self.error_do(e, 'judge_link', url_list)

    # 获取图片信息
    def get_info(self, original_url):
        image_type = "图片"
        try:
            r = requests.get(url=original_url, allow_redirects=False)
            try:
                long_url = r.headers['Location']
            except:
                long_url = original_url
            key = re.findall('video/(\d+)?', long_url)[0]
            api_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'
            print("当前key为:" + key)
            print("api地址为:" + api_url)
            print('-' * 120)
            self.printf("当前key为:" + key)
            self.printf("api地址为:" + api_url)
            self.printf('-' * 120)
            js = json.loads(requests.get(url=api_url, headers=self.headers).text)

            try:
                image_data = js['item_list'][0]['images']
                # 图集背景音频
                try:
                    image_music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
                    image_music_title = str(js['item_list'][0]['music']['title'])
                except:
                    image_music_url = ''
                    image_music_title = "音频获取错误，无法下载，为您跳过！！！"
                    print('\r[  警告  ]:下载音频出错!\r')
                    self.printf('\r[  警告  ]:下载音频出错!\r')
                # 创建时间
                image_creat_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(js['item_list'][0]['create_time']))
                # 图集标题
                title = str(js['item_list'][0]['desc'])
                # 第一次处理名称
                if '#……版本过低，升级后可展示全部信息' in title:
                    image_title = title.replace('#……版本过低，升级后可展示全部信息', '', 1)
                else:
                    image_title = title
                new_image_title = ''.join(image_title.splitlines())
                if len(new_image_title) > 182:
                    self.printf("[  提示  ]:" + "文件名称太长 进行截取")
                    new_image_title = new_image_title[0:180]
                    self.printf("[  提示  ]:" + "截取后的文案：" + new_image_title + '长度为：%d\r' % len(new_image_title))
                # 图集作者昵称
                image_author = str(js['item_list'][0]['author']['nickname'])
                # 图集作者抖音号
                image_author_id = str(js['item_list'][0]['author']['unique_id'])
                if image_author_id == "":
                    # 如果作者未修改过抖音号，应使用此值以避免无法获取其抖音ID
                    image_author_id = str(js['item_list'][0]['author']['short_id'])
                # 去水印图集链接
                images_url = []
                for data in image_data:
                    images_url.append(data['url_list'][0])
                # 图片数量
                image_num = len(images_url)

                self.image_info = [new_image_title, images_url, image_author, image_author_id, image_music_url,
                                   image_music_title, image_creat_time, image_type, original_url, image_num]

                # 输出具体信息
                print("作品信息")
                print("文案：" + image_title)
                print("发布时间：" + image_creat_time)
                print("作者昵称：" + image_author)
                print("作者id：" + image_author_id)
                print('图片数量：%d张\r' % image_num)
                print("背景音乐：" + image_music_title)
                print('-' * 120)
                self.printf("作品信息")
                self.printf("文案：" + image_title)
                self.printf("发布时间：" + image_creat_time)
                self.printf("作者昵称：" + image_author)
                self.printf("作者id：" + image_author_id)
                self.printf('图片数量：%d张\r' % image_num)
                self.printf("背景音乐：" + image_music_title)
                self.printf('-' * 120)
                self.label_text_2.setText(image_title)
                self.label_post_time_2.setText(image_creat_time)
                self.label_nickname_2.setText(image_author)
                self.label_author_id_2.setText(image_author_id)
                self.label_pic_num_2.setText('%d张\r' % image_num)
                self.label_muisc_2.setText(image_music_title)

                for i in range(len(images_url)):
                    a = i + 1
                    self.image_filename = self.clean_filename(new_image_title) + '%s' % a + '.webp'
                    self.check_filename = self.clean_filename(new_image_title) + '%s' % a + '.png'
                    self.music_filename = self.clean_filename(new_image_title) + '_' + image_music_title + '.mp3'
                    self.pic_dir = self.save + "\\" + self.pic_save
                    self.music_dir = self.save + "\\" + self.music_save

                    if not os.path.exists(self.pic_dir):
                        os.makedirs(self.pic_dir)
                    if self.music_arg == 'yes':
                        if not os.path.exists(self.music_dir):
                            os.makedirs(self.music_dir)
                    else:
                        pass

                    self.check_info(self.check_filename, self.music_filename)
                    if self.jump == "yes":
                        continue
                    self.image_download(self.image_info, i)
                if self.music_arg == 'yes':
                    self.music_download(self.image_info)
                else:
                    pass

                return self, self.image_info
            except:
                self.printf("当前链接有误，请确认后再解析！")
        except Exception as e:
            value = "当前key为:" + key + '\n' + js + '\n' + self.image_info
            self.error_do(e, 'get_info', value)

    # 视频下载
    def image_download(self, image_info, i):
        image = requests.get((image_info[1])[i], headers=self.headers)  # 保存视频
        start = time.time()  # 下载开始时间
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(image.headers['content-length'])  # 下载文件总大小
        try:
            if image.status_code == 200:  # 判断是否响应成功
                print('[  图片  ]:' + self.image_filename + '[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                self.printf('[  图片  ]:' + image_info[0])
                self.printf('[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))

                v_url = self.pic_dir + "\\" + self.image_filename

                with open(v_url, 'wb') as file:  # 显示进度条
                    self.progressBar_download.reset()
                    for data in image.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                            '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                        a = size / content_size * 100
                        self.progressBar_download.setValue(a)
                    end = time.time()  # 下载结束时间
                    print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                            end - start))  # 输出下载用时时间
        except Exception as error:
            # print(error)
            print('[  警告  ]:视频下载出错!')
            self.printf('[  警告  ]:视频下载出错!')

    def music_download(self, image_info):
        music = requests.get(image_info[4])  # 保存音频
        start = time.time()  # 下载开始时间
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(music.headers['content-length'])  # 下载文件总大小
        try:
            if music.status_code == 200:  # 判断是否响应成功
                print('[  音频  ]:' + image_info[5] + '[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                self.printf('[  音频  ]:' + image_info[5])
                self.printf('[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))

                m_url = self.music_dir + "\\" + self.music_filename

                with open(m_url, 'wb') as file:  # 显示进度条
                    self.progressBar_download.reset()
                    for data in music.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                            '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                        a = size / content_size * 100
                        self.progressBar_download.setValue(a)
                    end = time.time()  # 下载结束时间
                    print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                            end - start))  # 输出下载用时时间
        except:
            print('\r[  警告  ]:下载音频出错!\r')
            self.printf('\r[  警告  ]:下载音频出错!\r')


class TwoForm(QWidget, Ui_video_download_page):
    def __init__(self):
        super(TwoForm, self).__init__()
        # 初始化变量
        self.start()
        # 启动界面
        self.setupUi(self)
        self.Explain()

    # 按钮互斥
    def checkBox_choice(self, cbx_1, cbx_2):
        if cbx_1.isChecked() == True:
            cbx_2.setChecked(False)

    # 槽函数 clear 清空
    def clear(self):
        text = ''
        self.progressBar_download.reset()
        self.plainTextEdit.clear()
        self.label_header.setText("当前暂无链接")
        self.label_post_time_2.setText(text)
        self.label_text_2.setText(text)
        self.label_nickname_2.setText(text)
        self.label_author_id_2.setText(text)
        self.label_muisc_2.setText(text)

    def start(self):
        # 定义全局变量
        self.music_dir = ''
        self.video_dir = ''
        self.music_filename = ''
        self.video_filename = ''
        self.jump = ''
        self.video_info = ''
        self.url_list = ''  # 链接列表
        self.download_mode = ''
        self.music_arg = ''
        self.uid = ''  # 用户主页
        self.mode = ''  # 下载模式

        self.sec = ''  # 用户唯一标识
        self.save = ''  # 保存路径
        self.video_save = ''
        self.dir = ''
        self.url = ''
        self.info_list = ''  # 视频信息列表
        self.nickname = ''  # 保存用户名
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }
        self.Isend = False  # 抓获所有视频
        self.count = 35  # 单页下载数
        self.musicarg = ''  # 下载音频
        self.like_counts = 0  # 点赞个数
        self.i_num = 0
        self.v_num = 0

    def choice(self, a):
        if self.checkBox_post.isChecked():
            self.mode = 'post'
        else:
            self.mode = 'like'
        if self.checkBox_bgm.isChecked():
            self.music_arg = 'yes'
        else:
            self.music_arg = 'no'
        if self.radioButton_many.isChecked():
            self.download_mode = 'many'
        else:
            self.download_mode = 'single'

        if self.download_mode == 'many' and self.mode == 'post':
            if self.music_arg == 'yes':
                self.label_mode_2.setText(a + "批量下载-POST-背景音乐")
            else:
                self.label_mode_2.setText(a + "批量下载-POST")

        elif self.download_mode == 'many' and self.mode == 'like':
            if self.music_arg == 'yes':
                self.label_mode_2.setText(a + "批量下载-LIKE-背景音乐")
            else:
                self.label_mode_2.setText(a + "批量下载-LIKE")

        elif self.download_mode == 'single' and self.music_arg == 'yes':
            self.label_mode_2.setText(a + "单个下载-背景音乐")
        else:
            self.label_mode_2.setText(a + "单个下载")

    # 槽函数 run 运行
    def run(self):
        # 实例化读取配置文件
        self.cf = configparser.RawConfigParser()
        # 用utf-8防止出错
        self.cf.read("conf.ini", encoding="utf-8")
        # 读取部分配置文件
        self.save = self.cf.get("save", "save")
        self.video_save = self.cf.get("video_save", "video_dir")
        self.music_save = self.cf.get("music_save", "music_dir")
        self.pic_save = self.cf.get("pic_save", "pic_dir")

        self.Isend = False  # 抓获所有视频

        if self.checkBox_ini.isChecked():
            a = "配置文件-"
            self.choice(a)
            print('[  提示  ]:将使用配置文件进行批量下载,请确认配置信息准确！！！\r')
            self.printf('[  提示  ]:将使用配置文件进行批量下载,请确认配置信息准确！！！\r')
            # 从配置文件读取链接
            self.uid = self.cf.get("uid", "video_url")
            self.plainTextEdit.setPlainText(self.uid)
            if self.find(self.uid) == '':
                print('[  警告  ]:当前配置文件无链接!\r')
                self.printf('[  警告  ]:当前配置文件无链接!\r')
            else:
                print('[  提示  ]:读取本地配置完成!\r')
                self.printf('[  提示  ]:读取本地配置完成!\r')
                self.judge_link()
        else:
            a = ""
            self.choice(a)
            self.uid = self.plainTextEdit.toPlainText()
            if self.find(self.uid) == '':
                print('[  警告  ]:当前无链接!\r')
                self.printf('[  警告  ]:当前无链接!\r')
            else:
                print('[  提示  ]:开始下载!\r')
                self.printf('[  提示  ]:开始下载!\r')
                self.judge_link()

    # 向文本输出框打印
    def printf(self, text):
        self.textBrowser_print.append(text)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser_print.textCursor()
        self.textBrowser_print.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    # 说明文件
    def Explain(self):
        self.printf("#" * 120)
        self.printf(
            """
                使用说明：
                        1、解析前请先选择下载模式
                        2、单个视频下载可以同时粘贴多个链接

                注意：  单个视频链接与用户主页链接要分清
            """
        )
        self.printf("#" * 120)
        self.printf('\r')

    # 将错误记录在logs.txt中
    def error_do(self, e, func_name, value=''):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(date + ":\n" + func_name + ': ' + str(e) + '\n' + "Input value: " + value + '\n' * 2)

    # 匹配粘贴的url地址
    def find(self, string):
        # findall() 查找匹配正则表达式的字符串
        # r_string = re.sub(r"\n", "", string)
        url = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url

    # out
    def out_print(self, info):
        # 输出具体信息
        self.printf('-' * 120)
        self.printf("作品信息")
        self.printf("发布时间：" + info[6])
        self.printf("文   案：" + info[0])
        self.printf("作者昵称：" + info[2])
        self.printf("作者 id：" + info[3])
        self.printf('背景音乐' + info[5])
        self.label_post_time_2.setText(info[6])
        self.label_text_2.setText(info[0])
        self.label_nickname_2.setText(info[2])
        self.label_author_id_2.setText(info[3])
        self.label_muisc_2.setText(info[5])

    def conversion(self):
        try:
            self.printf('[  提示  ]:转码中......')
            print('[  提示  ]:转码中......')
            img_list = os.listdir(self.pic_dir)
            new_img_list = []
            for m in img_list:
                m_temp = os.path.splitext(m)
                if m_temp[1] != '.png':
                    new_img_list.append(m)
            time.sleep(0.01)
            for n, filename in tqdm(enumerate(new_img_list), total=len(new_img_list)):
                info = os.path.splitext(filename)
                if info[1] != '.png':
                    png = img.open(self.pic_dir + filename)
                    png.save(self.pic_dir + info[0] + ".png")
                time.sleep(0.01)
                if info[1] == '.webp':
                    path = self.pic_dir + "\\" + filename
                    os.remove(path)

            print('[  提示  ]:转码完成！')
            self.printf('[  提示  ]:转码完成！')
        except Exception as e:
            print(e)
            value = img_list[1] + '\n' + new_img_list[1]
            self.error_do(e, 'conversion', value)

    # 替换不能用于文件名的字符
    # 文件二次命名 命名方式为 文案+作者id
    def clean_filename(self, string):
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'   # re.sub(r'[\\/:*?"<>|\r\n]
        new_title = re.sub(rstr, " ", string)  # 替换为空格
        return new_title

    # 判断是否已经下载过
    def check_info(self, video_filename, music_filename, video_dir):
        try:
            if self.music_arg == 'no':
                already_exists = os.listdir(video_dir)
                if video_filename in already_exists:
                    print('[  提示  ]:', video_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                    for i in range(20):
                        print(">", end='', flush=True)
                        time.sleep(0.01)
                    print('\r')
                    self.jump = "yes"
                else:
                    self.jump = "no"
            else:
                already_exists = os.listdir(video_dir)
                music_already_exists = os.listdir(self.music_dir)
                new_music_filename = re.findall(re.compile(r'_([^_]*).mp3'), music_filename)
                if new_music_filename[0] == '音频获取错误，无法下载，为您跳过！！！':
                    if video_filename in already_exists:
                        print('[  提示  ]:', video_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                        for i in range(20):
                            print(">", end='', flush=True)
                            time.sleep(0.01)
                        print('\r')
                        self.jump = "yes"
                    else:
                        self.jump = "no"
                else:
                    if video_filename in already_exists and music_filename in music_already_exists:
                        print('[  提示  ]:', video_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                        for i in range(20):
                            print(">", end='', flush=True)
                            time.sleep(0.01)
                        print('\r')
                        print('[  提示  ]:', music_filename, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                        for i in range(20):
                            print(">", end='', flush=True)
                            time.sleep(0.01)
                        print('\r')
                        self.jump = "yes"
                    else:
                        self.jump = "no"
            return self.jump
        except Exception as e:
            print(e)
            value = already_exists + "self.jump:" + self.jump
            self.error_do(e, 'check_info', value)

    # 保存解析历史记录和作品信息
    def wirte_history(self, video_info):
        try:
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            with open('history.txt', 'a', encoding='utf-8') as f:
                f.write(
                    date + '\n' + '下载类型：\t' + video_info[7] + '\n' + '视频（主页）链接:\t' + video_info[
                        8] + '\n' + '作品信息\t' + '\n' + '发布时间：\t' + video_info[6] + '\n'
                    + '文        案：\t' + video_info[0] + '\n' + '作者昵称：\t' + video_info[2] + '\n' + '作者  ID：\t' +
                    video_info[
                        3] + '\n' + '背景音乐：\t' + video_info[5] + '\n' * 2)
        except Exception as e:
            print(e)
            self.error_do(e, 'wirte_history', video_info)

    def request_info(self, api_post_url):
        response = requests.get(
            url=api_post_url, headers=self.headers)
        html = json.loads(response.content.decode())
        return html

    def judge_link(self):
        try:
            self.url_list = self.find(self.uid)
            total_urls = len(self.url_list)
            print('[  提示  ]:本次共有%d个链接\r' % total_urls)
            self.printf('[  提示  ]:本次共有%d个链接\r' % total_urls)
            for counts in range(len(self.url_list)):
                count = counts + 1
                print('>' * 120)
                print('-' * 120)
                print('当前为%d个链接\r' % count)
                self.printf('\n' + '>' * 120)
                self.printf('-' * 120)
                self.printf('当前为%d个链接\r' % count)
                self.label_header.setText('本次共有%d个链接' % total_urls + '当前为%d个链接\r' % count)
                if self.download_mode == 'many':
                    self.Isend = False  # 抓获所有视频
                    self.first_get_date(counts)
                else:
                    self.one_video_get_date(counts)
                    if self.jump == "yes":
                        continue
                    self.videos_download(self.video_info)
                    self.wirte_history(self.video_info)
                    if self.music_arg == 'no':
                        continue
                    self.music_download(self.video_info)
        except Exception as e:
            print(e)
            self.error_do(e, 'judge_link', self.url_list)

    def one_video_get_date(self, counts):
        try:
            video_type = "单个视频"
            r = requests.get(url=self.url_list[counts], allow_redirects=False)
            long_url = r.headers['Location']
            key = re.findall('video/(\d+)?', long_url)[0]
            api_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'
            js = json.loads(requests.get(url=api_url, headers=self.headers).text)
            # 去水印后视频链接(2022年1月1日抖音APi获取到的URL会进行跳转，需要在Location中获取直链)
            video_url = str(js['item_list'][0]['video']['play_addr']['url_list'][0]).replace('playwm', 'play')
            # 视频标题
            title = str(js['item_list'][0]['desc'])
            video_title = ''.join(title.splitlines())
            if len(video_title) > 182:
                print("[  提示  ]:", "文件名称太长 进行截取")
                self.printf("[  提示  ]:" + "文件名称太长 进行截取")
                video_title = video_title[0:180]
                print("[  提示  ]:", "截取后的文案：" + video_title + '长度为：%d\r' % len(video_title))
                self.printf("[  提示  ]:" + "截取后的文案：" + video_title + '长度为：%d\r' % len(video_title))
            # 发布时间
            creat_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(js['item_list'][0]['create_time']))
            # 视频作者昵称
            video_author = str(js['item_list'][0]['author']['nickname'])
            # 视频作者抖音号
            video_author_id = str(js['item_list'][0]['author']['unique_id'])
            if video_author_id == "":
                # 如果作者未修改过抖音号，应使用此值以避免无法获取其抖音ID
                video_author_id = str(js['item_list'][0]['author']['short_id'])
            # 音乐链接
            music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
            # 音乐名称
            music_title = str(js['item_list'][0]['music']['title'])

            self.video_info = [video_title, video_url, video_author, video_author_id, music_url, music_title,
                               creat_time, video_type, self.url_list[counts]]

            # 输出具体信息
            self.printf("作品信息")
            self.printf("发布时间：" + self.video_info[6])
            self.printf("文案：" + self.video_info[0])
            self.printf("作者昵称：" + self.video_info[2])
            self.printf("作者id：" + self.video_info[3])
            self.printf('背景音乐' + self.video_info[5])
            self.printf('-' * 120)
            self.label_post_time_2.setText(self.video_info[6])
            self.label_text_2.setText(self.video_info[0])
            self.label_nickname_2.setText(self.video_info[2])
            self.label_author_id_2.setText(self.video_info[3])
            self.label_muisc_2.setText(self.video_info[5])

            self.video_save = "单个下载"
            self.video_filename = creat_time + self.clean_filename(video_title) + '.mp4'
            self.music_filename = self.clean_filename(video_title) + '_' + music_title + '.mp3'
            self.video_dir = self.save + "\\" + self.video_save
            self.music_dir = self.video_dir

            if not os.path.exists(self.video_dir):
                os.makedirs(self.video_dir)
            if not os.path.exists(self.music_dir):
                os.makedirs(self.music_dir)

            self.check_info(self.video_filename, self.music_filename, self.video_dir)
            print(self.jump)
        except Exception as e:
            print(e)
            value = 'key:' + key + '\n' + js + '\n' + (self.video_info[1])[1] + (self.video_info[2])[1]
            self.error_do(e, 'one_video_get_date', value)

    def first_get_date(self, counts):
        try:
            self.url = self.url_list[counts]
            r = requests.get(url=self.url)
            # 获取用户sec_uid
            for one in re.finditer(r'user\/([\d\D]*)', str(r.url)):
                self.sec = one.group(1)
            print('[  提示  ]:用户的sec_id=%s\r' % self.sec)
            self.printf('[  提示  ]:用户的sec_id=%s\r' % self.sec)

            # 第一次访问页码
            max_cursor = 0
            # 构造第一次访问链接
            api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=PDHVOQAAXMfFyj02QEpGaDwx1S&dytk=' % (
                self.mode, self.sec, str(self.count), max_cursor)
            html = self.request_info(api_post_url)

            # 处理用户名
            if self.mode == 'post':
                self.nickname = html['aweme_list'][0]['author']['nickname']
            else:
                self.nickname = "栋栋"

            # 尝试次数
            index = 0
            # 存储api数据
            result = []
            while result == []:
                index += 1
                print('----正在进行第 %d 次尝试----\r' % index)
                self.printf('----正在进行第 %d 次尝试----\r' % index)
                time.sleep(0.3)
                html = self.request_info(api_post_url)
                if self.Isend == False:
                    print('[  用户  ]:', str(self.nickname), '\r')
                    self.printf('[  用户  ]:' + str(self.nickname) + '\n')
                    max_cursor = html['max_cursor']
                    result = html['aweme_list']
                    print('----抓获数据成功!----\r')
                    self.printf('----抓获数据成功!----\r')

                    # 处理第一页视频信息
                    self.get_video_info(result, max_cursor)
                else:
                    max_cursor = html['max_cursor']
                    self.next_data(max_cursor)
                    print('----此页无数据，为您跳过----\r')
                    self.printf('----此页无数据，为您跳过----\r')
            return max_cursor, result, self.sec
        except Exception as e:
            print(e)
            value = self.url
            self.error_do(e, 'first_get_date', value)

    # 下一页
    def next_data(self, max_cursor):
        try:
            # 尝试次数
            index = 0
            # 存储api数据
            result = []
            # 获取解码后原地址
            r = requests.get(url=self.url, allow_redirects=False)
            # 获取用户sec_uid
            if self.uid[0:20] == 'https://v.douyin.com':
                for one in re.finditer(r'user/([\d\D]*?)\?', str(r.url)):
                    self.sec = one.group(1)
            else:
                for one in re.finditer(r'user\/([\d\D]*)', str(r.url)):
                    self.sec = one.group(1)

            # 构造下一次访问链接
            api_next_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (
                self.mode, self.sec, str(self.count), max_cursor)

            while self.Isend == False:
                # 回到首页，则结束
                if max_cursor == 0:
                    self.Isend = True

                index += 1
                print('----正在对', max_cursor, '页进行第 %d 次尝试！----\r' % index)
                time.sleep(0.3)
                html = self.request_info(api_next_post_url)

                if self.Isend == False:
                    # 下一页值
                    max_cursor = html['max_cursor']
                    result = html['aweme_list']
                    print('----%d页抓获数据成功!----\r' % max_cursor)
                    self.printf('----%d页抓获数据成功!----\r' % max_cursor)
                    # 处理下一页视频信息
                    self.get_video_info(result, max_cursor)
                elif self.Isend == True:
                    print("全部下载完成")
                    self.printf("全部下载完成")
                else:
                    print('----%d页抓获数据失败!----\r' % max_cursor)
                    self.printf('----%d页抓获数据失败!----\r' % max_cursor)

        except Exception as e:
            print(e)
            value = '%d' % r.status_code + '\n' + html
            self.error_do(e, 'next_date', value)

    def get_video_info(self, result, max_cursor):
        try:
            name = "个人点赞"
            name_1 = "主页批量"
            author_list = []        # 作品文案信息
            video_list = []         # 无水印视频链接
            aweme_id = []           # 作品id
            nickname = []           # 作者名称
            new_video_list = []     # 视频列表
            dynamic_cover = []      # 封面大图
            judgment_list = []
            key_list = []

            uri_url = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&radio=1080p&line=0'

            for v in range(self.count):
                try:
                    judgment = str(result[v]['aweme_type'])
                    judgment_list.append(judgment)
                    # 对图片进行处理
                    if judgment == '2':
                        try:
                            key = str(result[v]['aweme_id'])
                            key_list.append(key)
                        except:
                            pass
                    # 对视频进行处理
                    elif judgment == '4':
                        try:
                            title = str(result[v]['desc'])
                            new_title = ''.join(title.splitlines())
                            if len(new_title) > 182:
                                print("[  提示  ]:", "文件名称太长 进行截取")
                                self.printf("[  提示  ]:" + "文件名称太长 进行截取")
                                new_title = new_title[0:180]
                                print("[  提示  ]:", "截取后的文案：" + new_title + '长度为：%d\r' % len(new_title))
                                self.printf("[  提示  ]:" + "截取后的文案：" + new_title + '长度为：%d\r' % len(new_title))
                            author_list.append(new_title)
                            video_list.append(str(result[v]['video']['play_addr']['url_list'][0]))
                            uri_list = (str(result[v]['video']['play_addr']['uri']))
                            # 生成1080p视频链接
                            new_video_list.append(uri_url % uri_list)
                            aweme_id.append(str(result[v]['aweme_id']))
                            nickname.append(str(result[v]['author']['nickname']))
                            # dynamic_cover.append(str(result[v]['video']['dynamic_cover']['url_list'][0]))
                        except:
                            print("a")
                            pass
                    else:
                        print("获取错误")
                        pass
                except:
                    pass

            for q in range(len(judgment_list)):
                judgment = judgment_list[q]
                # 点赞视频排序
                self.like_counts += 1
                print('当前为第%d个链接' % q)
                if q == 0:
                    self.i_num = 0
                    self.v_num = 0
                else:
                    pass

                if judgment == '2':
                    i = self.i_num
                    self.i_num += 1
                    images_url = []
                    video_type = "批量图片"

                    api_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key_list[i]}'
                    image_js = json.loads(requests.get(url=api_url, headers=self.headers).text)

                    # 去水印图集链接 # 将单个链接所有图片放入images_url
                    image_data = image_js['item_list'][0]['images']
                    for data in image_data:
                        images_url.append(data['url_list'][0])
                    # 图集标题
                    title = str(image_js['item_list'][0]['desc'])
                    # 第一次处理名称
                    if '#……版本过低，升级后可展示全部信息' in title:
                        image_title = title.replace('#……版本过低，升级后可展示全部信息', '', 1)
                    else:
                        image_title = title
                    new_image_title = ''.join(image_title.splitlines())
                    if len(new_image_title) > 182:
                        self.printf("[  提示  ]:" + "文件名称太长 进行截取")
                        new_image_title = new_image_title[0:180]
                        self.printf("[  提示  ]:" + "截取后的文案：" + new_image_title + '长度为：%d\r' % len(new_image_title))
                    # 图集作者昵称
                    image_author = str(image_js['item_list'][0]['author']['nickname'])
                    # 图集作者抖音号
                    image_author_id = str(image_js['item_list'][0]['author']['unique_id'])
                    if image_author_id == "":
                        # 如果作者未修改过抖音号，应使用此值以避免无法获取其抖音ID
                        image_author_id = str(image_js['item_list'][0]['author']['short_id'])

                    # 创建时间
                    image_creat_time = time.strftime("%Y-%m-%d %H.%M.%S",
                                                     time.localtime(image_js['item_list'][0]['create_time']))
                    # 图集背景音频
                    try:
                        image_music_url = str(image_js['item_list'][0]['music']['play_url']['url_list'][0])
                        image_music_title = str(image_js['item_list'][0]['music']['title'])
                    except:
                        image_music_url = ''
                        image_music_title = "音频获取错误，无法下载，为您跳过！！！"
                    # 图片数量
                    image_num = len(images_url)

                    image_info = [new_image_title, images_url, image_author, image_author_id, image_music_url,
                                  image_music_title, image_creat_time, video_type, self.url, image_num]

                    self.out_print(image_info)
                    print('图片数量：%d' % image_num)
                    for m in range(len(images_url)):
                        n = m + 1
                        self.image_filename = self.clean_filename(new_image_title) + '%s' % n + '.webp'
                        self.check_filename = self.clean_filename(new_image_title) + '%s' % n + '.png'
                        self.music_filename = self.clean_filename(new_image_title) + '_' + image_music_title + '.mp3'

                        if self.mode == 'post':
                            self.pic_dir = self.save + "\\" + name_1 + "\\" + image_author + "\\" + self.pic_save
                            self.music_dir = self.save + "\\" + name_1 + "\\" + image_author + "\\" + self.music_save
                        else:
                            self.pic_dir = self.save + "\\" + name + "\\" + self.pic_save
                            self.music_dir = self.save + "\\" + name + "\\" + self.music_save

                        if not os.path.exists(self.pic_dir):
                            os.makedirs(self.pic_dir)
                        if self.music_arg == 'yes':
                            if not os.path.exists(self.music_dir):
                                os.makedirs(self.music_dir)
                        else:
                            pass

                        self.check_info(self.check_filename, self.music_filename, self.pic_dir)
                        print(self.jump)
                        if self.jump == "yes":
                            continue
                        self.image_download(image_info, m)
                    if self.jump == "no":
                        self.conversion()
                        self.wirte_history(image_info)
                    if self.music_arg == 'yes':
                        if image_music_url != '':
                            self.music_download(image_info)
                        else:
                            print("音频下载出错")
                    else:
                        pass

                elif judgment == '4':
                    i = self.v_num
                    self.v_num += 1
                    video_type = "批量视频"
                    # 获取单部视频接口信息
                    jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={aweme_id[i]}'  # 官方接口
                    js = json.loads(requests.get(url=jx_url, headers=self.headers).text)
                    creat_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(js['item_list'][0]['create_time']))
                    try:
                        music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
                        music_title = str(js['item_list'][0]['music']['title'])
                    except:
                        music_url = ''
                        music_title = "音频获取错误，无法下载，为您跳过！！！"

                    video_info = [author_list[i], new_video_list[i], nickname[i], aweme_id[i], music_url, music_title,
                                  creat_time, video_type, self.url]

                    # 输出具体信息
                    self.out_print(video_info)
                    name = "栋栋"
                    self.video_filename = creat_time + self.clean_filename(author_list[i]) + '.mp4'
                    self.music_filename = self.clean_filename(author_list[i]) + '_' + music_title + '.mp3'
                    if self.mode == 'post':
                        self.video_dir = self.save + "\\" + name_1 + "\\" + nickname[i] + "\\" + self.video_save
                        self.music_dir = self.save + "\\" + name_1 + "\\" + nickname[i] + "\\" + self.music_save
                    else:
                        self.video_dir = self.save + "\\" + name + "\\" + self.video_save  # 栋栋\\download
                        self.music_dir = self.save + "\\" + name + "\\" + self.music_save

                    if not os.path.exists(self.video_dir):
                        os.makedirs(self.video_dir)
                    if self.music_arg == 'yes':
                        if not os.path.exists(self.music_dir):
                            os.makedirs(self.music_dir)
                    else:
                        pass

                    self.check_info(self.video_filename, self.music_filename, self.video_dir)
                    print(self.jump)
                    if self.jump == "yes":
                        continue
                    self.videos_download(video_info)
                    self.wirte_history(video_info)
                    if self.music_arg != 'yes':
                        continue
                    if music_url == '':
                        continue
                    self.music_download(video_info)

            # 获取下一页信息
            self.next_data(max_cursor)
        except Exception as e:
            print(e)

    # 视频下载
    def videos_download(self, video_info):
        video = requests.get(video_info[1], headers=self.headers)  # 保存视频
        start = time.time()  # 下载开始时间
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(video.headers['content-length'])  # 下载文件总大小
        try:
            if video.status_code == 200:  # 判断是否响应成功
                print('[  视频  ]:' + video_info[0] + '[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                self.printf('[  视频  ]:' + video_info[0])
                self.printf('[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))
                v_url = self.video_dir + "\\" + self.video_filename

                with open(v_url, 'wb') as file:  # 显示进度条
                    self.progressBar_download.reset()
                    for data in video.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                            '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                        a = size / content_size * 100
                        self.progressBar_download.setValue(a)
                    end = time.time()  # 下载结束时间
                    print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                            end - start))  # 输出下载用时时间
        except Exception as e:
            print('[  警告  ]:下载视频出错!')

    # 图片下载
    def image_download(self, image_info, m):
        image = requests.get((image_info[1])[m], headers=self.headers)  # 保存视频
        start = time.time()  # 下载开始时间
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(image.headers['content-length'])  # 下载文件总大小
        try:
            if image.status_code == 200:  # 判断是否响应成功
                print('[  图片  ]:' + self.image_filename + '[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                self.printf('[  图片  ]:' + image_info[0])
                self.printf('[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))

                v_url = self.pic_dir + "\\" + self.image_filename

                with open(v_url, 'wb') as file:  # 显示进度条
                    self.progressBar_download.reset()
                    for data in image.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                            '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                        a = size / content_size * 100
                        self.progressBar_download.setValue(a)
                    end = time.time()  # 下载结束时间
                    print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                            end - start))  # 输出下载用时时间
        except Exception as error:
            # print(error)
            print('[  警告  ]:图片下载出错!')
            self.printf('[  警告  ]:图片下载出错!')

    def music_download(self, video_info):
        music = requests.get(video_info[4])  # 保存音频
        start = time.time()  # 下载开始时间
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(music.headers['content-length'])  # 下载文件总大小
        try:
            if music.status_code == 200:  # 判断是否响应成功
                print('[  音频  ]:' + video_info[5] + '[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                self.printf('[  音频  ]:' + video_info[5])
                self.printf('[文件 大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))
                m_url = self.music_dir + "\\" + self.music_filename

                with open(m_url, 'wb') as file:  # 显示进度条
                    self.progressBar_download.reset()
                    for data in music.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                            '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                        a = size / content_size * 100
                        self.progressBar_download.setValue(a)
                    end = time.time()  # 下载结束时间
                    print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                            end - start))  # 输出下载用时时间
        except Exception as e:
            print(e)
            print('\r[  警告  ]:下载音频出错!\r')


class ThreeForm(QWidget, Ui_history_page):
    def __init__(self):
        super(ThreeForm, self).__init__()
        self.setupUi(self)

        font = QtGui.QFont()
        font.setFamily("【慧心】奶酪体")
        font.setPointSize(124)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: #FFFFF3;\n"
                                       "color: rgb(16, 16, 16);\n"
                                       "border-radius: 5px; \n"
                                       "font: 12pt \"【慧心】奶酪体\";")

        try:
            f = open('history.txt', encoding='utf-8')
            data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
            f.close()  # 关
            for a in data:
                self.printf(a)
        except:
            self.printf("暂无历史记录")

    def printf(self, text):
        self.textBrowser.append(text)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def refresh(self):
        try:
            f = open('history.txt', encoding='utf-8')
            data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
            f.close()  # 关
            for a in data:
                self.printf(a)
                time.sleep(0.1)
        except:
            self.printf("暂无历史记录")


class FourForm(QWidget, Ui_setting_page):
    def __init__(self):
        super(FourForm, self).__init__()
        self.setupUi(self)

        # 实例化读取配置文件
        self.cf = configparser.RawConfigParser()
        # 用utf-8防止出错
        self.cf.read("conf.ini", encoding="utf-8")
        # 将读取的数据写入
        self.save = self.cf.get("save", "save")
        self.pic_save = self.cf.get("pic_save", "pic_dir")
        self.music_save = self.cf.get("music_save", "music_dir")
        self.video_save = self.cf.get("video_save", "video_dir")

        self.lineEdit_save.setText(self.save)
        self.lineEdit_picture.setText(self.pic_save)
        self.lineEdit_music.setText(self.music_save)
        self.lineEdit_video.setText(self.video_save)

    def confirm(self):
        # 实例化读取配置文件
        cf = configparser.RawConfigParser()
        # 用utf-8防止出错
        cf.read("conf.ini", encoding="utf-8")
        save = self.lineEdit_save.text()
        pic_save = self.lineEdit_picture.text()
        music_save = self.lineEdit_music.text()
        video_save = self.lineEdit_video.text()
        if self.save != save:
            cf.set("save", "save", save)
        if self.pic_save != pic_save:
            cf.set("pic_save", "pic_dir", pic_save)
        if self.music_save != music_save:
            cf.set("music_save", "music_dir", music_save)
        if self.video_save != video_save:
            cf.set("video_save", "video_dir", video_save)
        cf.write(open("conf.ini", "w", encoding='utf-8'))

    def recover(self):
        self.lineEdit_save.setText(self.save)
        self.lineEdit_picture.setText(self.pic_save)
        self.lineEdit_music.setText(self.music_save)
        self.lineEdit_video.setText(self.video_save)
        self.cf.set("save", "save", self.save)
        self.cf.set("pic_save", "pic_dir", self.pic_save)
        self.cf.set("music_save", "music_dir", self.music_save)
        self.cf.set("video_save", "video_dir", self.video_save)
        self.cf.write(open("conf.ini", "w", encoding='utf-8'))