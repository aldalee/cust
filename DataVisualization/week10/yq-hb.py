import requests
from pyecharts.charts import *
from pyecharts import options as opts

url = 'https://lab.isaaclin.cn/nCoV/api/area'
data = requests.get(url).json()
for item in data['results']:
    if item['provinceShortName'] == '湖北':
        hb_data = item['cities']
hb_bar = (
        Bar(init_opts=opts.InitOpts(theme='dark'))
        .add_xaxis([hd['cityName'] for hd in hb_data])
        .add_yaxis('累计确诊人数', [hd['confirmedCount'] for hd in hb_data])
        .add_yaxis('累计治愈人数', [hd['curedCount'] for hd in hb_data])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="湖北新冠疫情确诊及治愈情况"),
            legend_opts=opts.LegendOpts(is_show=True)
                )
        )
hb_bar.render(path='湖北新冠疫情图.html')