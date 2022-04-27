#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TukuDownload.py
@Date       :2022/04/05 20:23:37
@Author     :Dongdong
@version    :1.1.3
@License    :(C)Copyright 2021-2022
@Mail       :2638415826@qq.com
'''

import argparse
import configparser
import json
import os
import re
import requests
import sys
import time
from PIL import Image as img
from tqdm import tqdm

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
                                        TuKuDownload V1.1.3
                    使用说明：
                            1、运行软件前先打开目录下 conf.ini 文件按照要求进行配置
            """
        )
        print("#" * 120)
        print('\r')

        # 保存路径
        self.save = ''
        # 图片地址
        self.picurl = ''
        # 判断是否跳过
        self.jump = ''
        # 记录图片信息
        self.image_info = ''

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
                    'https://raw.githubusercontent.com/Dongdong0112/PicDownload/main/conf.ini')  # 暂时用GitHub 可用Gitee
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
            # print('[  警告  ]:未检测到命令，将使用配置文件进行批量下载!')

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
    def cheak_info(self, cheak_file, img_info):
        try:
            if cheak_file in img_info:
                print('[  提示  ]:', cheak_file, '[文件已存在，为您跳过]', end="")  # 开始下载，显示下载文件大小
                for i in range(20):
                    print(">", end='', flush=True)
                    time.sleep(0.01)
                print('\r')
                self.jump = "yes"
                return self.jump
        except Exception as e:
            print(e)
            self.error_do(e, 'cheak_info', self.jump)
            pass

    # 将错误记录在logs.txt中
    def error_do(self, e, func_name, input_value=''):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(date + ":\n" + func_name + ': ' + str(e) + '\n' + "Input value: " + input_value + '\n' * 2)

    # 保存解析历史记录和作品信息
    def wirte_history(self, image_info):
        try:
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            with open('history.txt', 'a', encoding='utf-8') as f:
                f.write(
                    date + '\n' + '图片原链接:' + image_info[5] + '\n' + '作品信息\t' + '\n' + '发布时间：\t' + image_info[8] + '\n'
                    + '文案：\t' + image_info[2] + '\n' + '作者昵称：\t' + image_info[3] + '\n' + '作者id：\t' + image_info[4] + '\n'
                    + '图片数量：\t' + '%d张' % image_info[6] + '\n' * 2)
        except Exception as e:
            # print(e)
            self.error_do(e, 'wirte_history')

    '''
    # 对图片进行转换
    def conversion(self):
        img_list = os.listdir(self.save)
        for n, filename in tqdm(enumerate(img_list), total=len(img_list)):
            # print(filename)
            info = os.path.splitext(filename)
            if info[1] != '.png':
                png = img.open(self.save + filename)
                # temp = info[0].split('.')  # 在 ‘.’ 处分割字符串
                # png.save(self.save + temp[0] + ".png")  # 转换jpg格式就写 “.jpg”
                png.save(self.save + info[0] + ".png")
            time.sleep(0.1)
            if info[1] == '.webp':
                path = self.save + "\\" + filename
                os.remove(path)
            # time.sleep(0.1)
        print('[  提示  ]:转码完成！')
    '''
    def conversion(self):
        try:
            print('[  提示  ]:转码中......')
            img_list = os.listdir(self.save)
            new_img_list = []
            for m in img_list:
                m_temp = os.path.splitext(m)
                if m_temp[1] != '.png':
                    new_img_list.append(m)
            time.sleep(0.01)
            for n, filename in tqdm(enumerate(new_img_list), total=len(new_img_list)):
                # print(filename)
                info = os.path.splitext(filename)
                if info[1] != '.png':
                    png = img.open(self.save + filename)
                    # temp = info[0].split('.')  # 在 ‘.’ 处分割字符串
                    # png.save(self.save + temp[0] + ".png")  # 转换jpg格式就写 “.jpg”
                    png.save(self.save + info[0] + ".png")
                time.sleep(0.01)
                if info[1] == '.webp':
                    path = self.save + "\\" + filename
                    os.remove(path)
                # time.sleep(0.1)
            print('[  提示  ]:转码完成！')
        except Exception as e:
            self.error_do(e, 'conversion', img_list)


    # 处理url
    def judge_link(self):
        try:
            url_list = self.find(self.picurl)
            total_urls = len(url_list)
            print('[  提示  ]:本次共有%d个链接\r' % total_urls)
            for counts in range(len(url_list)):
                count = counts + 1
                time.sleep(0.3)
                print('\n' + '>' * 120)
                print('-' * 120)
                print('当前为%d个链接\r' % count)
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
            js = json.loads(requests.get(url=api_url, headers=self.headers).text)
            try:
                image_data = js['item_list'][0]['images']
                # 图集背景音频
                image_music = str(js['item_list'][0]['music']['play_url']['url_list'][0])
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
                    print("[  提示  ]:", "文件名称太长 进行截取")
                    new_image_title = new_image_title[0:180]
                    # print("[  提示  ]:", "截取后的文案：{0}，长度：{1}".format(new_image_title], len(new_image_title)))
                    print("[  提示  ]:", "截取后的文案：" + new_image_title + '长度为：%d\r' % len(new_image_title))
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
                image_info = [images_url, image_music, image_title, image_author, image_author_id, original_url, image_num,new_image_title,image_creat_time]
                self.image_info = image_info
                # 输出具体信息
                print("作品信息")
                print("文案：" + image_title)
                print("发布时间：" + image_creat_time)
                print("作者昵称：" + image_author)
                print("作者id：" + image_author_id)
                print('图片数量：%d张\r' % image_num)
                print('-' * 120)
                # print(image_music)
                self.image_download(image_info,images_url)
                return self, image_info, images_url, api_url
            except:
                # print(e)
                print("当前链接有误，请确认后再解析！")
        except Exception as e:
            self.error_do(e, 'get_info', original_url)

    def image_download(self, image_info, image_url):
        try:
            # 创建并检测下载目录是否存在
            try:
                os.makedirs(self.save)
            except:
                pass
            # 尝试下载图片
            img_info = os.listdir(self.save)
            for i in range(len(image_url)):
                a = i + 1
                filename = self.clean_filename(image_info[7]) + '%s' % a + '.webp'
                cheak_file = self.clean_filename(image_info[7]) + '%s' % a + '.png'
                self.cheak_info(cheak_file,img_info)
                # print(self.jump)
                if self.jump == "yes":
                    continue
                image = requests.get(image_url[i])
                start = time.time()  # 下载开始时间
                size = 0  # 初始化已下载大小
                chunk_size = 1024  # 每次下载的数据大小
                content_size = int(image.headers['content-length'])  # 下载文件总大小
                try:
                    if image.status_code == 200:  # 判断是否响应成功
                        # 文件命名是否带 创建时间
                        # print('[  图片  ]:' + image_info[8] + ' ' + image_info[2] + '%s'%a + '[文件 大小]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))  # 开始下载，显示下载文件大小
                        # img_url = self.save + "\\" filename
                        print('[  图片  ]:' + image_info[2] + '%s' % a + '[文件 大小]:{size:.2f} MB'.format(
                            size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                        img_url = self.save + "\\" + filename
                        with open(img_url, 'wb') as file:  # 显示进度条
                            for data in image.iter_content(chunk_size=chunk_size):
                                file.write(data)
                                size += len(data)
                                print('\r' + '[下载进度]:%s%.2f%%' % (
                                    '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                            end = time.time()  # 下载结束时间
                            print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                                    end - start))  # 输出下载用时时间
                except Exception as e:
                    print('----[  警告  ]:图片下载出错!')
                    print('----[  警告  ]:', e, '\r')
        except Exception as e:
            self.error_do(e, 'image_download', image_info)



if __name__ == "__main__":
    def get_args(picurl,dir):
        RTK = TuKu()
        RTK.setting(picurl,dir)
        input('[  完成  ]:已完成批量下载，输入任意键后退出:')
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