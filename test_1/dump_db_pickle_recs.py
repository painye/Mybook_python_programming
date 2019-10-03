import glob
import pickle

# glob模块能根据文件扩展名获得当前目录下所有该扩展名的文件
for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    # 将文件反序列化
    record = pickle.load(recfile)
    print(filename, '=>\n', record)

recfile = open('sue.pkl', 'rb')
record = pickle.load(recfile)
print(record['name'])
