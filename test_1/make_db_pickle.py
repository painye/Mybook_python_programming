from initdata import db
import pickle

''' 格式化的文件，有较大的局限性，每一次更新需要重写整个数据库
    pickle模块可以将内存中的Python对象转换成序列化的字节流，这是一种可以写入任何类似文件
    对象的字节串。pickle模块可以根据序列化的字节流重新构建原来内存中的对象：转换成原来那个对象
    pickle模块取代了专有的的数据模式。'''

# 使用二进制模式的文件
dbfile = open('people-pickle', 'wb')
# 字节数据而非字符串，将数据库的内容传入新建的文件
pickle.dump(db, dbfile)
dbfile.close()
