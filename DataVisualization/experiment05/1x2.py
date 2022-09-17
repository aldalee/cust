import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

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
    for row in reader:
        try:
            current_date3 = datetime.strptime(row[0], "%Y-%m-%d")
            high3 = int(row[1])
            low3 = int(row[3])
        except ValueError:
            print(current_date3, 'missing data')
        else:
            highs3.append(high3)
            dates3.append(current_date3)
            lows3.append(low3)
            # 根据数据绘制图形

    fig = plt.figure(dpi=200, figsize=(5, 4))
    plt.subplot(223)
    plt.plot(dates2, highs2, c='red', alpha=0.5)
    plt.plot(dates2, lows2, c='blue', alpha=0.5)
    plt.fill_between(dates2, highs2, lows2, facecolor='purple', alpha=0.2)
    plt.title("beautiful_weather_2014", fontsize=8)
    plt.xlabel('日期', fontsize=6)
    fig.autofmt_xdate()
    plt.ylabel("温度(F)", fontsize=6)
    plt.tick_params(axis='both', which='major', labelsize=5)

    plt.subplot(224)
    plt.plot(dates3, highs3, c='red', alpha=0.5)
    plt.plot(dates3, lows3, c='blue', alpha=0.5)
    plt.fill_between(dates3, highs3, lows3, facecolor='purple', alpha=0.2)
    plt.title("sunny_weather_2014", fontsize=8)
    plt.xlabel('日期', fontsize=6)
    fig.autofmt_xdate()
    plt.ylabel("温度(F)", fontsize=6)
    plt.tick_params(axis='both', which='major', labelsize=5)

    plt.show()
