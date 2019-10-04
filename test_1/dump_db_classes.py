import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>', db[key].name, db[key].pay)


# 这里不需要重新导入Person类来让shelve获取它的实例或者运行他们的方法
# 当实例存储在shelve文件或pickle中时，底层的pickle会记录下实例的属性以及足够的信息
# 以便于接下来它们被读取时可以自动的定位它们的类。
bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())