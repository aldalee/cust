# -*- coding: utf-8 -*-
"""
    data_explore.py
    对航空数据进行基本的探索，返回缺失值以及最大值，最小值
    @author: lhy
    @date: 2021-6-22
"""

import pandas as pd
import os

datafile = './data' + os.sep + 'air_data.csv'  # 航空原始数据文件
data = pd.read_csv(datafile, encoding='utf-8')  # 将数据导入
print(data.head())

# 将每个属性的描述性统计量展示,获取数据中的空值项，并进行转置处理
explore = data.describe(percentiles=[], include='all').T
print(">>>数据描述统计结果：")
print(explore)

# 计算属性对应的空值个数
explore['null'] = len(data) - explore['count']
# 选取部分探索内容
explore = explore[['null', 'max', 'min']]
# 属性列名的重命名
explore.columns = [u'空值记录数', u'最大值', u'最小值']
# 对索引命名
explore.index.name = u'属性名称'
print(">>>最终探索的数据结果：")
print(explore)

# 将探索的结果保存到csv文件
csvPath = os.getcwd() + os.sep + 'output'
if not os.path.exists(csvPath):
    print(">>>程序检测到指定路径不存在，正在创建中...")
    os.mkdir(csvPath)
    print(">>>输出文件夹创建成功！")
resultFile = csvPath + os.sep + 'data_explore.csv'  # 数据探索结果文件
explore.to_csv(resultFile, encoding='utf_8_sig', index=False)
print("data_explore.csv文件写入成功！")
