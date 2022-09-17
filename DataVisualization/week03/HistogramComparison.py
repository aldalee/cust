"""
-*- coding: utf-8 -*-
Created by lhy on 2020/9/20 23:16
Description:
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False


x = [1, 2, 3, 4, 5,6]
y = [122,146,193,194,125,145]
y1 = [161,197,233,238,162,190]


plt.bar(x, y1, align="center", color="yellow", tick_label=["北京", "上海", "广州", "深圳","杭州","武汉"])
plt.bar(x, y1, align="center", bottom=y, color="blue")

plt.xlabel("城市")
plt.ylabel("盈收")

plt.grid(True,axis="y", ls="-.",color="red",alpha=0.1)
plt.legend()


for x, y in enumerate(y):
    plt.text(x+1, y-20, '%s' % y, ha='center', va='center')
for x, y in enumerate(y1):
    plt.text(x+1, y-20, '%s' % y, ha='center', va='top')
plt.title("180512206李环宇-六大城市盈收")
plt.show()
