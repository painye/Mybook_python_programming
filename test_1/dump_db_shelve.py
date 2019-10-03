import shelve

'''
    这里仍是一个字典的字典， 但最顶层的字典实际上是映射到文件的shelve，当通过键来访问记录时
    其内部会使用pickle来序列化或反序列化记录，外面以一个通过键访问的文件作为接口。你也可以认为他就是一个持久化的字典'''

db = shelve.open('people-shelve')
for key in db:
    print(key, "=>\n", db[key])
print(db['sue']['name'])
db.close()