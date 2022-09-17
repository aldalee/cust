"""
-*- coding: utf-8 -*-
Created by lhy on 2020/10/29 14:42
Description:
"""
import pandas as pd
from pyecharts.charts import Sankey
from pyecharts import options as opts
db1 = pd.DataFrame({
    'country':['Italy','Italy','Italy','Italy'],
    'ages':['18岁以下','19-50岁','50-70岁','70岁以上'],
    'confirm':['1677','31394','43617','43139'],
    'Deceased':['167','408','4492','34813'],
    'Active/Recovered': ['1510','30986','39125','8326']
})
#用一个字典嵌套的链表来储存
nodes=[]
for i in range(2):
    values = db1.iloc[:,i].unique()
    for value in values:
        dic={}
        dic['name'] = value
        nodes.append(dic)
nodes.append({'name':'Deceased'})
nodes.append({'name':'Active/Recovered'})

links = []

for i in db1.values:
    dic={}
    dic['source']=i[0]
    dic['target']=i[1]
    dic['value']=i[2]
    links.append({'source':i[0],'target':i[1],'value':i[2]})
    links.append({'source':i[1],'target':db1.keys()[3],'value':i[3]})
    links.append({'source':i[1],'target':db1.keys()[4],'value':i[4]})
print(links)

# 绘图

pic = (
    Sankey().add('',
         nodes,
         links,
         linestyle_opt=opts.LineStyleOpts(opacity = 0.3, curve = 0.5, color = 'source'),
         label_opts=opts.LabelOpts(position = 'top'),
         node_gap = 30,

    )
    .set_global_opts(title_opts=opts.TitleOpts(title = '意大利新冠肺炎病患年龄分布'))
)
pic.render('Italytest.html')
