import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
tips = sns.load_dataset("tips")
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
sns.set(style="whitegrid", color_codes=True)
# sns.stripplot(x="day", y="total_bill", data=tips)
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
plt.title("180512206-lihuanyu")
plt.show()