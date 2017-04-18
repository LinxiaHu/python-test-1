#coding=utf-8
import re
import os
import time


def changeName(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path)
        lists = file_path[1].split('.')
        file_ext = lists[-1]  # 取出后缀名(列表切片操作)
        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
        if file_ext in img_ext:
            os.rename(path, file_path[0] + '/' + lists[0] + '_fc.' + file_ext)
            i += 1  # 注意这里的i是一个陷阱
            # 或者
            # img_ext = 'bmp|jpeg|gif|psd|png|jpg'
            # if file_ext in img_ext:
            #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            changeName(os.path.join(path, x))  # os.path.join()在路径处理上很有用


img_dir = 'D:\\xx\\xx\\images'
img_dir = img_dir.replace('\\', '/')
start = time.time()
i = 0
changeName(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f' % (c))
print('总共处理了 %s 张图片' % (i))
