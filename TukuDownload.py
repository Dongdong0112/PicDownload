#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TukuDownload.py
@Date       :2022/04/01 20:23:37
@Author     :Dongdong
@version    :1.0
@License    :(C)Copyright 2021-2022
@Mail       :2638415826@qq.com
@WeChat     :ZhangHiDg
'''

import re, os, time, json, requests, configparser, sys, argparse,logging
# 2
from retrying import retry
from werkzeug.urls import url_quote
import unicodedata


class TuKu():
    # 初始化
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }
        # 打印说明
        # self.out_Print()
        print("#" * 120)
        print(
            """
                                        TuKuDownload V1.0
                    使用说明：
                            1、运行软件前先打开目录下 conf.ini 文件按照要求进行配置
            """
        )
        print("#" * 120)
        print('\r')

        # 保存路径       # 图片地址
        self.save = ''
        self.picurl = ''

        # 检测配置文件
        if os.path.isfile("conf.ini") == True:
            pass
        else:
            print('[  提示  ]:没有检测到配置文件，生成中!\r')
            try:
                self.cf = configparser.ConfigParser()
                # 往配置文件写入内容
                self.cf.add_section("url")
                self.cf.set("url", "picurl", "https://v.douyin.com/NCMK4Gw/")
                self.cf.add_section("save")
                self.cf.set("save", "address", ".\\PicDownload")
                with open("conf.ini", "a+") as f:
                    self.cf.write(f)
                print('[  提示  ]:生成成功!\r')
            except:
                input('[  提示  ]:生成失败,正在为您下载配置文件!\r')
                r = requests.get(
                    'https://raw.githubusercontent.com/Dongdong0112/PicDownload/main/conf.ini')  # 暂时用GitHub 应用Gitee
                with open("conf.ini", "a+") as conf:
                    conf.write(r.content)
                sys.exit()

        # 实例化读取配置文件
        self.cf = configparser.RawConfigParser()

        # 用utf-8防止出错
        self.cf.read("conf.ini", encoding="utf-8")

    # 后期修改 暂时不动
    def setting(self, picurl, dir):
        """
        @description  : 设置命令行参数
        ---------
        @param  : picurl 图片地址,dir 目录
        -------
        @Returns  : None
        -------
        """
        if picurl != None:
            if picurl == None:
                print('[  警告  ]:--user不能为空')
                pass
            else:
                self.picurl = picurl
                self.save = dir
                print('[  提示  ]:读取命令完成!\r')
                self.judge_link()
        # 没有接收到命令
        else:
            print('[  警告  ]:未检测到命令，将使用配置文件进行批量下载!')

            # 读取保存路径
            self.save = self.cf.get("save", "address")

            # 读取图片地址
            self.picurl = self.cf.get("url", "picurl")

            print('[  提示  ]:读取本地配置完成!\r')
            input('[  提示  ]:按回车启动：')
            print("-" * 120)
            self.judge_link()

    # 匹配粘贴的url地址
    # 解析抖音分享口令中的地址并返回列表
    def find(self, string):
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url

    # 替换不能用于文件名的字符
    # 文件二次命名 命名方式为 文案+作者id
    def clean_filename(self, string):
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'   # re.sub(r'[\\/:*?"<>|\r\n]
        new_title = re.sub(rstr, " ", string)  # 替换为空格
        filename = new_title
        return filename

    # 处理url
    def judge_link(self):
        try:
            url_list = self.find(self.picurl)
            total_urls = len(url_list)
            print('[  提示  ]:本次共有%d个链接\r' % total_urls)
            for counts in range(len(url_list)):
                count = 0
                count = counts + 1
                time.sleep(0.3)
                print('>' * 120)
                print('-' * 120)
                print('当前为%d个链接\r' % count)
                self.get_info(url_list[counts])
        except Exception as e:
            self.error_do(e, 'judge_link', url_list)

    # 将错误记录在logs.txt中
    def error_do(self,e,func_name,input_value=''):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('logs.txt', 'a') as f:
            f.write(date + ":\n" + func_name + ': ' + str(e) + '\n' + "Input value: " + input_value + '\n')

    # 获取图片信息
    def get_info(self, original_url):
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
            # response = requests.get(url=api_url, headers=self.headers)
            # js = json.loads(response.content.decode())
            # 作用同下 有问题再解决
            js = json.loads(requests.get(url=api_url, headers=self.headers).text)
            try:
                image_data = js['item_list'][0]['images']
                # 图集背景音频
                image_music = str(js['item_list'][0]['music']['play_url']['url_list'][0])
                # 图集标题
                image_title = str(js['item_list'][0]['desc'])
                # 第一次处理名称
                new_image_title = ''.join(image_title.splitlines())
                '''
                if len(new_image_title) > 182:
                    print("[  提示  ]:", "文件名称太长 进行截取")
                    new_image_title = image_title[0:180]
                    print("[  提示  ]:", "截取后的文案：{0}，长度：{1}".format(new_image_title], len(new_image_title)))
                '''
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
                image_info = [images_url, image_music, image_title, image_author, image_author_id, original_url, image_num,new_image_title]
                # 输出具体信息
                print("作品信息")
                print("文案：" + image_title)
                print("作者昵称：" + image_author)
                print("作者id：" + image_author_id)
                print('图片数量：%d张\r' % image_num)
                print('-' * 120)
                # print(image_music) 差作品时间
                self.image_download(image_info,images_url)
                return self, image_info, images_url, api_url
            except:
                print("当前链接非图片链接，请确认后再解析！")
        except Exception as e:
            self.error_do(e, 'get_info', original_url)

    def image_download(self,image_info,image_url):
        try:
            # 创建并检测下载目录是否存在
            try:
                os.makedirs(self.save)
            except:
                pass
            # 尝试下载图片
            for i in range(len(image_url)):
                try:
                    a = i + 1
                    image = requests.get(image_url[i])
                    start = time.time()                                  # 下载开始时间
                    size = 0                                             # 初始化已下载大小
                    chunk_size = 1024                                    # 每次下载的数据大小
                    content_size = int(image.headers['content-length'])  # 下载文件总大小
                    try:
                        if image.status_code == 200:  # 判断是否响应成功
                            print('[  图片  ]:' + image_info[2] + '%s'%a + '[文件 大小]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))  # 开始下载，显示下载文件大小
                            v_url = self.save + "\\" + self.clean_filename(image_info[7]) + '%s'%a + '.webp'
                            with open(v_url, 'wb') as file:  # 显示进度条
                                for data in image.iter_content(chunk_size=chunk_size):
                                    file.write(data)
                                    size += len(data)
                                    print('\r' + '[下载进度]:%s%.2f%%' % (
                                        '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                                end = time.time()  # 下载结束时间
                                print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                                        end - start))  # 输出下载用时时间
                    except Exception as e:
                        print(e)
                        print('----[  警告  ]:图片下载出错!')
                        print('----[  警告  ]:', e, '\r')

                except Exception as e :
                    pass
        except Exception as e:
            self.error_do(e, 'image_download')





if __name__ == "__main__":
    def get_args(picurl,dir):
        RTK = TuKu()
        RTK.setting(picurl,dir)
        sys.exit(0)
    try:
        parser = argparse.ArgumentParser(description='TikTokMulti V1.2.5 使用帮助')
        parser.add_argument('--picurl', '-u', type=str, help='为用户主页链接，非必要参数', required=False)
        parser.add_argument('--dir','-d', type=str,help='视频保存目录，非必要参数， 默认./Download', default='./Download/')
        args = parser.parse_args()
        # 获取命令行
        get_args(args.picurl, args.dir)
    except Exception as e:
        print(e)
        print('[  提示  ]:未输入命令，自动退出!')
        sys.exit(0)