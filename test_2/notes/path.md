# Sys
	sys包括富含信息的名称，也包括完成具体工作的函数，例如可以告诉我们底层操作系统名称

## 模块搜索路径
	- sys模块可以使我们在python程序内部或者交互地查看模块搜索路径。
	- sys.path是一个由目录名称字符串组成的列表，每个目录名称字符串代表正在运行的Python
	  解释器的真正的搜索路径。
	- sys模块导入时，python会从左向右扫描列表，在列表中的每个目录下搜索模块文件
	- sys.path列表在解释器启东市根据PYTHONPATH设置进行初始化
	- sys.path,可以被当做普通列表进行更改（append、extend、insert、pop、remove、del)
	  但是对sys.path的更改只维持到Python进程结束时，每次重新启动新的Python程序或会话时
	  都必学重新设定
	- 需要注意的是sys.path设置代码中使用了原始字符串常量。python使用\\来表示\。

## 已加载模块表
	sys模块还包括嵌入解释器的钩子。sys.modules是一个字典，Python进程所导入的每一个模块在
	其中都有一个name:module项

		>>> sys.modules['sys']
		<module 'sys' (built-in)>

	我们可以使用这个钩子来编写程序，让程序显示或处理某个程序加载的所有模块(对sys.modules进行迭代)还可以通过sys.getrefcount来查看对象的引用次数。


