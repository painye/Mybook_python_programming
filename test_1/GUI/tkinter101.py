from tkinter import *
from tkinter.messagebox import  showinfo


def reply():
    showinfo(title='popup', message='Button pressed!')


# 创建一个主控件
window = Tk()
# 创建一个按钮，标题press，功能是reply函数的功能
# command中只给出了函数的名字，没有给所需要的函数参数所以不会调用只是指定了功能函数
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()