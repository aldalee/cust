"""
-*- coding: utf-8 -*-
Created by lhy on 2020/12/3 22:40
Description:
"""
# -*- coding: utf-8 -*-
# import numpy
import MySQLdb
import plotly.plotly
import plotly.graph_objs as pg

host = "192.168.21.104"
port = 3306
user = "root"
passwd = "bigdata"
charset = "utf8"
dbname = "spark"
conn = None

try:
    conn = MySQLdb.Connection(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=dbname,
        charset=charset
    )
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("select * from movie;")
    rows = cur.fetchall()
    # rows = numpy.array(rows)
    lists = [[], [], [], []]
    for row in rows:
        lists[0].append(row["years"])
        lists[1].append(row["number"])
    # print(lists)
    # print(lists[0])
    # print(([x[0] for x in lists]))

    date_years = pg.Bar(x=lists[0], y=lists[1], name='年份')
    # barmode = [stack,group,overlay,relative]
    layout = pg.Layout(barmode='group', title="各产品销售情况")
    fig = pg.Figure(data=date_years, layout=layout)
    plotly.offline.plot(fig, filename="test.html")

finally:
    if conn:
        conn.close()