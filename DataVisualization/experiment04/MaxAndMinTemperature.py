# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import datetime
import matplotlib.pyplot as mp
# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus'] = False
#import pandas as pd

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)  # 获取第一行的内容。  指针已经移动到了第二行开头

    #打印文件列表头及其位置
    # for index, column in enumerate(header_row): #enumerate拥有遍历序列中的元素以及它们的下标
    #     print index, column

    #column_name_max_temperature = head_row[1]  #获取最高温度那一列的列名

    dates = []
    max_temperatures = []
    min_temperatures = []

    #从第二行开始遍历，获取日期和最高温度
    #检查异常，如果数据为空，打印出异常信息
    for row in  reader:
        try:
            current_date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
            max_temperature = int(row[1])
            min_temperature = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            max_temperatures.append(max_temperature)
            min_temperatures.append(min_temperature)


#绘制图形
fig = plt.figure(dpi=128, figsize=(10, 7))  #设置图形分辨率及大小
plt.plot(dates, max_temperatures, color='red', linewidth=1)   #设置图形横坐标值、纵坐标值（最高温度）及线条颜色宽度
plt.plot(dates, min_temperatures, color='blue', linewidth=1) #设置图形横坐标值、纵坐标值（最低温度）及线条颜色宽度
#给图标区域着色。alpha为0表示完全透明，1（默认）表示完全不透明。
plt.fill_between(dates, max_temperatures, min_temperatures, facecolor='yellow', alpha=0.5)

#设置图形属性
plt.title('Daily high and low temperatures - 2014 Death valley, CA\n180512206-李环宇', fontsize=24)  #设置图形标题，标题字体大小及颜色
# plt.xlabel('', fontsize=20, color='blue')
plt.ylabel('Temperature (F)', fontsize=20)  #设置y轴标题，标题字体大小及颜色
plt.axes().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))   #设置x轴日期显示的格式
#设置x轴日期显示的间隔，2d表示两天，1m表示1个月。当要显示一个月的日期时，如果每天都显示，X轴会很挤，这个设置就有用处了
# plt.xticks(pd.date_range(dates[0],dates[-1],freq='1m'))
fig.autofmt_xdate() #设置时间显示为斜体
plt.tick_params(axis='x',  labelsize=10)    #设置x轴日期的显示，这里设置小一点。 axis（x：x轴，y：y轴，both：x和y轴）
plt.show()  #显示图形