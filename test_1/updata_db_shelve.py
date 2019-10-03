from initdata import tom
import shelve

db = shelve.open('people-shelve')
db['tom'] = tom
# 先要通过键来获取到sue的记录，在内存中对其进行修改
# 然后再重新对建赋值
sue = db['sue']
sue['pay'] *= 1.10
db['sue'] = sue
db.close()
