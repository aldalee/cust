# coding=utf-8
from matplotlib import pyplot as plt
import matplotlib as mpl
# 解决中文乱码
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

movie_name = ['少年的你','中国机长','我和我的祖国','双子杀手']
movie_total_box_office_1 = [15900,200,5000,100]
movie_total_box_office_2 = [12100,500,2100,300]
movie_total_box_office_3 = [2200,900,2500,500]
movie_total_box_office_4 = [1700,1900,1900,100]
#定义变量
bar_width = 0.1

bar_1 = list(range(len(movie_name)))
bar_2 = [i+bar_width for i in bar_1]
bar_3 = [i+bar_width for i in bar_2]
bar_4 = [i+bar_width for i in bar_3]

#设置图片尺寸与清晰度
plt.figure(figsize=(13, 8), dpi=80)

#导入数据，绘制条形图
plt.bar(range(len(movie_name)), movie_total_box_office_1, width=bar_width, label='第一星期')
plt.bar(bar_2, movie_total_box_office_2, width=bar_width, label='第二星期')
plt.bar(bar_3, movie_total_box_office_3, width=bar_width, label='第三星期')
plt.bar(bar_4, movie_total_box_office_4, width=bar_width, label='第四星期')

#添加标题
plt.title('180512206-李环宇-热映电影票房对比', size=20)
#添加xy轴
plt.xlabel('电影名称',fontsize=20)
plt.ylabel('电影票房(元)',fontsize=20)
#x轴刻度
plt.xticks(bar_2, movie_name,size=20,rotation=45)
plt.legend()

#展示效果图
plt.show()
