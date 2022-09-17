"""
-*- coding: utf-8 -*-
Created by lhy on 2020/10/29 14:37
Description:
"""
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Sankey

# 数据
data = [[ 'Brazil', 'Portugal', 5 ],
       [ 'Brazil', 'France', 1 ],
       [ 'Brazil', 'Spain', 1 ],
       [ 'Brazil', 'England', 1 ],
       [ 'Canada', 'Portugal', 1 ],
       [ 'Canada', 'France', 5 ],
       [ 'Canada', 'England', 1 ],
       [ 'Mexico', 'Portugal', 1 ],
       [ 'Mexico', 'France', 1 ],
       [ 'Mexico', 'Spain', 5 ],
       [ 'Mexico', 'England', 1 ],
       [ 'USA', 'Portugal', 1 ],
       [ 'USA', 'France', 1 ],
       [ 'USA', 'Spain', 1 ],
       [ 'USA', 'England', 5 ],
       [ 'Portugal', 'Angola', 2 ],
       [ 'Portugal', 'Senegal', 1 ],
       [ 'Portugal', 'Morocco', 1 ],
       [ 'Portugal', 'South Africa', 3 ],
       [ 'France', 'Angola', 1 ],
       [ 'France', 'Senegal', 3 ],
       [ 'France', 'Mali', 3 ],
       [ 'France', 'Morocco', 3 ],
       [ 'France', 'South Africa', 1 ],
       [ 'Spain', 'Senegal', 1 ],
       [ 'Spain', 'Morocco', 3 ],
       [ 'Spain', 'South Africa', 1 ],
       [ 'England', 'Angola', 1 ],
       [ 'England', 'Senegal', 1 ],
       [ 'England', 'Morocco', 2 ],
       [ 'England', 'South Africa', 7 ],
       [ 'South Africa', 'China', 5 ],
       [ 'South Africa', 'India', 1 ],
       [ 'South Africa', 'Japan', 3 ],
       [ 'Angola', 'China', 5 ],
       [ 'Angola', 'India', 1 ],
       [ 'Angola', 'Japan', 3 ],
       [ 'Senegal', 'China', 5 ],
       [ 'Senegal', 'India', 1 ],
       [ 'Senegal', 'Japan', 3 ],
       [ 'Mali', 'China', 5 ],
       [ 'Mali', 'India', 1 ],
       [ 'Mali', 'Japan', 3 ],
       [ 'Morocco', 'China', 5 ],
       [ 'Morocco', 'India', 1 ],
       [ 'Morocco', 'Japan', 3 ]]

df = pd.DataFrame(data, columns=['source', 'target', 'value'])
print('- data shape: ', df.shape, '\n')

# 生成节点， 先合并源节点和目标节点，然后去除重复的节点，最后输出成 dict 形式
nn = pd.concat([df['source'], df['target']])
nn = nn.drop_duplicates()
nodes = pd.DataFrame(nn, columns=['name']).to_dict(orient='records')
print('- nodes:\n', nodes, '\n')

# 生成连接， dict 形式
links = df.to_dict(orient='records')
print('- links:\n', links, '\n')

# 绘制桑基图
sk =(
    Sankey(init_opts=opts.InitOpts(width="800px", height="600px")) # 页面大小
    .add(
        series_name="legend", # legend
        nodes=nodes,
        links=links,
        # opacity 透明度； curve 弯曲程度； color 色系
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"), # 节点名称
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="sankey")) # 标题
    .render("sankey.html") # 保存成 html 文件
)
