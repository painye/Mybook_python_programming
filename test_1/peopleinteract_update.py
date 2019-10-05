# 交互式更新,对文件中的人员信息进行修改，或者添加新的人员信息
import shelve
from person import  Person

fieldnames =('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    # 回车退出循环
    if not key:
        break
    # 如果元组（人员信息表）中有该人员，读取信息
    if key in db:
        record = db[key]
    # 如果没有该人员则新建一个对象，并传入参数
    else:
        record = Person(name=key, age='?')
    # 对待改人员的各项信息进行遍历，修改
    for field in fieldnames:
        currval = getattr(record, field)
        # 显示的打印出待改人员的待改信息，并输入新的信息
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            print('\t\t\t修改后的信息：\n\t\t\t[{}]={}'.format(field, newtext))
            c = input('\t\t\t请再次确认您是否要进行修改\n\t\t\t\t(y/n)')
            if c == 'y':
                # 为record对象的field属性赋值为eval(newtext)
                if field == 'job':
                    setattr(record, field, newtext)
                else:
                    setattr(record, field, eval(newtext))
    db[key] = record
db.close()