# -*- coding: utf-8 -*-
"""
    data_reduction.py
    对航空数据进行规约
    @author: lhy
    @date: 2021-6-22
"""

import pandas as pd
import os

datafile = './output' + os.sep + 'data_cleaned.csv'
data = pd.read_csv(datafile, encoding='utf-8')

data = data[['FFP_DATE', 'LOAD_TIME', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM', 'LAST_TO_END']]

# 将数据转换成LRFMC指标格式
data['L'] = [i.days for i in (pd.to_datetime(data['LOAD_TIME']) - pd.to_datetime(data['FFP_DATE'])) / 30]
data['R'] = data['LAST_TO_END'] / 30
data['F'] = data['FLIGHT_COUNT']
data['M'] = data['SEG_KM_SUM']
data['C'] = data['avg_discount']
# 筛选出LRFMC五个维度指标
data = data[['L', 'R', 'F', 'M', 'C']]
print(data.head())

# 保存文件
csvFile = os.getcwd() + os.sep + 'output' + os.sep + 'data_reduction.csv'
data.to_csv(csvFile, encoding='utf_8_sig', index=False)
print("data_reduction.csv文件写入成功！")

# 数据标准化
data = (data - data.mean(axis=0)) / data.std(axis=0)
data.columns = ['Z' + i for i in data.columns]  # 列表推导式
print(data.head())

# 保存文件
csvFile = os.getcwd() + os.sep + 'output' + os.sep + 'data_zscore.csv'
data.to_csv(csvFile, encoding='utf_8_sig', index=False)
print("data_zscore.csv文件写入成功！")
