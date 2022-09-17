# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
plt.subplot(111)
# 设置数据表格
colLabels = ["第一季度", "第二季度", "第三季度", "第四季度"]
rowLabels = ["营业额/万元"]
numValues = [[200, 100, 150, 50]]
# 添加数据
elements = ["第一季度", "第二季度", "第三季度", "第四季度"]
num = [0.4, 0.2, 0.3, 0.1]
colors = ["#67E0E3", "#FFDB5C", "#97C979", "#FF9F7F"]
explode =(0.1,0,0,0)
# 设置饼图形状
wedges, texts, autotexts = plt.pie(num,autopct="%3.1f%%",explode=explode,shadow=False,colors=colors,textprops={'fontsize': 13, 'color': 'black'},)

# 设置标签
plt.legend(wedges,
           elements,
           fontsize=10,
           title="时间",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.4, 1))


colColors = ["#67E0E3", "#FFDB5C", "#97C979", "#FF9F7F"]
plt.table(cellText=numValues, cellLoc="center", colWidths=[0.2] * 5, colLabels=colLabels, colColours=colColors,
          rowLabels=rowLabels, rowLoc="center", loc="bottom")

# 保存图片到本地
plt.title('180512206-李环宇-2018年营业额')
plt.savefig('third.jpg')
plt.show()
