import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# 中文乱码
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 准备数据data
labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = [1000.0, 1500.0, 2000.0, 2500.0, 4000.0, 8300.0, 5800.0]
ax = plt.subplot(111)
for x, y in enumerate(data):
    plt.text(x, y + 0.2, '%s' % y, ha='center', va='top', fontsize=15)
plt.plot(labels, data, ls="-", lw=2, color="orange", marker="o", ms=10, mfc="c", mec="c")
ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))
plt.xticks(labels, labels, rotation=45)
plt.title('180512206-李环宇-卫星路国商一周营业额')
plt.savefig('./first.jpg')
plt.show()
