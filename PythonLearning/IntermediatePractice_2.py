# -*- coding: utf-8 -*-

#循环设计

#range()
#在Python中，for循环后的in跟随一个序列的话，循环每次使用的是序列元素，而不是序列的下标
#range()对循环的控制
s = "danhuilingshiyuanzai"
for i in range(0, len(s), 2):       #用i作为s的下标来控制循环，range()函数的三个参数分别定义了：上限，下限和每次循环的步长，这就与c语言的for循环类似了
    print s[i]

#enumerate()，可以再每次循环中同时得到下标和元素
s = "danhuilingshifeizai"
for (index, char) in enumerate(s):      #实际上，enumerate()在每次循环中，返回的是一个包含两个元素的tuple，两个元素分别赋予index和char
    print index
    print char

#zip()，有多个等长的序列，每次循环在各序列中分别取出一个元素，来自不同列表的元素合成一个tuple，合并后的tuple放入zip()返回的列表中。zip()函数起到了聚合列表的作用
ta = [1, 2, 3]
tb = [4, 5, 6]
tc = ["x", "y", "z"]
for (a, b, c) in zip(ta, tb, tc):       #每次循环时，从各个序列从左到右取出一个元素，合并成一个tuple，然后tuple的元素赋予给a,b,c
    print (a, b, c)

zipped = zip(ta, tb)        #聚合列表
print zipped

na, nb = zip(*zipped)       #分解聚合后的列表
print na, nb

#二、循环对象，正在成为循环的标准形式

#1. 什么是循环对象
#循环对象是一个对象，包含有一个next()方法，此方法的目的是进行到下一个结果，而在结束一系列结果之后，举出StopIteration错误
#当一个循环结构(比如for)调用循环对象时，他就会在每次循环的时候调用next()方法，直到StopIteration出现，for循环接收到，就知道循环已经结束，并停止调用next()
f = open("loopObject.txt", "w+")
f.write("I love yuanpangzai!\n" + "I love yuanfeizai!\n" + "I love danhuipang!\n")
f.close()
#f = open("loopObject.txt")     #open()返回的实际上是一个循环对象，其包含有next()方法，而该方法每次返回的就是新的一行的内容，在到达文件结尾时举出StopIteration，这样就相当于手工进行了循环。
#print f.next()
#print f.next()
#etc
for line in open("loopObject.txt"):     #for结构自动调用next()方法，将该方法的返回值赋予给line，循环知道出现StopIteration的时候结束。
    print line
f.close()
#相对于序列，用循环对象的好处在于：不用再循环还没开始的时候，就生成好要使用的元素。所使用的元素可以在循环过程中逐次生成。节省空间，提高效率，更加灵活

#2. 迭代器
#从技术上说，循环对象和for循环之间还有一个中间层，就是要将循环对象转换成迭代器(Iterator)。这一转换是通过使用iter()函数实现的。但从逻辑层面上，常常可以忽略这一层，所以循环对象和迭代器常常相互指代对方

#3. 生成器
#主要目的：构成一个用户自定义的循环对象
def gen():          #写法与定义函数类似，只是在return的地方都改为yield。
    a = 100
    yield a         #可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。
    a = a*8
    yield a         #再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield
    yield 1000
#生成器自身又构成一个循环器，每次循环使用一个yield返回的值。如上例的生成器共有3个yield，如果用作循环器时，会进行三次循环。
for i in gen():
    print i

def gen():
    for i in range(4):
        yield i

G = (x for x in range(4))   #这是一个生成器表达式，是上面生成器的简写方式

#4. 表推导
#表推导是快速生成表的方法，它的语法简单，很有实用价值
L = []                  #普通方法生成一个list
for x in range(10):
    L.append(x**2)

L = [x**2 for x in range(10)]       #这是一个表推导的方式，是上面list生成的简写方式。与生成器表达式类似

#三、 函数对象
#秉承着一切皆对象的理念，函数也是一个对象，具有属性(可以使用dir()查询)。作为对象，它还可以赋值给其他对象名，或者作为参数传递

#1. lambda函数
#可以用lambada函数的语法定义函数
def func(x, y):     #普通的函数定义方法
    return x + y

func = lambda x, y: x + y    #lambada生成一个函数对象。该函数参数为x,y，返回值为x+y。函数对象赋给func，func的调用与正常的函数无异

#2. 函数作为参数传递(函数名即该对象)
def test (f, a, b):     #第一个参数f就是一个函数对象
    print "test"
    print f(a, b)
test(func, 3, 5)    #将func传给f，test中的f()就拥有了func()的功能
#使用上面的test()函数，带入不同的函数参数，这样就可以提高程序的灵活性，例如：
test((lambda x, y: x**2 + y), 6, 9)     #修改了func的实现过程

#3. map()函数
re = map((lambda x: x+3), [1, 3, 5, 6]) #map()有两个参数，一个是lambda所定义的函数对象，另一个是包含多个元素的list
print re
# map()的功能是将函数对象依次作用于list的每一个元素，每次作用结果存储于返回的list re中。

re = map((lambda x, y: x+y), [1, 2, 3], [6, 7, 9])  #如果作为参数的函数对象有多个参数，可使用此方式，向map()传递函数参数的多个参数，即map()将每次从两个表中分别取出一个元素，带入lambda所定义的函数中
print re

#4. filter()函数
def func(a):
    if a > 100:
        return True
    else:
        return False
print filter(func, [10, 56, 101, 500])  #filter()函数的第一个参数也是一个函数对象，也是将作为参数的函数对象(此例为func)作用于多个元素。
# 如果对象返回的是True,则该次的元素被存储于返回表中。fliter通过读入的函数来筛选数据。同样，在python 3.x中，filter返回的不是表而是循环对象。

#5. reduce()函数
#reduce函数的第一个参数也是函数，但是有一个要求，就是这个函数自身能接收两个参数，reduce()可以 累进地 将函数作用于各个参数。
print reduce((lambda x, y: x + y), [1, 2, 5, 7, 9])     #reduce()的一个参数是lambda函数，它接收两个参数x,y，并返回x+y
#reduce将表中的前两个元素传递给lambda，然后返回值作为lambda的第一个参数再次输入到函数中，而表中的下一个元素即第三个元素作为lambda函数的第二个参数，参与下一次的对lambda的调用，直到表中没有剩余元素为止。

#四、错误处理

#1. 异常处理
re = iter(range(5))
try:
    for i in range(100):
        print re.next()
except StopIteration:
    print "Here is the end", i
print "LOL"

#完整语法结构
#try:
#   …
#except exception1:
#   …
#except exception2:
#   …
#except:                #剩下所有的异常都交给这段程序处理
#   …
#else:                  #如果try中没有异常，那么except部分将被跳过，执行else中的语句。
#   …
#finally：               #finally是无论是否有异常，最后都要做的一些事情。流程如下：try—>异常->except->finally；try->无异常->else->finally。
#   …
#如下例子
try:
    print(a*2)
except TypeError:
    print("TypeError")
except:
    print("Not Type Error & Error Noted")

#如果无法将异常交给合适的对象，异常将继续向上层抛出，直到被捕捉或者造成主程序报错。如下：
def test_func():
    try:
        m = 1/0
    except NameError:
        print("Catch NameError in the sub-function")

try:
    test_func()
except ZeroDivisionError:
    print("Catch error in the main program")

#2. 抛出异常

print("danhuilingshiyuanzai")
#raise StopIteration             #StopIteration是一个类。抛出异常时，会自动有一个中间环节，就是生成StopIteration的一个对象，Python实际上抛出的是这个对象。
#raise StopIteration()           #也可以自行生成一个对象
print("danhuilingshifeizai")

#五、动态类型
#动态类型(dynamic typing)是Python另一个重要的核心概念。Python的变量(variable)不需要声明，而在赋值时，变量可以重新赋值为任意值，这都与动态类型的概念相关。

#1. 动态类型
#用于储存数据的对象，例如数字，字符，字符串，表，词典，在c语言中这样的数据对象为变量，而在Python中，这些都是对象。
#对象是储存在内存中的实体，但我们并不能直接接触到该对象。我们在程序中的写的对象名
