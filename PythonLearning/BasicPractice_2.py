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



