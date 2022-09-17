"""
-*- coding: utf-8 -*-
Created by lhy on 2020/9/12 16:07
Description: 数据可视化9.10课堂作业
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 解决中文乱码
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.linspace(0.05,10,1000)
y = np.sin(x)
plt.axvspan(xmin=1.0,xmax=2.0,facecolor="y",alpha=0.3)
plt.axhspan(ymin=1.0,ymax=2.0,facecolor="y",alpha=0.3)
plt.plot(x,y,ls="-",lw=2,c="c",label="f(x)=sin(x)")
plt.legend()

plt.xlim(0, 4*np.pi)
plt.ylim(-1.5, 1.5)

plt.xlabel('x Axis')
plt.ylabel('y Axis')
# 显示最大值
plt.annotate(
            "maximum",
            xy=(np.pi/2,1.0),
            xytext=((np.pi/2+1.0)+1,0.8),
            weight="bold",
            color="b",
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b")
            )
# 显示最小值
plt.annotate(
            "minimum",
            xy=(np.pi*3/2,-1.0),
            xytext=((np.pi*3/2),0),
            weight="bold",
            color="b",
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b")
            )
# 绘制参考区域
plt.axvspan(xmin=1.0,xmax=3.0,facecolor="r",alpha=0.5)
plt.axhspan(ymin=0.5,ymax=1.0,facecolor="b",alpha=0.3)
plt.grid(linestyle=":",color="r")
plt.title('180512206李环宇')
plt.show()