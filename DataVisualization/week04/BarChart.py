"""
-*- coding: utf-8 -*-
Created by lhy on 2020/9/27 15:59
Description:
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False

# 构建DataFrame
index = ['%d月'%x for x in range(1,13)]
pd = pd.DataFrame(np.random.randint(3000,size=36).reshape(12,3),index = index,columns=['一班','二班','三班'])

pd.plot(kind = 'bar',ylim = [0,4000],rot = 0)
plt.title("180512206李环宇-大数据班级平均月消费-数据随机生成")
plt.savefig('180512206李环宇-柱状图-数据随机生成.jpg')
plt.show()
