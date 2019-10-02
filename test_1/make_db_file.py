from initdata import db
import sys

dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'


# 保存文件
def storeDbase(db, dbfilename=dbfilename):
    """将数据库格式化保存为普通文件"""
    dbfile = open(dbfilename, 'w')
    for key in db:
        # 该语句类似于dbfile.write(key+'\n')
        print(key, file=dbfile)
        # 遍历字典中的每一个键值对，将其写入文件
        for (name, value) in db[key].items():
            # repr()和``做的是完全一样的事情，它们返回的是一个对象的“官方”字符串表示，
            # 也就是说绝大多数情况下可以通过求值运算（使用内建函数eval()）重新得到该对象。
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def loadDbase(dbfilename=dbfilename):
    """解析数据，重新构建数据库"""
    dbfile = open(dbfilename)
    # 标准输入文件，以文件dbfile作为输入流
    sys.stdin = dbfile
    # 将数据库的内容存储在db这个变量中
    db = {}
    # key代表最外层的字典，即人员
    key = input()
    while key != ENDDB:
        rec = {}
        # 读入第二层字典，人员的信息
        filed = input()
        while filed != ENDREC:
            # 该层循环遍历人员信息字典中的每一个键值对
            name, value = filed.split(RECSEP)
            rec[name] =eval(value)
            filed = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    storeDbase(db)
