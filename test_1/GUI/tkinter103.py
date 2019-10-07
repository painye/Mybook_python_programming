from tkinter import *
from tkinter.messagebox import showinfo

"""
     Entry 是Tkinter 用来接收字符串等输入的控件. 该控件允许用户输入一行文字. 如果用户输入的文字长度长于Entry 控件的宽度时, 
    文字会向后滚动. 这种情况下所输入的字符串无法全部显示. 点击箭头符号可以将不可见的文字部分移入可见区域. 如果你想要输入多行文本
    , 就需要使用Text 控件.
"""


def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)


top = Tk()
top.title('Echo')

Label(top, text="Enter your name:").pack(side=TOP)
# 创建一个Entry控件，top作为父容器
ent = Entry(top)
# 除去标签之后的top位置
ent.pack(side=TOP)
# 输入的name由ent实例的get方法得到
# 使用lambda来延迟对reply函数的调用，使得输入数据得以传入，如果不使用lambda，reply函数会在创建按钮时就进行了调用
btn = Button(top, text="Submit", command=lambda: (reply(ent.get())))
btn.pack(side=RIGHT)
top.mainloop()