# -*- coding: utf-8 -*-
import BasicPractice_2

#词典，与列表类似，词典也可以储存多个元素，这种存储多个元素的对象称为容器
#词典元素包含两部分，键和值。常见以字符串或数字或真值来表示键(不可变的对象可以作键)，值可以是任意对象，键和值两者一一对应
#与表不同的是，词典元素没有顺序，不能通过下标引用元素，词典是通过键来引用
dic = {"danhuiling": 49, "danhuipang": 48, "Roger": 100}
print type(dic)
print dic["danhuipang"]
dic["danhuipang"] = 49
print dic

#构建一个新的空的词典
dic = {}
print dic
#在词典中添加一个新元素
dic["danhuifei"] = 47
print dic

#词典元素的循环调用
dic = {"danhuiling": 47, "danhuipang": 48, "danhuiyuan": 49, "tom": 100}
for key in dic:
    print dic[key]  #通过打印结果可以看出dic是没有顺序的

#词典的常用方法
print dic.keys()        #返回dic所有的键
print dic.values()      #返回dic所有的值
print dic.items()       #返回dic所有的元素(键值对)
del dic["danhuiyuan"]; print dic   #删除dic的danhuiyuan元素
dic.clear(); print dic  #清空dic，dic变为{}
print len(dic)               #查询词典中元素的个数

#文本文件的输入输出
#文本文件的读写主要通过open()所构建的文件对象来实现

#创建文件对象，打开一个文件，并使用一个对象来表示该文件：对象名 = open(文件名，模式)
#常用模式：
#r，打开只读文件，该文件必须存在
#r+，打开可读写的文件，该文件必须存在
#w,打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件
#w+，打开可读写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件
#a，以附加的方式打开只写文件，若文件不存在，则会建立该文件；如果文件存在，写入的数据会被附加到文件尾，即文件原先的内容会被保留
#a+，以附加的方式打开可读写的文件。若文件不存在，则会建立该文件；若果文件存在，写入的数据会被附加到文件尾，即文件原先的内容会被保留
#上述的形态字符串都可以再加一个b字符，如rb、w+b或ab+等组合，加入b字符是用来告诉函数库打开的文件为二进制文件，而非纯文字文件
#f = open("test.txt", "r")

#文件对象的方法

#读取
#content = f.read(N)     #读取N bytes的数据
#ccontent = f.readline() #读取一行
#content = f.readlines() #读取所有行，储存在列表中，每个元素是一行

#写入
#f.write("I love yuanpangzai!\n") #将"I love yuanpangzai!"写入并换行

#关闭文件
#f.close()  #不要忘记关闭文件

#模块
#模块和函数及对象一样，都是为了更好的组织已经有的程序，以方便重复利用。一个.py文件就构成一个模块，通过模块，你可以调用其他文件中的程序

#引入模块
print BasicPractice_2.leapYear(2000, 2, 3)  #import部分在最上面，引入模块后可以通过"模块.对象"的方式来调用引入模块中的某个对象
#Python中还有其他的引入方式
#import a as b              #引入模块a，并将模块a重命名为b
#from a import function1    #从模块a中引入function1对象。调用a中对象时，不用再说明模块，即直接使用function1，而不是a.function1
#from a import *            #从模块a中引入所有对象。调用a中对象时，不用再说明模块，即直接使用对象，而不是a.对象

#搜索路径
#Python会在以下路径中搜索它想要寻找的模块：
    #程序所在的文件夹
    #操作系统环境变量PYTHONPATH所包含的路径
    #标准库的安装路径

#模块包
#可以将功能相似的模块放在同一个文件夹中(例如this_dir)中，构成一个模块包
#import this_dir.module     #引入this_dir文件夹中的module模块，该文件夹中必须包含一个__init__.py的文件，提醒Python，该文件夹为一个模块包，__init__.py可以是一个空文件

#函数的参数传递

#回忆一下函数的参数位置传递
def f(a, b, c):
    return a+b+c
print (f(1, 2, 3))      #在调用f时，1，2，3根据位置分别传递给了a，b，c

#关键字传递
print(f(c=3, b=4, a=5)) #关键字传递是根据每个参数的名字传递参数,不用遵守位置的对应关系
print(f(3, c=3, b=4))   #关键字传递可以和位置传递混用，但位置参数要出现在关键字参数之前

#参数默认值
def f(a, b, c=10):      #给参数c设定默认值
    return a+b+c
print (f(2, 3))         #如果值没有被传递，则使用默认值
print (f(1, 2, 3))      #如果值被传递了，就使用传递的值

#包裹传递
#在定义函数时，有时不能确定调用的时候会传递多少个参数。此时，使用包裹(packing)位置参数，或者包裹关键字参数
#包裹传递的关键，在于定义函数时，在相应元祖或字典前加*或**

#包裹位置参数
def func(*name):        #在func的参数表中，所有的参数被name手机，根据位置合并成一个tuple，这就是包裹位置传递。为了提醒Python参数，name(可以是name以外别的代号)是包裹位置传递所用的tuple名，在定义func时，在name前加*号
    print type(name)
    print name
func(1, 4, 6)
func(5, 6, 7, 8, 9, 1)

#包裹关键字传递
def func(**dict):       #使用dict作为一个字典，收集所有关键字，传递给函数func，在字典名称前(此例为dict)要加**，以表示参数dict是包裹关键字传递所用的字典
    print type(dict)
    print dict
func(a=1, b=9)
func(m=2, n=1, c=11)

#解包裹
#*和**，也可以在调用的时候使用，即解包裹。包裹和解包裹并不是相反的操作，而是两个相对独立的过程
def func(a,b,c):
    print a, b, c
arges = (1, 3, 4)       #所谓解包裹，就是在传递tuple时，让tuple的每一个元素对应一个位置参数
func(*arges)            #在调用func的时候使用*，是为了提醒python，我想把arges拆分成三个元素，分别传递给a，b，c
dict = {"a": 6, "b": 7, "c": 9} #同样也可以对词典进行解包裹
func(**dict)

#混合
#在定义或调用参数是，参数的几种传递方式可以混用，但在过程中要注意前后顺序，基本原则是：先位置，再关键字，再包裹位置，再包裹关键字

#作业
#2. 建立一个record.txt的文档，写入某内容，再从record.txt中读取并打印在屏幕上

f = open("record.txt", "w+")
f.write("I love yuanpangzai!\n" + "I love yuanfeizai!\n")
f.close()

f = open("record.txt", "r+")
content = f.readlines()
for i in range(len(content)):
    print content[i]
f.close()



