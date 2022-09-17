# -*- coding: utf-8 -*-
"""
    dv_custype_clusters_hist.py
    KMeans客户聚类统计柱状图
    @author: lhy
    @date: 2021-6-22
"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# 解决中文乱码，设置字体为楷体
plt.rcParams['font.sans-serif'] = ['KaiTi']
# 解决正负号乱码
plt.rcParams['axes.unicode_minus'] = False

csvFile = './output' + os.sep + 'KMeans_clusters.csv'
data = pd.read_csv(csvFile, encoding='utf_8_sig')

# 设置图表x轴标签数据集
x_labels = ['C' + str(i) for i in range(1, 6)]
y_values = [y[0] for y in np.array(data.iloc[:, [0]].values[:])]



# 画图
ax = plt.subplot()
plt.style.use('ggplot')
ax.set_ylim([0, 30000])
ax.set_xlabel('客户类别')
ax.set_ylabel('聚类客户个数(单位：人)')
ax.set_title('聚类客户个数分析图')
bar = plt.bar(x_labels, y_values, width=0.5)
'''图表美化'''
# 为每一个矩形柱状图添加数值标签
for x, y in zip(x_labels, y_values):
    plt.text(x, y, '%.0f' % y, ha='center', va='bottom')
plt.grid(linestyle='--')
# plt.style.use('ggplot')
plt.show()
imageFile = os.getcwd() + os.sep + 'output' + os.sep + 'custype_clusters_hist.jpg'
# plt.savefig(imageFile)
print("custype_clusters_hist.jpg 图片保存成功")
