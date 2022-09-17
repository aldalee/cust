import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    # 获取日期和最高气温,最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

filename1 = 'death_valley_2014.csv'
with open(filename1) as f1:
    reader = csv.reader(f1)
    header_row = next(reader)

    # 获取日期和最高气温,最低气温
    dates1, highs1, lows1 = [], [], []
    for row in reader:
        try:
            current_date1 = datetime.strptime(row[0], "%Y-%m-%d")
            high1 = int(row[1])
            low1 = int(row[3])
        except ValueError:
            print(current_date1, 'missing data')
        else:
            highs1.append(high1)
            dates1.append(current_date1)
            lows1.append(low1)

filename2 = 'death_valley_2014.csv'
with open(filename2) as f2:
    reader = csv.reader(f2)
    header_row = next(reader)


    # 获取日期和最高气温,最低气温
    dates2, highs2, lows2 = [], [], []
    for row in reader:
        try:
            current_date2 = datetime.strptime(row[0], "%Y-%m-%d")
            high2 = int(row[1])
            low2 = int(row[3])
        except ValueError:
            print(current_date2, 'missing data')
        else:
            highs2.append(high2)
            dates2.append(current_date2)
            lows2.append(low2)

filename3 = 'sitka_weather_2014.csv'
with open(filename3) as f3:
    reader = csv.reader(f3)
    header_row = next(reader)

    # 获取日期和最高气温,最低气温
    dates3, highs3, lows3 = [], [], []
    for row in reader:  # 依此循环csv文件的每一行
        try:
            current_date3 = datetime.strptime(row[0], "%Y-%m-%d")  # s取出每一行的下标为0的数据
            high3 = int(row[1])  # 循环的每一行为列表形式存在在row里，取出每一行的下标为1的数据
            low3 = int(row[3])
        except ValueError:
            print(current_date3, 'missing data')
        else:
            highs3.append(high3)
            dates3.append(current_date3)
            lows3.append(low3)
            # 根据数据绘制图形

    fig = plt.figure(dpi=200, figsize=(5, 3))
    plt.subplot(221)  # 设置绘图窗口的尺寸
    plt.plot(dates, highs, c='red', alpha=0.5)  # alpha设置颜色的透明度。0是完全透明；1是完全不透明
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # fill_between()接收一个x值系列和两个y值系列，并填充两个y值系列之间的空间。
    plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.2)

    # 设置图形的格式
    plt.title("sitka_weather_2014", fontsize=8)
    plt.xlabel('日期', fontsize=6)
    fig.autofmt_xdate()  # 使x轴标签绘制为斜的日期标签，以免它们彼此重叠
    plt.ylabel("温度(F)", fontsize=6)
    plt.tick_params(axis='both', which='major', labelsize=5)

    plt.subplot(222)
    plt.plot(dates1, highs1, c='red', alpha=0.5)
    plt.plot(dates1, lows1, c='blue', alpha=0.5)
    plt.fill_between(dates1, highs1, lows1, facecolor='yellow', alpha=0.2)
    plt.title("death_valley_2014", fontsize=8)
    plt.xlabel('日期', fontsize=6)
    fig.autofmt_xdate()
    plt.ylabel("温度(F)", fontsize=6)
    plt.tick_params(axis='both', which='major', labelsize=5)

    plt.subplot(223)
    plt.plot(dates2, highs2, c='red', alpha=0.5)
    plt.plot(dates2, lows2, c='yellow', alpha=0.5)
    plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.2)
    plt.title("beautiful_weather_2014", fontsize=8)
    plt.xlabel('日期', fontsize=6)
    fig.autofmt_xdate()
    plt.ylabel("温度(F)", fontsize=6)
    plt.tick_params(axis='both', which='major', labelsize=5)

    plt.subplot(224)
    plt.plot(dates3, highs3, c='red', alpha=0.5)
    plt.plot(dates3, lows3, c='yellow', alpha=0.5)
    plt.fill_between(dates3, highs3, lows3, facecolor='blue', alpha=0.2)
    plt.title("sunny_weather_2014", fontsize=8)
    plt.xlabel('日期', fontsize=6)
    fig.autofmt_xdate()
    plt.ylabel("温度(F)", fontsize=6)
    plt.tick_params(axis='both', which='major', labelsize=5)

    plt.show()
