import matplotlib.pyplot as plt
import matplotlib as mpl
# 解决中文乱码
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
#电影名
movie_name = ['少年的你','中国机长','我和我的祖国','双子杀手','哪吒之魔童降世','寄生虫','蜘蛛侠','复联4','极限逃生','送我上青云','流浪地球','疯狂的外星人']
#总票房，单位：亿
movie_total_box_office = [46.81, 42.05, 21.83, 17.03, 13.46, 11.38, 10.78, 10.25, 9.46, 9.26, 8.88, 7.88]
#设置图形大小
plt.figure(figsize=(18,12), dpi=80)
#绘制条形图
plt.bar(range(len(movie_name)), movie_total_box_office, width=0.5, color='orange')  #bar绘制正常的条形图，x轴对应movie_name, y轴对应movie_total_box_office
#设置字符串到x轴fontproperties="SimHei" 设置显示汉字（黑体）
plt.xticks(range(len(movie_name)), movie_name, fontproperties="SimHei", rotation=45)
xstep = []  #初始x轴刻度
for i in range(50):  #用for循环增加step的刻度值
    xstep.append(i)
ystep = []
for i in range(0,50,5):  #用for循环增加step的刻度值
    ystep.append(i)
plt.yticks(ystep,fontsize=15)
plt.title('180512206-李环宇-2019年度内地电影票房top20',fontsize=23)
plt.ylabel('电影票房(亿)',fontsize=20)
plt.xticks(fontsize=17)
# plt.grid(alpha=0.5)
#保存成图片
plt.show()
