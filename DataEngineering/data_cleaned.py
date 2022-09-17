# -*- coding: utf-8 -*-
"""
    data_cleaned.py
    对航空数据进行清洗
    @author: lhy
    @date: 2021-6-22
"""

import pandas as pd
import os

datafile = './data' + os.sep + 'air_data.csv'  # 航空原始数据文件
data = pd.read_csv(datafile, encoding='utf-8')  # 将数据导入
print(data.head())

print(">>>数据的各个属性相关信息:")
data.info()

'''数据清洗'''
# 丢弃票价为空的记录
data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
print("\n>>>根据一级条件进行筛选后的数据:")
data.info()

# 丢弃票价为0，平均折扣率不为0、总飞行公里数大于0的记录。
condition1 = data['SUM_YR_1'] != 0
condition2 = data['SUM_YR_2'] != 0
condition3 = (data['SEG_KM_SUM'] != 0) & (data['avg_discount'] == 0)
data = data[condition1 | condition2 | condition3]
print("\n>>>根据二级条件进行筛选后的数据:")
data.info()

# 保存数据
csvFile = os.getcwd() + os.sep + 'output' + os.sep + 'data_cleaned.csv'
data.to_csv(csvFile, encoding='utf_8_sig', index=False)
print("data_cleaned.csv数据文件写入成功！")
