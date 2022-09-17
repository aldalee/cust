import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False   # 用来正常显示负号

X = np.linspace(-np.pi,np.pi,256,endpoint=True)   #获取x坐标

sin,cos = np.sin(X),np.cos(X)  #获取y坐标

plt.plot(X,sin,"b-",lw=2.5,label="正弦Sin()")
plt.plot(X,cos,"r-",lw=2.5,label="余弦Cos()")


plt.xlim(X.min()*1.5,X.max()*1.5)
plt.ylim(cos.min()*1.5,cos.max()*1.5)

plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'])
plt.yticks([-1,0,1])

plt.title("180512206-李环宇-实验一",fontsize=16,color="black")

plt.text(+2.1,-1.4,"",fontsize=16,color="purple")


ax=plt.gca()  #获取Axes对象
ax.spines['right'].set_color('none')    #隐藏右边界
ax.spines['top'].set_color('none')      #隐藏上边界

ax.xaxis.set_ticks_position('bottom')   #x轴坐标刻度设置在坐标轴下面
ax.spines['bottom'].set_position(('data',0))  #x轴坐标轴平移至经过零点（0,0）位置

ax.yaxis.set_ticks_position('left')           #y轴坐标刻度设置在坐标轴下面
ax.spines['left'].set_position(('data',0))    #y轴坐标轴平移至经过零点（0,0）位置

plt.legend(loc="upper left",fontsize=12)


t1 = 2*np.pi/3 #设定第一个点的x轴值
t2 = -np.pi   #设定第二个点的x轴值
plt.plot([t1,t1],[0,np.sin(t1)],color ='b',linewidth=1.5,linestyle="--")
#第一个列表是x轴坐标值，第二个列表是y轴坐标值
#这两个点坐标分别为（t1,0）和（t1，np.sin(t1)），根据两点画直线l1
plt.plot([t2,t2],[0,np.cos(t2)],color ='r',linewidth=1.5,linestyle="--")
#这两个点坐标分别为（t2,0）和（t2，np.cos(t2)），根据两点画直线l2


plt.scatter([t1,],[np.sin(t1),], 50, color ='b')
plt.scatter([t2,],[np.cos(t2),], 50, color ='r')


plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t1,np.sin(t1)),    #点的位置
             xycoords='data',       #注释文字的偏移量
             xytext=(+10,+30),      #文字离点的横纵距离
             textcoords='offset points',
             fontsize=14,      #注释的大小
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))   #箭头指向的弯曲度

plt.annotate(r'$\cos(-\pi)=-1$',
             xy=(t2,np.cos(t2)),   #点的位置
             xycoords='data',      #注释文字的偏移量
             xytext=(0,-40),       #文字离点的横纵距离
             textcoords='offset points',
             fontsize=14,    #注释的大小
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))   #箭头指向的弯曲度

for label in ax.get_xticklabels()+ax.get_yticklabels():           #获取刻度
    label.set_fontsize(18)                                        #设置刻度字体大小

    # label.set_bbox(dict(facecolor='r',edgecolor='g',alpha=0.5))   #set_bbox为刻度添加边框
                                                                  #facecolor:背景填充颜色
                                                        #edgecolor:边框颜色
                                                                  #alpha:透明度
plt.fill_between(X,np.abs(X)<0.5,sin,sin>0.5,color='g',alpha=0.8)
#设置正弦函数的填充区域，其中的一种方式
plt.fill_between(X,cos,where=(-2.5<X)&(X<-0.5),color='purple')
#设置余弦函数的填充区域，另外一种方式

plt.grid()
plt.show()   #显示图表
