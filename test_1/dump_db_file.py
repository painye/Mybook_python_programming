from make_db_file import loadDbase
'''将文件中的内容重新载入数据库'''

db = loadDbase()
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
