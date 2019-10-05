"""
    实现简单的交互式循环， 允许用户通过键来查询shelve中记录的对象
"""

import shelve

fieldnames = ('name', 'age', 'job', 'pay')
maxfiled = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? =>')
    # 如果键入空行，则退出
    if not key:
        break

    try:
        # record 是一个对象
        record = db[key]
    # 捕捉全部的异常
    except:
        print('No such key "%s"!' % key)
    # 一段只有在安全的情况下才会运行的代码块
    else:
        for filed in fieldnames:
            # max获取了四个字段的最大长度，作为ljust函数左对齐的域宽
            # getattr函数获得record对象的filed属性
            print(filed.ljust(maxfiled), '=>', getattr(record, filed))
