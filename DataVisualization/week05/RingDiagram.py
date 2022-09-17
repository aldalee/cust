"""
-*- coding: utf-8 -*-
Created by lhy on 2020/10/10 23:38
Description:
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

# 数据集，x1,x2分别对应外部、内部百分比例(外部为学霸，内部为学渣在时间安排，数据纯属虚构)
x1 = [30,30,10,10,5,15]
x2 = [5,5,20,30,30,10]

# 设置饼状图各个区块的颜色
color = ['aqua','PaleGreen','lightcoral','olive','gold','RoyalBlue']

plt.pie(x1,
        autopct='%3.1f%%',
        radius=1,
        pctdistance=0.85,
        colors=color,
        wedgeprops=dict(linewidth=2,width=0.3,edgecolor='w'))
plt.pie(x2,
        autopct='%3.1f%%',
        radius=0.7,
        pctdistance=0.7,
        colors=color,
        wedgeprops=dict(linewidth=2,width=0.4,edgecolor='w'))
# 图例
legend_text = ['代码', '算法', '跑步', '美餐', '王者', '睡觉']
# 设置图例标题、位置
plt.legend(legend_text, title='任务表', loc='lower right')
# 设置坐标轴比例以显示为圆形
plt.axis('equal')
plt.title("180512206李环宇-学霸和学渣的时间对比")
plt.show()