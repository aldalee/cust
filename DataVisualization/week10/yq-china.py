import requests
from pyecharts.charts import *
from pyecharts import options as opts

url = 'https://lab.isaaclin.cn/nCoV/api/area'
data = requests.get(url).json()
province_data = []
for item in data['results']:
    if item['countryName'] == '中国':
        province_data.append((item['provinceShortName'], item['confirmedCount']))
china_map = (
        Map(init_opts=opts.InitOpts(theme='dark'))
        .add('确诊人数', province_data, 'china',is_map_symbol_show=False,  is_roam=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color='#ffffff'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国疫情累计确诊人数地图"),
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(max_=2000,
                                              is_piecewise=True,
                                              pieces=[
                                                  {"max": 9999, "min": 1000, "label": "1000-9999人", "color": "#B40404"},
                                                  {"max": 999, "min": 500, "label": "500-999人", "color": "#DF0101"},
                                                  {"max": 499, "min": 100, "label": "100-499人", "color": "#F78181"},
                                                  {"max": 99, "min": 10, "label": "10-99人", "color": "#F5A9A9"},
                                                  {"max": 9, "min": 0, "label": "1-9人", "color": "#FFFFCC"},
                                              ])
        )
)
china_map.render(path='中国疫情地图.html')