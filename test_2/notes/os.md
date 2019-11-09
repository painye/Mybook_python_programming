# os模块。
	包含了在C程序和shell脚本中经常用到的所有操作系统的调用。准确的说该模块提供了POSIX工具
	操作系统调用的跨平台移植标准，以及不依赖平台的目录处理工具，如Os.path。os基本上作为计算机系统调用的可移植接口来使用。

## os模块中的工具
	Shell变量			os.environ
	运行程序				os.system, os.open, os.execv, os.spawnv
	派生进程				os.fork, os.pipe, os.waitpid, os.kill
	文件描述符，文件锁		os.open, os.read, os.write
	文件处理				os.remove, os.rename, os.mkfifo, os.mkdir, os.rmdir
	管理文件				os.getcwd, os.chdir, os.chmod, os.getpid, os.listdir, os.access
	移植工具				os.sep, os.pathsep, os.curdir, os.path.split, os.path.join
	路径名工具			os.path.exists('path'), os.path.isdir('path'), os.path.gatsize('path')

## 管理工具

		>>> os.getpid()
		3340
		>>> os.getcwd()
		'C:\\Users\\dell\\Desktop\\thePython\\Mybook_python_programming\\test_1'
		>>> os.chdir("c:\\Users")
		>>> os.getcwd()
		'c:\\Users'

	os.getpid函数给出调用函数的进程的ID（这是系统为当前运行程序定义的唯一标志符，可用于进程控制和唯一命名）
	Os.getcwd则返回当前的工作目录。

## 可移植的常量
	os模块导出了一组用于建华跨平台编程的名称，包括与具体平台相关的路径和目录分隔符、父目录、当前目录指示器、换行符。

		>>> os.pathsep, os.sep, os.pardir, os.curdir, os.linesep
		(';', '\\', '..', '.', '\r\n')

	os.sep是python底层运行平台所采用的目录组分割符号，Windows下预设为"\", POSIX计算机则是"/"
	os.pathsep提供用于在目录列表中分隔目录的字符，windows使用";"。

	dirpath在windows中是dir\dir，Linux中是dir/dir，在Macs上是dir:dir,但dirpath.split(os.sep)的调用可以将平台相关的目录分解

## 常见os.path工具
	- 内嵌的os.path模块提供了一套目录处理的相关工具，例检查文件类型(isdir, isfile)，测试文件是否存在(exists)， 以及通过文件名获得文件的大小(   getsize)

		>>> os.path.isdir("C:\\Users"), os.path.isfile("C:\\users")
		(True, False)

	- 我们还能得到用于分割和合并目录路径字符串的函数，他们会自动应用Python所在的底层平台的目录命名管理

	 	>>> os.path.split("C:\\users\\del\\Desktop")
		('C:\\users\\del', 'Desktop')
		>>> os.path.join("C:\\U", "my.text")
		'C:\\U\\my.text'
		>>> name="C:\\users\\name\\my\\my.text"
		>>> os.path.dirname(name),os.path.basename(name)
		('C:\\users\\name\\my', 'my.text')
		>>> os.path.splitext(name)
		('C:\\users\\name\\my\\my', '.text')

	os.path.split将文件名从目录路径中剥离， os.path.join将他们合并。
	diranme和basename调用反回了split返回结果的前两项
	splitext则剥离了文件的扩展名。

	- split和join方法可以达到与os.sep相同的作用，但还是有差别

		>>> os.sep
		'\\'
		>>> name="C:\\users\\name\\my\\my.text"
		>>> os.path.split(name)                     #返回的是一个元组
		('C:\\users\\name\\my', 'my.text')
		>>> name.split(os.sep)                      #返回的是一个列表
		['C:', 'users', 'name', 'my', 'my.text']
		os.sep.join(name.split(os.sep))
		'C:\\users\\name\\my\\my.text'
		>>> os.path.join(*(name.split(os.sep)))     #Join调用要求传入多参数(*)
		'C:users\\name\\my\\my.text'

	- abspath可移植的返回文件的完整目录路径名。负责将当前目录添加为前缀以及处理..父目录句法等

		>>> os.path.join(*(name.split(os.sep)))
		'C:users\\name\\my\\my.text'
		>>> os.chdir("C:\\users")
		>>> os.getcwd()
		'c:\\Users'
		>>> os.path.abspath("dell")          
		'c:\\Users\\dell'                           #扩展为当前工作目录下的完整路径名
		>>> os.path.abspath("dell\\desktop")        #相对于当前工作目录的不完整路径
		'c:\\Users\\dell\\desktop'

		>>> os.path.abspath('')                     #空字符串代表当前工作目录
		'C:\\users'

		>>> os.path.abspath('.')                    #当前工作目录
		'C:\\users'                                 
		>>> os.path.abspath('..')					#上一级工作目录
		'C:\\'
		>>> os.path.abspath('..\windows')       	#扩展相对路径句法
		'C:\\windows'

		当基于GUI的程序通过单击文件管理器中的图标或桌面快捷方式来启动时，程序的执行路径为被单击文件的主要目录，
		可以用abspath方法吧文件的绝对路径打印出来。







