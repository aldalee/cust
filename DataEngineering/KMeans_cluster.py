# -*- coding: utf-8 -*-
"""
    KMeans_cluster.py
    KMeans客户聚类算法分析
    @author: lhy
    @date: 2021-6-22
"""
import pandas as pd
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

csvFile = './output' + os.sep + 'data_zscore.csv'
data = pd.read_csv(csvFile, encoding='utf_8_sig')
print(data.head())

# 找到最好的聚类簇
# 从sklearn导入聚类算法函数
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

random_state = 5
score = []
inertia = []
nums = range(2, 10)

# 遍历多个可能的候选簇数量
for n_clusters in range(2, 10):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(data)
    inertia.append(kmeans.inertia_)  # 衡量模型性能
    score.append(silhouette_score(data, kmeans.labels_, sample_size=128, metric='euclidean'))  # 衡量聚类算法的指标

plt.figure(figsize=(10, 6))
# 使用ggplot的绘图风格
plt.style.use('seaborn-darkgrid')
plt.subplot(121)
plt.plot(nums, score)
plt.grid(linestyle=':')
plt.xlabel('K')
plt.ylabel('Score')
plt.title('Performance of K-means')

plt.subplot(122)
plt.plot(nums, inertia)
plt.grid(linestyle=':')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Inertia of K-means')
plt.show()

# 设置聚类分析算法的分类个数参数
k = 5
# 创建KMeans聚类模型对象实例
kmodel = KMeans(n_clusters=k)

# 模型的训练
kmodel.fit(data)

# 查看客户样本对应的类别个数
r1 = pd.Series(kmodel.labels_).value_counts()
print(">>>查看客户样本对应的类别个数:")
print(r1)

# 查看聚类中心值
r2 = pd.DataFrame(kmodel.cluster_centers_)
print(">>>查看客户样本类别的聚类标准中心值:")
print(r2)

# 连接数据形成最终统一的聚类分析统计表1 KMeans_clusters.csv
data_cluster = pd.concat([r1, r2], axis=1)
data_cluster.columns = ['聚类个数'] + list(data.columns)
print(">>>KMeans聚类统计分析表1：")
print(data_cluster)

# 保存 KMeans_clusters.csv
csvFile = os.getcwd() + os.sep + 'output' + os.sep + 'KMeans_clusters.csv'
data_cluster.to_csv(csvFile, encoding='utf_8_sig', index=False)
print("KMeans_clusters.csv文件写入成功！")

# 将原始无标签数据转化为有标签数据
data_details = pd.concat([data, pd.Series(kmodel.labels_, index=data.index)], axis=1)
data_details.columns = list(data.columns) + ['客户类别']
print(">>>KMeans客户分类明细统计表：")
print(data_details.head())

# 保存 KMeans_clusters_details.csv
csvFile = os.getcwd() + os.sep + 'output' + os.sep + 'KMeans_clusters_details.csv'
data_details.to_csv(csvFile, encoding='utf_8_sig', index=False)
print("KMeans_clusters_details文件写入成功！")

# 聚类中心点在每个维度上的散点图
clu = kmodel.cluster_centers_
x = [1, 2, 3, 4, 5]
colors = ['red', 'green', 'yellow', 'blue', 'black']
for i in range(5):
    plt.plot(x, clu[i], label='cluster ' + str(i), linewidth=1, color=colors[i], marker='o')
plt.legend()
plt.xlabel('ZL--ZR--ZF--ZM--ZC')
plt.ylabel('values')
plt.show()

# 聚类结果进行可视化展现
# 查看每个类别下，每个数值得分布数据
for i in range(k):
    data[data_details['客户类别'] == i].plot(kind='kde', linewidth=2, subplots=True, sharex=False,
                                         layout=(1, data.shape[1]), figsize=(16, 2))
    plt.legend()
plt.show()

