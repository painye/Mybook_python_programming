""""
    实现一个图形界面，用于查看和更新存储于shelve中的类实例
    该shelve保存在脚本运行的机器上，可能是一个或多个本地文件
"""

from tkinter import *
from tkinter.messagebox import showerror
import shelve
from person import Person

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')


# 查找键的功能
def fetchRecord():
    key = entries['key'].get()      # 先获得待找人员
    # 如果有这个人将信息存入record
    # 如果没有则调用showerror错误·
    try:
        # 使用键获取数据并在GUI中展示，具体的显示在entries[filed].insert()方法
        record = db[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            # 删除原来的信息
            entries[field].delete(0, END)
            # 在0位置上插入record对象的field属性，这里相当于我直接输入了，并显示了这些字符串到文本
            entries[field].insert(0, repr(getattr(record, field)))


# 修改或添加功能
def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        # 如果entries[filed]为空，则eval会出错，先判断其是否为空
        if entries[field].get():
            setattr(record, field, eval(entries[field].get()))
    db[key] = record


def makeWidgets():
    global entries
    window = Tk()
    window.title('people-shelve')
    # form 是一个以window为父控件的自由附加包
    form = Frame(window)
    form.pack()
    entries = {}
    # enumerate是枚举的意思，该函数能让一个可迭代的迭代器组成一个索引序列，可以通过该函数得到索引与其对应的值
    # ix就是索引，lable是值
    for (ix, label) in enumerate(('key',) + fieldnames):
        # 标签设置布局
        lab = Label(form, text=label)                       # 给window创建一个文本为label的标签
        ent = Entry(form)                                   # 使用Entry控件获得用户输入并显示
        # grid是一个布局管理器与pack相似
        lab.grid(row=ix, column=0)                          # 在控件window的第ix行第0列上是标签
        ent.grid(row=ix, column=1)                          # 在控件window的第ix行第1列上是输入
        entries[label] = ent                                # 获取用户输入的字符串的ent对象，并在entries中创建label与该字符串的键值对

    # 按键设置与布局
    Button(window, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window


if __name__ == '__main__':
    db = shelve.open(shelvename)
    window = makeWidgets()
    window.mainloop()
    db.close()
