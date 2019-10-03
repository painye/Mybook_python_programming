from initdata import bob, sue
import shelve

'''shelve自动地将对象进行pickle进和pickle出键访问文件系统。
因为他是用键访问被存储记录，所以不需要手动的为每条记录管理一个普通文件
shelve系统自动分隔存储记录，并且只获取和更新被访问和修改的记录

shelve接口就像pickle一样简单：与字典相同，只增加了open和close调用

'''

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()

