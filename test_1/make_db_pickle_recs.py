from initdata import bob, sue, tom
import pickle
'''
    每当需要更新文件的时候，需要重新读出和写入整个数据库，本程序则是将每一条记录都使用一个pickle文件'''

# 便利的迭代器是由，元组组成的列表，其中元组中的元素是字典的名字和对应字典
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()