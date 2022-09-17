"""
-*- coding: utf-8 -*-
Created by lhy on 2020/10/29 14:39
Description:
"""
from pyecharts import options as opts
from pyecharts.charts import Sankey
node =[{'name': '内蒙古'},
       {'name': '基里巴斯'},
       {'name': '也门'},
       {'name': '古巴'},
       {'name': '喀麦隆'},
       {'name': '多米尼克'},
       {'name': '中非共和国'}]

link =[{'source': '内蒙古', 'target': '中非共和国', 'value': 165000},
       { 'source': '内蒙古', 'target': '也门', 'value': 136200},
       {'source': '内蒙古', 'target': '古巴', 'value': 213000},
       {'source': '内蒙古', 'target': '喀麦隆', 'value': 16560300},
       {'source': '内蒙古', 'target': '基里巴斯', 'value': 2831400},
       {'source': '内蒙古', 'target': '多米尼克', 'value': 101400}]
pic = (
	    Sankey().add('',
       node,
	   link,
       linestyle_opt=opts.LineStyleOpts(opacity = 0.3, curve = 0.5, color = 'source'),
        label_opts=opts.LabelOpts(position = 'right'),
         node_gap = 30,#节点之间的距离,(查看垂直图片的操作orient="vertical")

    ).set_global_opts(title_opts=opts.TitleOpts(title = '通话记录'))
	)
pic.render('sankey2.html')