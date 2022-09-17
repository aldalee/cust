"""
-*- coding: utf-8 -*-
Created by lhy on 2020/10/22 15:23
Description:
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
font = FontProperties(size=14)
#创建数据
plt.figure(figsize=(10,6))
x=np.arange(5)
y1=[100,120,70,68,82]
y2=[120,75,70,78,85]
std_err1=[7,3,5,2,9]
std_err2=[5,1,4,2,5]
error_attri={"elinewidth":2,"ecolor":"black","capsize":6}
bar_width=0.4
tick_label=["法学","计算机","电信","机电","哲学"]
#创建图形
plt.bar(x,y1,
bar_width,
#不在外部设置width这个属性，会报错
color="#87cee3",
align="center",
yerr=std_err1,
error_kw=error_attri,
#error_kw是设计误差棒具体细节的属性
label="2020",
alpha=1)
plt.bar(x+bar_width,y2,
#若没有向右侧增加一个bar——width的话，第一个柱体会被遮挡住
bar_width,
color="#cd5c5c",
yerr=std_err2,
error_kw=error_attri,
label="2019"
,alpha=1
)
#创建辅助标签
plt.xlabel("专业",fontproperties=font)
plt.ylabel("薪资量(万元)",fontproperties=font)
plt.xticks(x+bar_width/2,tick_label,fontproperties=font)
#xticks在py2中与3不是完全相同，tick_label用列表对名称进行了设计，此处设计其他属性
plt.title("180512206-李环宇-北京大学不同专业不同年份年薪图",fontproperties=font)
plt.grid(axis="y",ls="-",color="purple",alpha=0.7)
plt.legend()
plt.show()