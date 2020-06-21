python基础
	警醒格言
		每天努力一点点
		1.01^365 = 37.8
		0.99^365 = 0.03
		积硅步以致千里，积懒惰以致深渊
		1.02^365 = 1377.4
		0.98^365 = 0.0006
	python环境安装
		https://www.python.org/    
			下载，一直下一步
		国外源安装：（比较慢）
		pip install openpyxl
		常用的国内源：
		http://mirrors.aliyun.com/pypi/simple/		阿里云
		https://pypi.mirrors.ustc.edu.cn/simple/		中科大
		https://pypi.tuna.tsinghua.edu.cn/simple		清华
		pip  install  openpyxl  -i   +   url
		pycharm设置作者信息：
file->setting->Editor->File and code templates , python scripts,设置如下：
# -*- coding: utf-8 -*-
********************************
@Time     :${DATE} ${TIME}
@Author   :gaoliang
@Email    :337901080@qq.com
@File     :${NAME}.py
@Software :${PRODUCT_NAME}
********************************
		ipython
			python版本大于3.5
				pip install ipython
		python -V
			查看python版本
	python中的注释
		防止遗忘，增加代码的可读性
		特殊含义（指定编码）
			# -*- coding: utf-8 -*-
		复杂的操作需要添加注释
	python中的变量
		变量类似于便利贴、名称
		可以通过变量找到指向的值
		每个变量在使用之前都必须赋值，变量赋值之后该变量才会被创建
		等号=用来给变量赋值，=左边是变量名，=右边是变量所指向的值
		便利贴和值
		python和C，变量的区别
			python
				a = 1;
a=2;
b=a;
					给a盒子赋值1，a盒子里存放的是1，给a盒子赋值2，a盒子存放的是2；把a赋值给b，相当于给a盒子取别名为b（不会拷贝一份a盒子），此时该盒子既叫a,也叫b
			C
				a=1;
a=2;
int b=a;
					给a盒子赋值1，a盒子里存放的是1，给a盒子赋值2，a盒子存放的是2；把a赋值给b，相当于拷贝一份a盒子给b盒子，再改变复制盒子的名称为b
		变量四要素
			变量名
			变量值
			变量的类型
				用type函数获取
					变量类型由值确定
			变量的地址
				用id函数获取
		标识符
			由字母、数字、下划线组成，且不能以数字开头
			不能与关键字重复
				关键字
					python内部已经使用过的标识符
						import keyword
print(keyword.kwlist)
					具有特殊的含义和功能
			建议不要以内置函数或类重名，不然会覆盖原始内置函数的功能
			常见的变量名、函数名、类名等
			需要见名知意
		变量的命名规则
			每个单词都使用小写字母
			多个单词之间使用下划线（_）连接
			为了可读性，每个赋值号=左右两边空一格
				user_name = 'zhangsan'
		驼峰命名法
			大驼峰命名法
				python中类名使用大驼峰命名法
					UserRegister
	python中的数据类型
		数字类型
			bool
				非0即真
			int
			float
			complex
		非数字类型
			字符串
			列表
			元祖
			字典
			集合
	python中的运算符
		算术运算符
			+、-、*、/、%
			//
				整除
			**
				幂
		比较运算符
			==、!=
			>、>=、<、<=
			结果为bool类型，True or False
				ord('a')
				chr('97')
		逻辑运算符
			and
				x and y
					同真则真，有假则假
			or
				x or y
					有真则真，同假则假
			not
				not x
					取反
		赋值运算符
			=
			+=、-=、*=、/=、%=、//=、**/
		运算符的优先级
			先乘除后加减；同级运算符是从左到右运算
			可以使用小括号调整计算的优先级
		成员运算符
			in
			not in
	python中的字符串
		定义
			是一串字符，用来表示文本数据类型
		表示
			''
			""
			""""""
		字符串的索引
			获取指定位置的元素
				顺序索引
					索引从0开始长度-1
				倒序索引
					从右向左，从-1开始到-长度
		字符串的切片操作
			切片操作适用于字符串、列表、元祖等序列类型
			字符串的索引是左闭右开
			默认步长为1
			开始的0以及结束的-1均可省略，：不可省略
		字符串的内置方法
			string.startswith(str):检查字符串是否以str开头，是则返回True
			字符串包含
				string.isalnum():至少含有1个字符且所有的字符都是字母或数字则返回True
				string.isalpha():至少含有1个字符且所有的字符都是字母则返回True
				string.isdigit(): 只包含数字，返回True    用于判断数字组成的字符串
				string.isupper():
					string中包含至少1个区分大小写的字符，并且所有这些字符都是大写，则返回True
				string.islower():
					string中包含至少1个区分大小写的字符，并且所有这些字符都是小写，则返回True
			查找和替换
				string.startswith(str):检查字符串是否以str开头，是则返回True
				string.endswith(str):检查字符串是否以str结尾，是则返回True
				string.find(str, start=0, end=len(string)):
					检测str是否在string中且在start和end指定范围内，是就返回str开始的索引值，否则返回-1
				string.index(str, start, end):检测str是否在string中且在start和end指定范围内，是就返回str开始的索引值，否则会报错
			大小写转换
				string.upper():将字符串中的所有字母转换成大写字母,不改变原有字符，返回一个新的字符串
				string.lower():将字符串中的所有字母转换成小写字母不改变原有字符，返回一个新的字符串
			文本对齐
				string.center(width) ：返回一个原字符串居中，并使用空格来填充至长度width的新字符串
					'hello world'.center(30, '*')
			去除空白字符或指定字符
				string.strip()  截掉string两边的空白字符  ' hello world '.strip(' ')
					返回一个新的字符串
				string.lstrip() 截掉string左边的空白字符
				string.rstrip() 截掉string右边的空白字符	
			拆分与连接
				string.split(str, num):
					以str为分隔符拆分string，如果num有指定值，则仅分隔成num+1个子字符串
					'/user/bin/env'.split('/')	['', 'user', 'bin', 'env']
					'/user/bin/env'.split('/', 3)	['', 'user', 'bin', 'env']
				string.join(seq):
					以string作为分隔符，将seq中所有的元素合并为1个新的字符串
					list_1 = ['', 'user', 'bin', 'env']
					'/'.join(list_1)	'/user/bin/env'
		格式化输出
			1)format()方法(推荐使用)：
				把含有{}的字符串当作1个模板，通过传入的参数进行格式化
不指定序号，会自动按顺序去匹配{} {}
指定序号去匹配{0} {1}
指定同1个序号去匹配
					print('{2} {0} {3} {1} {2} {0}'.format('be', 'not', 'to', 'or'))
				把含有{}的字符串当作1个模板，通过传入的参数进行格式化
				{:.3}'.format(result)     保留3位有效数字
				输出多个字符:
				print('hello {0},{1} is my favorite language'.format('gaoliang', 'python'))
				{:*^40S}
					居中对齐，并用*填充
			2)格式化操作符(%)
				%s	字符串
%d	有符号十进制整数
%.2f 浮点数，保留小数点后两位
%%	输出%
				print('格式化字符串'  % 变量1)
				print('格式化字符串' % (变量1, 变量2...))	
		嵌套使用
			字符串中包含单引号时，用双引号	
			字符串中包含双引号时，用单引号
			函数注释常用"""	"""
	python中的序列
		定义
			成员有序排列,可通过下标(索引)访问
			不是python中指定的数据类型，仅仅是多种类型所支持的一种操作
		组成
			字符串、元组、列表
		支持的操作
			1.通过索引获取指定位置的元素
			2.切片操作
				[::]
			3.成员关系运算符
				in
				not in
			4.连接运算符(+)
				序列+序列
				必须是同一类型
			5.重复运算符（*）
				序列*数字
			6.循环遍历（for in）
				解释
					从头到尾依次从序列中获取数据，在循环体内部对每一个元素执行相同的操作
				语法格式
					for item in squnence:
    pass
			7.求序列的长度和序列中某个元素出现的个数
				len(序列)
				new_list.count(item)
			8.支持的内置函数
				表示
					函数名(序列)
				组成
					all()
						如果序列的元素都为True,结果为True;否则结果为False
					any()
						序列中只要有一个元素为True,结果为True, 否则结果为Fasle
					enumerate()
						返回一个enumerate对象，返回一个包含序列中每个元素索引和值的元组
					len()
						返回序列的长度
					list()
						将一个可迭代对象转换成元组
					max()
						返回序列中最大的元素
					min()
						返回序列中最小的元素
					sorted()
						返回一个排序后的新序列（原序列不变）
					sum()
						返回序列中所有元素之和
		字符串不可修改，进行相应操作时，会返回一个新的字符串；列表可修改，进行相应操作时，在其本身进行修改
	python中的列表
		表现方式
			空列表
				[]
			非空列表
				[1, 2, 3]
				['Tom', 'Jack', 'Mary']
		相关操作
			求列表的长度
				len(new_list)
			列表排序
				升序
					new_list.sort()
						返回值为None,改变自身
				降序
					new_list.sort(reverse=True)
			列表反转
				new_list.reverse()
			获取列表中的元素
				new_list[index]
			获取某一元素在列表中第一次出现的索引
				new_list.index(item)
			插入元素
				在指定位置插入元素
					new_list.insert(index, new_value)
				在列表末尾插入元素（当追加的元素为序列时，整体追加）
					new_list.append(other_list)
				在列表末尾追加元素（当追加的元素为序列时，单个追加）
					new_list.extend(other_list)
			删除元素
				删除指定索引的元素
					del new_list[index]
					new_list.pop(index)
				删除第一个出现的指定元素
					new_list.remove(item)
				删除末尾元素
					new_list.pop()
			清空元素
				new_list.clear()
	python中的元组
		定义
			不可修改的序列
			元组的元素不可修改，不可增加元素
			一般在元素不可修改的场景下使用
			元组是序列类型，支持序列的所有操作
		表现形式
			空元组
				（）
			含有一个元素的元组
				(1,)
			非空元组
				(1,2,3)
		应用场景
			函数的参数和返回值，一个函数可以接收任意多个参数或者一次返回多个数据
		元组与列表的联系
			列表中保存数据类型相似的数据，元组中保存不同数据类型的数据
			元组为不可变类型，遍历时速度更快
			元组可以做为dict字典的key,列表不可以
		元组和列表之间的转换
			使用list()函数可以把元组转换成列表
			使用tuple()函数可以把列表转换成元组
	python中的字典
		定义
			存储多个数据
			描述一个物体
		语法格式
			{
  key1: value1,
  key2: value2
}
		key值唯一，为不可变类型（可为数字、字符串、元组），值可为任意类型
			python3.7之后字典变为有序的
		创建
			{key1:value1,key2:value2}
			dict([(key1, value1), (key2, value2)])
		常用操作
			取值
				获取字典中所有的key值
					new_dict.keys()
				获取字典中所有的value值
					new_dict.values()
				获取字典中所有的(key, value)元组列表
					new_dict.item()
				取出字典中某个元素,key不存在会报错
					new_dict[key]
				从字典中取值，key不存在返回None
					new_dict.get(key)
			删除
				删除指定的键值对，key不存在会报错
					del new_dict[key]
				删除一个键值对,返回值
					new_dict.pop(key)
				删除字典中最后一个键值对，并返回该键值对
					new_dict.popitem()
			清空字典
				new_dict.clear()
			新增键值对
				new_dict.update(dict_02)
			获取字典中键值对的数量
				len(new_dict)
	python中的条件判断
		流程控制：顺序、分支、循环
		单if条件判断：
			if condition:
    pass
		if-else 条件判断：
			if condition:
    pass
else:
    pass
		if-elif-else条件判断：
			if condition:
    pass
elif condition:
    pass
else:
    pass
	python中的循环
		while循环:   while循环嵌套
			定义：指定的代码重复执行
			语法格式
				while condition:
pass
			特性：
				初始条件：计数器
循环条件：修改计数器
					定义循环变量
					循环条件
					修改循环变量
			循环关键字
				break
continue
			在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
		for 循环
			定义：
				可以遍历任何序列类型  元组、字符串、列表、字典、可迭代对象
				通过遍历对象的长度来控制循环次数（暂时正确）
				遍历完毕，循环即结束
			格式
				for item in iterable:
    pass
			遍历方式
				通过索引来遍历
				通过元素来遍历
			while和for循环的异同点：
				相同点： 重复执行代码
				不同点：
					while: 往往循环次数不确定
					for : 一般循环次数已知，性能更高，推荐使用
			break和continue
				break和continue是专门在循环中使用的关键字
				break:当某一条件满足时，退出循环，不再执行后续重复的代码
				continue:当某一条件满足时，不执行后续重复的代码，开始下一次循环
				break和continue只针对当前循环有效
	python中的函数
		含义
			把具有独立功能的代码块组织成一个小模块，在需要的时候调用
				提高编写的效率、代码的复用
				让程序更小、更模块化
			两个步骤
				定义函数----封装独立的功能
				调用函数----享受封装的成果
		函数格式
			def 函数名():
"""
注释信息
"""
    pass
				函数名称应该符合标识符的命名规则
				:"代表函数头的结束
				def 是英文define的缩写
		函数调试
			pycharm的调试工具
				调试的目的：排错、查看程序的执行顺序
				F7(Step Into):程序会进入到函数或类里面执行
				F8(Step Over):函数或对象直接执行
		函数参数的类型：
			位置参数
				形参和实参一一对应，参数个数一致
			关键字参数
				意义：参数比较多时，不用按顺序传参，为参数指定名称，
				特性：要放在位置参数右侧
			默认参数
				意义：参数取值相对固定，给参数指定默认值，简化函数的调用。
				特性：在形参上指定默认参数  
				默认参数要放在非默认参数右侧 
				实参可以覆盖默认参数
			可变参数
				意义：传入的实参(个数和类型)不确定时使用
				打包
					在函数定义时
						* 的作用：将位置参数组成一个元组，并赋值给args;
						**的作用：将关键字参数组成一个字典，并赋值给kwargs
					注意
						在函数定义时， * 表示打包，在函数体内部， * 表示的却是解包
				解包
					在函数调用时
						*的作用：够将元组或列表解包成不同的参数
						**的作用： 以键/值的形式解包一个字典，使其成为一个独立的关键字参数
				    *args在前，**kwargs在后
				形参为打包，实参为解包
			函数定义时
				位置参数----默认参数----可变参数
			函数调用时
				位置参数----关键字参数
		函数的返回值
			没有return，默认返回None
			有return，返回某个对象或tuple元组
		函数名.__doc__
			查看函数的注释
		Ctrl + Q
			查看函数信息
		Ctrl+P
			查看函数需要传入哪些参数
		修改某个函数里面的参数名称
			shift + F6
		函数的嵌套使用
		局部变量和全局变量(函数外部变量叫做全局变量)
			函数内修改全局变量
				global 全局变量名
全局变量名=value
			先局部-再全局-再模块
		常用内置函数
			range(start, stop, step)
				定义
					生成整数序列
				语法格式
					range(10)
					range(1, 10)
					list(range(10))
				只能取到stop-1的值
				默认从0开始取值
		操作变量并赋值给变量本身
			item = item.strip()
	python中的模块
		意义
			为了提高代码的复用
		清楚
			from  模块  import  函数/类/全局变量
			__all__ = ['print_fac', 'print_num']
from lemom_01_python_base.py_practice import *
			以使用as关键字给其中一个取别名
			多次导入相同的模块，只会导入一次
		原则
			1）每个py文件都应该是可以被导入的
			2）一个独立的python文件就是一个模块
			3）在导入文件时，文件中 所有没有缩进的代码都会被执行一遍
		搜索顺寻
			先在当前目录中查找
				再到系统目录中查找
					最后到sys.path中查找
		实际开发场景
			开发人员 通常会在 模块下方增加测试代码
			仅在模块内使用，而被导入到其他文件中不需要执行
		os模块
			os.getcwd()：显示当前的工作路径，只具体到路径，不具体到文件
			os.path.basename()
				获取当前文件的基类路径
					py_practice.py
			os.path.dirname()
				获取当前文件的路径，不具体到文件或目录
			os.path.join(a, b)：连接两个部分的路径，组成一个完整的路径
			os.path.split(path)：将文件和路径拆分开
			os.mkdir(path)：在某个目录下，创建一个新目录
			os.makedirs(path)：创建多级目录
			os.rmdir(path)：删除一个目录
			os.removedirs(path)：删除多级目录
			os.listdir(path)：获取当前目录下的目录列表
			os.path.isdir(*args, **kwargs)：判断当前文件是否是目录，返回布尔值
			os.path.isfile(path)：判断当前文件是否是文件，返回布尔值
			os.path.exists(path)：判断路径是否存在，返回布尔值
			os.chdir(path)
				修改工作目录
			path为r"\c:bin"
		__name__
			直接运行py文件，__name__等于__main__,
导入py文件（调用），__name__等于路径.模块名
				可以在脚本的逻辑代码前加一句判断，使得被调用是不会执行原脚本的逻辑代码，只允许调用方法
			每一个py运行文件都有
		__file__变量
			__file__表示文件本身
				在pycharm中会自动输出绝对路径
					即print(__file__)
						D:\py_learn_trip\lemom_01_python_base\py_practice.py
				在cmd中执行需要手动将将项目的路径导入环境变量path
					py_practice.py
					即DIR_NAME=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
					sys.path.append(DIR_NAME)
						需要先导入sys模块
		导入规则
			系统模块
				第三方模块
					自定义模块
			定义全局变量
				定义类
					定义函数
			def main():
    pass
				if __name == '__main__':
	   pass
					根据__name__变量判断是否执行下方逻辑代码
	python中的文件
		文件分类
			文本文件
				可以使用 文本编辑器 查看
			二进制文件
				不能使用文本编辑器查看
					如图片文件、音频文件、视频文件
		文件操作流程
			1.打开文件
				2.读、写文件
					3.关闭文件
		文件操作方法
			open("文件名", mode="r")	打开文件，并且返回文件操作对象
			read()	将文件内容读取到内存中
				读取整个文件，返回一个字符串
			write(字符串)	将指定内容写入文件
				无返回值
			close()	关闭文件
			read/write/close 三个方法都需要通过 文件对象 来调用
			readline() 方法可以一次读取一行内容；方法执行后，会把文件指针 移动到下一行，准备再次读取
				读取文件中一行数据，返回一个字符串
				读取到文件末尾，返回空字符串
			readlines()
				读取整个文件，返回一个字符串列表
					['周瑜\n', '诸葛亮\n', '曹操\n', '司马懿']
		打开文件的方式
			file = open(filename, mode='r',encoding='utf-8')
				返回一个文件对象
			r、w、a
		具体事例
			txt1 = open("1.txt", "r", encoding="utf-8")
txt2 = open("2.txt", "w", encoding="utf-8")
while True:
    text = txt1.readline()
    if not text:
        break
    txt2.write(text)
txt1.close()
txt2.close()
	python中的异常
		概念
			在程序运行时，如果python解释器遇到一个错误，就会停止运行，并且抛出一些错误提示信息，这就是异常。
			抛出异常
				程序停止运行并抛出一些错误提示信息
		异常的完整语法格式
			try:
pass （不确定是否能正常运行的代码） 
except 错误类型1:
pass  （针对错误类型1，做相应的代码处理）
expect (错误类型2, 错误类型3)：
pass  针对错误类型2和错误类型3，做相应的代码处理）
except Exception as e:  
print("未知错误：{}".format(e))
else:    无异常时，执行else下的代码
pass
finally:  有无异常时，执行finally下的代码
pass   
	python中的类与对象
		类
			相同特征或者行为的事物的一个统称
				是抽象的，不能直接使用
			特征被称为属性  它是什么样的
			行为被称为方法  它可以做什么
		对象
			对象是由类创建出来的一个具体存在，可以直接使用
			由哪一个类创建出来的对象，就拥有在哪一个类中定义的属性和方法
		类和对象的关系
			类是模板，对象是根据类这个模板创建出来的
			先有类，再有对象
			类只有一个，而对象可以有很多个
			对象拥有类的属性和方法；属性值可能不同
		类的设计
			类的设计分析
				使用面向对象开发前，应该首先分析需求，确定一下，程序中需要包含哪些类
			类的设计要素
				在程序开发中，要设计一个类，通常需要满足以下三个要素	
				类名：
					满足大驼峰命名法
						每一个单词的首字母大写，单词与单词之间没有下划线
				属性
					这类事物具有什么样的特征
				方法
					这类事物具有什么样的行为
			确定类名
				名词提炼法，分析整个业务流程，出现的名词，通常就是要找的类
			确定属性和方法
				对对象的特征描述，通常可以定义为属性
				对象具有的行为（动词），通常可以定义为方法
			实例
				一条灰色的狗狗叫旺财
				看到陌生人会汪汪叫
				看到亲人会摇尾巴
			提取
				类名：狗
				属性
					颜色：灰色；姓名：旺财
				方法
					汪汪叫和摇尾巴
		类的理解
			构造方法
				self.hair='大波浪'
					设置属性
				self.name
					获取属性
				self.name=name
					创建属性
				实例化对象时，会自动调用构造方法
			实例方法的调用
				类内部
					self.实例方法名(参数)
				类外部
					对象.实例方法名(参数)
				当通过对象调用实例方法时，会将对象本身当成一个参数传递给实例方法
			方法的定义
				运行程序时，自动从上到下加载程序
			__str__方法
				打印对象时会调用
				必须return一个字符串
			isinstance(object, classname)
				判断一个对象是否属于某个类
			身份运算符
				定义
					身份运算符用于比较两个对象的内存地址是否一致   ---  是否是对同一个对象的引用
				运算符
					is
					is not
				实例
					is是判断两个标识符是不是引用同一个对象
						x is y,类似id(x) == id(y)
					is not是判断两个标识符是不是引用不同对象
						 is not y,类似id(x) != id(y)
				is 与 == 区别
					is 用于判断两个变量 引用对象是否为同一个
					== 用于判断引用变量的值是否相等
				引用
					one_list = [1,2, 3];two_list=[1,2,3];
						one_list is two_list  
							结果为false
					one_list = [1,2, 3];two_list=one_list;
						one_list is two_list  
							结果为True
								引用
						Python参数传递采用的肯定是“传对象引用”的方式。，这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值——相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象——相当于通过“传值’来传递对象
					 函数的传递引用
						def eggs(someParameter):
    someParameter.append('hello list')
 
spam=[1,2,3,4]
eggs(spam)
print(spam)
					变量是对象的一个引用
						a = 1;
a = 2;
b = a;
							赋值操作 = 就是把一个名字绑定到一个对象上。就像给对象添加一个标签。
			属性和方法
				类属性与类方法
					类属性就是针对类定义的属性
						类属性用于记录与这个类相关的特征
							不会记录具体对象的特征
						所有对象的共同特征
							固定的
						类属性名=属性值
					类方法就是针对类定义的方法
						在类方法内部可以直接访问类属性或者调用其它的类方法
						修改、获取类属性
					语法
						@classmethod
def 类方法名(cls):
pass
					类方法需要用修饰器@classmethod来标识，告诉解释器这是一个类方法
类方法的第一个参数应该是cls
由哪一个类调用的方法，方法内的cls就是哪一个类的引用
cls这个参数和实例方法的第一个参数是self类似
				静态方法
					定义
						不使用类的属性，定义成一个静态方法
					语法
						@staticmethod
def 类方法名():
    pass
		类的继承
			概念
				子类继承父类的所有属性和方法(不包括私有方法）
			语法
				class 类名(父类):
 pass
			重写
				概念
					对父类的方法进行重写
				被调用时
					首先检查自身有没有这个方法，如果没有就去父类查找
			拓展
				 def __init__(self, name, age, color, job):
        # 先调用父类的构造方法，创建name, age, color这三个属性，然后再添加一个job属性
        # 对父类的拓展，java中叫做派生
        super().__init__(name, age, color)
         self.job = job
				def eat(self):  # 拓展
        super().eat()
        print("{}吃蟠桃".format(self.name))
				在父类方法的基础上进行修改
			Diagrams	
				查看继承关系
				查看继承的属性和方法