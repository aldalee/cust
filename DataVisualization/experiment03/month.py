import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus'] = False


taobao = np.array([8000, 8500, 9000, 10983, 6789, 9867, 3598, 5867, 9999, 23451, 9877, 10000])
jd = np.array([8594, 7396, 5982, 9437, 9162, 15634, 9945, 6462, 8235, 6666, 9994, 15493])
mp.figure('180512206-李环宇-商城月营业额', facecolor='lightgray')
mp.title('180512206-李环宇-商城月营业额', fontsize=16)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Volume', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':', axis='y')
x = np.arange(12)
a = mp.bar(x - 0.2, taobao, 0.4, color='dodgerblue', label='淘宝', align='center')
b = mp.bar(x + 0.2, jd, 0.4, color='orangered', label='京东', align='center')
# 设置标签
for i in a + b:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%d' % int(h), ha='center', va='bottom')
mp.xticks(x, ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])

mp.legend()
mp.savefig("./second.jpg")
mp.show()