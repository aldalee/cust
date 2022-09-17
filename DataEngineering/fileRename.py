# -*- coding: utf-8 -*-
"""
    fileRename.py
    文件批量重命名
    @author: lhy
    @date: 2021-7-01
"""

import os
import string
import shutil

PATH = './images/'
images = os.listdir(PATH)
copyImages = images
outPATH = './imageOut/'

try:
    if os.path.exists(outPATH):
        shutil.rmtree(outPATH)  # 递归的删除文件夹下的所有文件
    os.mkdir(outPATH)
except Exception as e:
    print("Exception:" + e)

for image in copyImages:
    if image.endswith('.png'):
        oldName = image
        image = image.strip(string.digits)[:-4]     # 剔除文件首尾的数字并提取出文件名
        newName = '综合课程设计-结果-' + image + '180512206-李环宇.png'
        os.rename(PATH + oldName, outPATH + newName)
print("Done!")
