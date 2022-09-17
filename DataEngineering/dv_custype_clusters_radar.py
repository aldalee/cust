# -*- coding: utf-8 -*-
"""
    dv_custype_clusters_radar.py
    KMeans客户聚类统计雷达图
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
customers_names = pd.Series(['C' + str(i) for i in range(1, 6)])
data = pd.concat([customers_names, data], axis=1)
data.columns = ['类别名称', '聚类个数', 'ZL:客户关系长度', 'ZR:消费时间间隔', 'ZF:消费频率', 'ZM:飞行里程', 'ZC:平均折扣系数']
print(data.head())
# 获取客户名称数据集
kinds = data.iloc[:, 0]
print(">>>kinds:")
print(kinds)
# 获取特征值数据矩阵
centers = pd.concat([data.iloc[:, 2:], data.iloc[:, 2]], axis=1)
# 转换成二维数据结构，雷达图需要二维数组结构数据充当参数
centers = np.array(centers)
print(">>>centers:")
print(centers)

# 获取特征值的字段名称数据集
labels = data.iloc[:, 2:].columns
n = len(labels)
# 设置雷达图的基础底线结构
angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
angles = np.concatenate((angles, [angles[0]]))

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)  # 设置作为极点坐标
floor = np.floor(centers.min())
ceil = np.ceil(centers.max())

# 画出若干个五边形
for i in np.arange(floor, ceil + 0.5, 0.5):
    ax.plot(angles, [i] * (n + 1), '--', lw=0.5, color='black')

# 去掉背景圆
ax.spines['polar'].set_visible(False)  # 外圈
ax.grid()  # 内圈
ax.set_yticks([])  # 去掉刻度
ax.set_theta_zero_location('N')  # 摆正位置
ang = angles * 180 / np.pi
ax.set_thetagrids(ang[:-1], labels)
# 绑定数据
for i in range(len(kinds)):
    ax.plot(angles, centers[i], lw=2, label=kinds[i])

# 添加图例
plt.legend(loc='lower right', bbox_to_anchor=(1.2, 0.1))
# plt.show()
imageFile = os.getcwd() + os.sep + 'output' + os.sep + 'custype_clusters_radar.jpg'
plt.savefig(imageFile)
print("custype_clusters_radar.jpg 图片保存成功")