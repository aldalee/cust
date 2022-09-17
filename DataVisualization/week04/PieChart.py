"""
-*- coding: utf-8 -*-
Created by lhy on 2020/9/26 21:36
Description:
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager as fm
from matplotlib import cm

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False
citys = ['北京', '上海', '广州', '深圳', '杭州', '武汉', '南京','沈阳', '大连', '重庆', '长春']
values = [random.randint(0,10000) for i in range(len(citys))]
s = pd.Series(values, index=citys)
labels = s.index
sizes = s.values

fig, ax = plt.subplots(figsize=(6,6)) # 设置绘图区域大小

colors = cm.rainbow(np.arange(len(sizes))/len(sizes)) # colormaps: Paired, autumn, rainbow, gray,spring,Darks
patches, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%',
        shadow=False, startangle=170, colors=colors)

ax.axis('equal')
ax.set_title('180512206李环宇-理工大学学生来源饼图-数据随机生成', loc='center')

# 重新设置字体大小
proptease = fm.FontProperties()
proptease.set_size('xx-large')

plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

plt.savefig('180512206李环宇-饼图-数据随机生成.jpg')
plt.show()