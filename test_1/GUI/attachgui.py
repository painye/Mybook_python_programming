from tkinter import *
from tkinter102 import MyGui

# 应用主窗口
mainwin = Tk()
# 为mainwin创建一个文本为__name__的标签，并应用布局管理器
Label(mainwin, text=__name__).pack()

# 弹出窗口
# 实例化(顶级窗口),类似于弹出窗口，具有独立的的窗口属性（如标题栏，边框）
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
# 将导入的实例popup作为父容器显示地传入构造函数当中，单按钮控件包附加到了父容器的右边。
MyGui(popup).pack(side=RIGHT)
# "press"按钮是附加上去的自定义Frame
mainwin.mainloop()