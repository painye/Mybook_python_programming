from tkinter import *
from tkinter.messagebox import showinfo

"""
    Frame框架，在屏幕上创建一个矩形区域，多作为容器来布局窗体
    程序现在是一个Frame的子类，它自动成为一个可附加组件，我们可以把这个类创建的所有控件作为一个包添加到其他的GUI中
    只需要把这个Frame绑定到GUI上
"""


class MyGui(Frame):
    def __init__(self, parent=None):
        # 调用父类Frame的构造函数
        Frame.__init__(self, parent)
        # 创建按钮,初始化TK控件实例
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()