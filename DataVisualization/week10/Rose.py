from pyecharts.charts import Pie
from pyecharts import options as opts
import random, requests

url = 'https://lab.isaaclin.cn/nCoV/api/area'
data_json = requests.get(url).json()
country_list = []
count_list = []
ds = {}
for item in data_json['results']:
    if item['countryEnglishName']:
        if item['deadCount'] is not None and item['countryName'] is not None:
            if int(item['deadCount']) > 20000:
                d = {item['countryName']:item['deadCount']}
                ds.update(d)
ds = dict(sorted(ds.items(), key = lambda k: k[1]))
# 名称有重复的，把国家名作为 key 吧
country_list = ds.keys()
count_list = ds.values()
# 随机颜色生成
def randomcolor(kind):
    colors = []
    for i in range(kind):
        colArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colArr[random.randint(0, 14)]
        colors.append("#" + color)
    return colors
color_series = randomcolor(len(count_list))
# 创建饼图
pie = Pie(init_opts=opts.InitOpts(width='800px', height='900px'))
# 添加数据
pie.add("", [list(z) for z in zip(country_list, count_list)],
        radius=['20%', '100%'],
        center=['60%', '65%'],
        rosetype='area')

# 设置全局配置项
pie.set_global_opts(title_opts=opts.TitleOpts(title='全球新冠疫情',subtitle='死亡人数超过\n20000 的国家',
                                               title_textstyle_opts=opts.TextStyleOpts(font_size=15,color= '#0085c3'),
                                               subtitle_textstyle_opts= opts.TextStyleOpts(font_size=15,color= '#003399'),
                                               pos_right= 'center',pos_left= '53%',pos_top= '62%',pos_bottom='center'
                                              ),
                     legend_opts=opts.LegendOpts(is_show=False))
# 设置系列配置和颜色
pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
                                              formatter='{b}：{c}', font_style='italic',
                                              font_family='Microsoft YaHei'))
pie.set_colors(color_series)
pie.render('180512206-李环宇-南丁格尔玫瑰图.html')