"""
    实现用来查看和更新保存在shelve中类实例的基于web的界面；
    shelve保存在服务器上（如果是本地机器德华，就是同一个机器）
"""

import cgi, shelve, sys, os           # cgi.test()转储输入


# 调用class-shelve数据库
import html

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')


# form['file']或form[ ' trial ' ]表示一个input标签整体，而标签有属性，如可以通过form['file'].filename或form['file'].file等来获取文件的相关信息，
# 通过form[ ' trial ' ].value来获取text文本框里面的值。
# form是fieldStorage()的实例，代表着解析后的整个前端发来的表单
form = cgi.FieldStorage()               # 解析表单数据
print('Content-type: text/html')        # 响应html中的hdr和空行
# sys.path.insert定义搜索路径的优先顺序，序号从0开始，表示最大优先级，sys.path.insert()加入的是临时搜索路径，程序退出后失效。
# os.getcwd()用于获取当前执行python文件的文件夹,但是返回的是当前python被执行的文件夹，而不是文件所在文件夹
# 也就是说在本程序在上一级的文件中调用，返回的是html文件所在的文件夹，而不是该py文件所在的文件夹，切记
# 总体来说是为了查找当前文件和Person
sys.path.insert(0, os.getcwd())


# 主html模板，提供对key的操作Fetch或者Update
replyhtml = """
    <html>
    <title>People Input Form</title>
    <body>
    <form method=POST action="http://localhost:8081/peoplecgi.py">
        <table>
        <tr><th>Key<td><input type=text name=key value="%(key)s">
        $ROWS$
        </table>
        <p>
        <input type=submit value="Fetch", name=action>
        <input type=submit value="Update", name=action>
    </form>
    </body></html>
"""


# 为$ROWS$的数据行插入html
# rowhtml提供了当前查询的
rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    # 这种方式用符号“%”连接一个字符串和一组变量，字符串中的特殊标记会被自动用右边变量组中的变量替换
    # 使用字符串格式化将来自于记录的属性字典的键值填充到这段文本中
    rowshtml += (rowhtml % ((fieldname,)*3))
# 在replyhtml代码中的$ROWS$中替换为rowshtml
replyhtml = replyhtml.replace('$ROWS$', rowshtml)


# 将字典中的个属性的值转义为HTML字符
def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:                     # 值可能包含&, >等字符
        value = new[field]                      # 作为代码显示： 被引号引起
        # 通过repr将字典的值转换为代码文本
        new[field] = html.escape(repr(value))    # 转义HTML字符
    return new


# 实现查找功能，db为数据库字典， form是解析后的完整的表单,返回有着key中的工作人员的所有信息
def fetchRecord(db, form):
    try:
        # 找到form表单中待查找的'key'键
        key = form['key'].value
        # 将该‘key'记录下来
        record = db[key]
        fields = record.__dict__                # 使用属性字典，fields是字典类的属性字典
        fields['key'] = key                     # 填充响应字符， 将表单中key的value赋给属性字典的key属性
    except:
        # 新建一个字典，键为fieldnames，值都默认为'?'
        fileds = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


# 更新数据库中的内容，所传参数为db数据库和解析后的表单form,返回key的工作人员的消息
def updateRecord(db, form):
    # 如果表单中没有key属性
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    # 如果存在key属性
    else:
        # 从表单中得到key
        key = form['key'].value
        # 在数据库中查询该人员，若有直接添加到查询记录中
        if key in db:
            record = db[key]
        # 如果没有该人员就直接创建对象，并直接将对象送往人员字典信息中
        else:
            from person import Person
            record = Person(name='?', age='?')
            for field in fieldnames:
                setattr(record, field, eval(form[field].value))
        # 将从html中得到的新的用户信息存入数据局中得到更新
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


# db中存储class-shelve数据库中的数据集
db = shelve.open(shelvename)
# action规定了向何处发送表单数据，它的值是一个URL
# form中得到的是一个结果后的表单，如果在改表单中能找到'action'就获取它的action值value见replyhtml代码，否则什么也不干
action = form['action'].value if 'action' in form else None
# 判断action的value值，调用相应的函数
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    # 用于创建并返回一个新的字典。两个参数：第一个是字典的键，第二个（可选）是传入键的值，默认为None。
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing or invalid actoin'
db.close()
print(replyhtml % htmlize(fields))
