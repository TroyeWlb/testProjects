#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from concurrent.futures import ThreadPoolExecutor, wait
from requests import get, head
import sys


class Downloader:
    def __init__(self, url, nums, file):
        self.url = url
        self.num = nums
        self.name = file
        self.getSize = 0
        self.info = {
            'main': {
                'progress': 0,
                'speed': ''
            },
            'sub': {
                'progress': [0 for i in range(nums)],
                'stat': [1 for i in range(nums)]
            }
        }
        r = head(self.url)
        # 若资源显示302,则迭代找寻源文件
        while r.status_code == 302:
            self.url = r.headers['Location']
            print("该url已重定向至{}".format(self.url))
            r = head(self.url)
        self.size = int(r.headers['Content-Length'])
        print('该文件大小为：{} bytes'.format(self.size))

    def down(self, start, end, thread_id, chunk_size=10240):
        raw_start = start
        for _ in range(10):
            try:
                headers = {'Range': 'bytes={}-{}'.format(start, end)}
                r = get(self.url, headers=headers, timeout=10, stream=True)
                print(f"线程{thread_id}连接成功")
                size = 0
                with open(self.name, "rb+") as fp:
                    fp.seek(start)
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            self.getSize += chunk_size
                            fp.write(chunk)
                            start += chunk_size
                            size += chunk_size
                            progress = round(size / (end - raw_start) * 100, 2)
                            self.info['sub']['progress'][thread_id - 1] = progress
                            self.info['sub']['stat'][thread_id - 1] = 1
                return
            except Exception as e:
                print(e)
                self.down(start, end, thread_id)
        print(f"{start}-{end}, 下载失败")
        self.info['sub']['stat'][thread_id - 1] = 0

    def show(self):
        while True:
            speed = self.getSize
            time.sleep(.5)
            speed = int((self.getSize - speed) * 2 / 1024)
            if speed > 1024:
                speed = f"{round(speed / 1024, 2)} M/s"
            else:
                speed = f"{speed} KB/s"
            progress = round(self.getSize / self.size * 100, 2)
            # print(f"\r文件下载进度：{progress}%，下载速度：{speed}", end='')
            self.info['main']['progress'] = progress
            self.info['main']['speed'] = speed
            print(self.info)
            if progress >= 100:
                break

    def run(self):
        # 创建一个和要下载文件一样大小的文件
        fp = open(self.name, "wb")
        print(f"正在初始化下载文件：{self.name}")
        fp.truncate(self.size)
        print(f"文件初始化完成")
        start_time = time.time()
        fp.close()
        part = self.size // self.num
        pool = ThreadPoolExecutor(max_workers=self.num + 1)
        futures = []
        for i in range(self.num):
            start = part * i
            if i == self.num - 1:
                end = self.size
            else:
                end = start + part - 1
            futures.append(pool.submit(self.down, start, end, i + 1))
        futures.append(pool.submit(self.show))
        print(f"正在使用{self.num}个线程进行下载...")
        wait(futures)
        end_time = time.time()
        speed = int(self.size / 1024 / (end_time - start_time))
        if speed > 1024:
            speed = f"{round(speed / 1024, 2)} M/s"
        else:
            speed = f"{speed} KB/s"
        print(f"{self.name} 下载完成，平均速度：{speed}")


if __name__ == '__main__':
    debug = 0
    if debug:
        url = 'http://mirrors.huaweicloud.com/centos/8.1.1911/isos/x86_64/CentOS-8.1.1911-x86_64-dvd1.iso'
        down = Downloader(url, 8, os.path.basename(url))
    else:
        url = sys.argv[1]  # 'http://mirrors.aliyun.com/centos/8.1.1911/isos/x86_64/CentOS-8.1.1911-x86_64-dvd1.iso'
        file = sys.argv[2]
        thread_num = int(sys.argv[3])
        down = Downloader(url, thread_num, file)
    down.run()