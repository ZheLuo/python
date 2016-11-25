# -*- coding: utf-8 -*-

#for循环
#基本构造：
#for 元素 in 序列：
#   statement
for a in (3, 4.4, "life"):
    print a

#函数range(), 帮助建立表, 从0开始一直到上限(不包括)
idx = range(5)
print idx

for a in range(10):
    print a**2

#while循环
#基本结构
#while 条件：
#   statement
i = 0
while i < 10:
    print i
    i = i + 1

#中断循环
#continue，在循环的某一次执行中，如果遇到continue，namely跳过这一次执行，进行下一次操作
#break，停止执行整个循环
for i in range(10):
    if (i == 2):
        continue
    print i
for i in range (10):
    if (i == 2):
        break
    print i

#函数定义
def square_sum(a,b):
    c = a**2 + b**2
    return c    #return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。#遇到return时，程序停止执行余下的语句，如果没有return或return后面没有返回值，函数讲自动返回None，None多用于关键字参数传递的默认值。

#函数调用和参数传递
print square_sum(3,4)

a = 1
def change_integer(a):
    a = a + 1
    return a
print change_integer(a)
print a     #当我们将一个整数变量传递给函数，函数对它进行操作，原整数变量的值并不发生变化

b = [1, 2, 3]
def change_list(b):
    b[0] = b[0] + 1
    return b
print change_list(b)
print b     #当我们将一个表传递给函数，函数对它进行操作，原表发生变化
#对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量（我们称之为值传递）
#对于表来说，表传递给函数的是一个指针，指针指向寻列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量（我们称之为指针传递）

#面向对象
#相近的对象，归为一类
class Bird(object):
    have_feather = True
    way_of_reproduction = "egg"
summer = Bird()
print summer.way_of_reproduction #对属性的引用是通过对象.属性(object.attribute)的形式实现的

#动作，即根据东西能做什么事情来区分类别
#"行为"属性为方法（method），通过在类的内部定义函数，来说明方法
class Bird(object):     #当括号中的object，当括号中为object时，说明这个类就没有父类了（到头了）
    have_feather = True
    way_of_reproduction = "egg"
    def move(self, dx, dy):     #self参数是为了方便我们引用对象自身，方法的第一个参数必须是self，无论是否用到。
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
summer = Bird()
print "after move:", summer.move(5,8)

#子类
#类别本身还可以细分成为子类，通过继承来表达
class Chicken(Bird):
    way_of_move = "walk"    #增加了一个子类属性
    possible_in_KFC = True  #增加了另外一个子类属性
class Oriole(Bird):
    way_of_move = "fly"
summer = Chicken()
print summer.have_feather
print summer.move(5,8)      #子类继承了父类，也就享有父类的所有属性，如move方法

#面向对象的进一步扩展
#调用类的其他信息
#通过self调用类属性
class Human(object):
    laugh = "hahahaha"
    def show_laugh(self):
        print self.laugh    #通过self.laugh调用了该类属性的值
    def laugh_10th(self):
        for i in range(10):
            self.show_laugh()
li_lei = Human()
li_lei.laugh_10th()

#__init__()方法
#__init__()方法是一个特殊方法（特殊方法的特点就是名字前后有两个下划线）
#如果在类中定义了__init__()方法，创建对象时，python就会自动调用这个方法，这个过程也被称为初始化
class happyBird(Bird):
    def __init__(self, more_words):
        print "We are happy birds.", more_words
summer = happyBird("Happy,Happy!")      #尽管只是创建了summer对象，但__init__()方法被自动调用了。先创建了对象，然后执行summer.__init__(more_words), "Happy,Happy!"被传递给了__init__()的参数more_words

#对象的性质
#有时性质的值随着对象的不同而不同，此时我们通过赋值给self.attribute，给对象增加一些性质，self会传递给各个方法，在方法内部可以通过引用self.attribute查询或修改对象的性质
class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender  #在初始化中将参数input_gender，赋值给对象的性质self.gender
    def printGender(self):
        print self.gender
li_lei = Human("Male")  #这里"male"作为参数传递给__init__()方法的input_gender变量。gender并不是类属性，是在建立了li_lei这一对象之后，通过初始化赋值给了self.gender
print li_lei.gender
li_lei.printGender()    #对象的性质也能被其他方法调用，调用方法跟类属性的调用类似

#内置函数dir()用于查询一个类或者对象所有属性
print dir(list)

#内置函数help()用来查询说明文档
#print help(list)

#list是一个类，实验一些list的方法
nl = [1, 2, 5, 3, 5]        #实际上nl是类list的一个对象
print nl.count(5)           #计数，看总共有多少个5
print nl.index(3)           #查询nl第一个3的下标
nl.append(6); print nl             #在nl的最后添加一个新元素6
nl.sort(); print nl         #对nl的元素排序
print nl.pop(), nl          #从nl中去除最后一个元素，并将该元素返回
nl.remove(2); print nl      #从nl中去除第一个2
nl.insert(0, 9);print nl   #在下标为0的位置插入9

#运算符是特殊方法
#比如list的add()方法可以看出是特殊方法，特殊之处在于其定义了对于"+"运算符对于list对象的意义，即两个list的对象相加时，会进行的操作.运算符比如"+"，"-"，"<"，">"及下标引用[start:end]等等，从根本上都是定义在类内部的方法
print [1, 2, 3] + [5, 6, 9]
#print [1, 2, 3] - [3, 4]    #会有错误信息，提示运算符"-"没有定义
# 我们现在继承list类，添加对"-"的定义
class superList(list):
    def __sub__(self, b):
        a = self[:] #self是superList的对象，由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象
        b = b[:]
        while len(b) > 0:
            element_b = b.pop() #从list b的最后一个元素开始取
            if element_b in a:  # 如果在a中有
                a.remove(element_b) #就在a中删除
        return a
print superList([1, 2, 3]) - superList([3, 4])
#如果某方法在父类中定义，又在子类中定义了，那么子类对象会参考子类的定义，而不会载入父类的定义，任何其他属性也是这样（Java中的重载）
#定义运算符对于复杂的对象非常有用。举例来说，人有多个属性，比如姓名，年龄，身高等，可以把对人类的比较(<,>,=)定义成只看年龄，这样就可以根据自己的目的，讲原本不存在的运算符增加在对象上了

#作业1

#闰年判断

def leapYear(year, month, day):
    if type(year) or type(month) or type(day) == type(1):
        if month > 12 or month < 0:
            return "Wrong Month"
        if day > 31 or day < 1:
            return "Wrong day"
        if year % 4 == 0:
            return True
        else: return False
    else: return "Wrong Date Format"

print leapYear(1999,2,27)
print leapYear(2000,3,4)
print leapYear(2000,3,43)
print leapYear(2000,13,2)
print leapYear(2000,13,43)







