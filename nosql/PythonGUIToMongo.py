from tkinter import *
import hashlib
import time
from pymongo import MongoClient
conn = MongoClient('192.168.21.101', 27017)
db = conn.MongoGUI
LOG_LINE_NUM = 0
class MY_GUI(object):
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
    # 设置窗口
    def set_init_window(self):
        # 窗口名
        self.init_window_name.title("文本处理工具_v1.2")
        # 1068 681为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        # 标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        # 文本框
        # 原始数据录入框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        # 处理结果展示
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        # 日志框
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮
        # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)
        self.str_trans_to_md5_button.grid(row=1, column=11)
    # 功能函数
    def str_trans_to_md5(self):
        t = self.init_data_Text.get(1.0, END).replace("\n", "")
        src = t.strip().replace("\n", "").encode()
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                # 用提供的字节串更新此哈希对象(hash object)的状态
                myMd5_Digest = myMd5.hexdigest()
                # 返回摘要值,以十六进制字节串的形式
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success", t, myMd5_Digest, "info")
                # 给insert传参数
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed", src, '', "error")
            # 给insert传参数

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time
    # 日志动态打印并写入数据库函数
    def write_log_to_Text(self, logmsg, input_to_mongo, output_to_mongo, result):
        mycol = db['log']  # 插入pgrthree数据库的log集合（没有这个集合会自动创建）
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)
        # 进行数据插入操作
        dict = {"input": input_to_mongo, "output": output_to_mongo, "time": str(self.get_current_time()), "result": result, "log": logmsg_in}
        insert_data = mycol.insert_one(dict)
        print(insert_data)
def gui_start():
    # 实例化出一个父窗口
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    init_window.mainloop()
gui_start()
