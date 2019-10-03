import pickle

# 找到想要修改的记录对应的文件，将记录加载成数据结构
suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

tomfile = open('tom.pkl', 'rb')
tom = pickle.load(tomfile)
tomfile.close()

# 修改数据的内容，并仅将修改后的记录存在文件中
sue['pay'] *= 1.10
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()

tom['name'] = 'Tom Tom'
tomfile = open('tom.pkl', 'wb')
pickle.dump(tom, tomfile)
