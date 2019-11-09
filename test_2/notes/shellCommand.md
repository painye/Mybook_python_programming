# 在脚本里运行shell命令
	os.system 					在python脚本中运行shell命令
	os.popen 					运行shell命令并与其输入或输出流相连接


## shell命令是什么
 	- shell是： 计算机上读取和运行命令行字符串的系统， 而shell命令则代表在shell提示符后输入的命令行字符串


## 运行shell命令
	os模块的system和popen调用使得python脚本可以运行底层系统shell可以理解的任何命令。
	：

		>>> import os
		>>> os.system('dir \dell')
		 驱动器 C 中的卷是 OS
		 卷的序列号是 C064-1496

		 C:\dell 的目录

		2017/10/07  20:10    <DIR>          .
		2017/10/07  20:10    <DIR>          ..
		2017/10/07  20:10    <DIR>          UpdatePackage
		               0 个文件              0 字节
		               3 个目录 64,167,489,536 可用字节
		0
		>>> os.system('type hello.py')
		系统找不到指定的文件。
		1

	这里第一条命令末尾的0只是系统调用本身的返回值（他的退出状态一般用0表示运行成功）命令输出的结果通常会显示在python会话和程序的
	标准输出流中


## 与shell命令进行通信
	os.system函数只是简单地执行一条shell命令行，但os.open还会连接到命令的标准输入\输出流；我们将得到一个类似文件的对象，他默认
	与命令的输出相连接（向popen传入w模式标志符则与命令的输入流相连接）。借助这个对象可以读取popen所派生的命令的输出结果，从而在输
	命令行之后拦截那些在正常情况下将出现在控制窗口中的文本。
	：

		>>> open('hello.py').read()
		'# a python program\nprint("hello world");'

		>>> text = os.popen('type hello.py').read()
		>>> text
		'# a python program\nprint("hello world");'

		>>> listing = os.popen('dir notes').readlines()
		>>> listing
		[' 驱动器 C 中的卷是 OS\n', ' 卷的序列号是 C064-1496\n', '\n', ' C:\\Users\\dell\\Desktop\\thePython\\Mybook_python_programming\\test_2\\notes 的目录\n', '\n', '2019/
		11/09  16:08    <DIR>          .\n', '2019/11/09  16:08    <DIR>          ..\n', '2019/11/09  16:06             4,619 os.md\n', '2019/11/09  16:03             1,383 p
		ath.md\n', '2019/11/09  16:08                 0 shellCommand.md\n', '               3 个文件          6,002 字节\n', '               2 个目录 64,164,413,440 可用字节\
		n']

	通过阅读dir命令的输出结果，我们可以获取目录中的文件列表，进而对这个列表进行迭代处理。

	一些基本的DOS命令可以运行我们能够在shell提示符输入的任何命令，所以他也可以用来启动其他python脚本
	：
		>>> os.system('python  hello.py')
		hello world
		0
		>>> out=os.popen('python hello.py').read()
		>>> out
		'hello world\n'


## 替代方案: Subprocess模块
	subprocess模块可以实现与os.system和os.popen相同的效果，他要求代码较多，但对流的连接和使用提供更完善的控制，适合连接方式复杂的流
	：

		>>> import subprocess 								#类似于os.system()
		>>> subprocess.call('python hello.py')
		hello world
		0
		>>> subprocess.call('cmd /c"type hello.py"')    	#类似于内建shell命令
		# a python program
		print("hello world")0
		>>> subprocess.call('type hello.py', shell=True)    #相当于内建函数
		# a python program
		print("hello world")0

	- windows下，需要将shell= true传递给call等subprocess工具和popen工具，才能运行shell内建命令

	模拟os.popen函数在脚本中运行shell命令并获取其标准输出文本
	：

		>>> pipe = subprocess.Popen('python hello.py', stdout=subprocess.PIPE)
		>>> pipe.communicate()
		(b'hello world\r\n', None)
		>>> pipe.returncode
		0
	
	这里将stdout流与管道连接起来，然后用pipe.communicate()来运行命令并接收他的标准输出流和错误流文本；运行完成之后
	命令的退出状态可作为属性来查看。或者，我们可以用其它接口直接读取命令的标准输出流文本，然后等待命令退出（返回退出状态）
	：

		>>> pipe = subprocess.Popen('python hello.py', stdout=subprocess.PIPE)
		>>> pipe.stdout.read()
		b'hello world\r\n'
		>>> pipe.wait()
		0

	实际上， os.popen函数hesubprocess.Popen对象之间存在直接的映射关系
	：

		>>> from subprocess import Popen, PIPE
		>>> Popen('python hello.py', stdout=PIPE).communicate()[0]
		b'hello world\r\n'
		>>>
		>>> import os
		>>> os.popen('python hello.py').read()
		'hello world\n'


## shell命令的局限
	- system和popen两个函数具有非常好的可移植性， 但真正的可移植程度取决于所运行的命令。例如dir和type shell
	  命令只在windows下有效

	- 调用两个函数时，他们必须在你的操作系统中启动完全不同的独立程序（他们通常在新进程里执行这些命令）。


## os模块导出的其他工具
	os.environ  						获取和设置shell环境变量
	os.fork 							在类Unix系统下派生新的子进程
	os.pipe 							负责程序间通信
	os.execlp 							启动新程序
	os.spawnv 							启动带有底层控制的新程序
	os.open 							打开基于底层描述符的文件
	os.mkdir 							创建新的目录
	os.mkfifo 							创建新的命名管道
	os.remove 							根据路径名删除文件
	os.walk 							将函数或循环应用于整个目录树的各部分


