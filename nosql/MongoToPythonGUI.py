import tkinter as tk
from tkinter import ttk
from tkinter import *
from pymongo import MongoClient

LINE_NUM = 0
conn = MongoClient('192.168.21.101', 27017)
db = conn.MongoGUI
win = tk.Tk()
win.title("查询工具")
# 添加标题
win.geometry('840x340+10+10')
label1 = ttk.Label(win, text="请选择", font="tahoma 12 normal")
label1.grid(column=1, row=0)


# 添加一个标签，并将其列设置为1，行设置为0# button被点击之后会被执行
def clickMe():
    # 当acction被点击时,该函数则生效显示当前选择的数
    mycoll = db['log']
    query1 = {"result": "info"}
    query2 = {"result": "error"}
    print(numberChosen.current())
    # 输出下所选的索引
    if LINE_NUM <= 9:
        if numberChosen.current() == 0:
            # 判断列表当前所选是第几个
            label1.config(text="查全部")
            # 注意，上面的label1如果直接.grid会出错
            resultTxt.delete('1.0', 'end')
            for find_all in mycoll.find():
                dict0 = "转换后结果:\t" + find_all["output"] + "\t转换日期:" + find_all["time"] + "\n"
                resultTxt.insert(END, dict0)
        if numberChosen.current() == 1:
            label1.config(text="查转换成功")
            resultTxt.delete('1.0', 'end')
            for find_success in mycoll.find(query1):
                dict1 = "转换后结果:\t" + find_success["output"] + "\t转换日期:" + find_success["time"] + "\n"
                resultTxt.insert(END, dict1)
        if numberChosen.current() == 2:
            label1.config(text="查转换失败")
            resultTxt.delete('1.0', 'end')
            for find_failed in mycoll.find(query2):
                if len(find_failed["output"]) == 0:
                    find_failed["output"] = "NULL"
                    dict2 = "转换后结果:" + find_failed["output"] + "\t转换日期:" + find_failed["time"] + "\n"
                    resultTxt.insert(END, dict2)
    else:
        resultTxt.insert(END, "操作失败！")


# 结果显示标签
result_label = tk.Label(win, text="查询结果", font="tahoma 12 normal")
result_label.grid(row=0, column=4)
# 查询结果显示文本框
resultTxt = tk.Text(win, width=108, height=16)
resultTxt.grid(row=1, column=5, columnspan=10)
# 按钮
# 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
# 设置其在界面中出现的位置  column代表列   row 代表行# 下拉选框
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = ["全部查询(all)", "转换成功(info)", "转换失败(error)"]  # 设置下拉列表的值
numberChosen.grid(column=1, row=1)
# 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)
# 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
win.mainloop()  # 当调用mainloop()时,窗口才会显示出来
