import pickle
'''使用pickle模块的字节流文件，将文件中的内容重新载入数据库中'''

dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])