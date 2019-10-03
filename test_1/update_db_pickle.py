import pickle

# 将文件的内容导向数据库
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

# 对数据库的内容进行修改
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

# 将修改后的数据库重新存入文件中
dbfile = open('people-pickle', 'wb')
# 注意这里是将整个数据库的内容都重新写入了文件
pickle.dump(db, dbfile)
dbfile.close()

