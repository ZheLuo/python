# -*- coding: utf-8 -*-

#变量无需声明，可用内置函数type()查询。
a = 10
print a
print type(a)

a = 1.3
#逗号分隔输出
print a, type(a)

#tuple序列
s1 = (2, 1.3, "danhuiling", 5.6, 120, False)
#list序列
s2 = [True, 5, "pangzai"]
print s1, type(s1)
print s2, type(s2)
#区别在于，一旦建立，tuple的各个元素不可在变更，而list的各个元素可以再变更。

#一个序列作为另外一个序列的元素
s3 = [1, [2, 3, 4]]
#空序列
s4 = []

print s1[0]
print s2[2]
print s3[1][2]

#由于list的元素可变，可以对list的元素进行赋值；但是tuple则会报错。
s2[2] = 3.0
print s2

#范围引用基本样式[下限：上限：步长]（如写明上限，上限不含在内）
print s1
print s1[:5]     #从开始到下标4（不含下标为5的元素）
print s1[2:]     #从下标2到最后
print s1[0:5:2]  #从下标0到下标4（不含下标5），每隔2取一个元素（即下标为0，2，4的元素）
print s1[2:0:-1] #从下标2到下标1（倒序取）
#元素尾部引用
print s1[-1] #倒数第一个元素
print s1[-3] #倒数第三个元素
print s1[0:-1] #最后一个元素不会被引用，即上限不含在内。

#字符串是特殊的tuple，可以执行tuple相关的操作
str1 = "danhuilingpangzai"
print str1[2:4]

#数学运算
print 1+9
print 1.3-4
print 3*5
print 4.5/1.5
print 3**2  #乘方
print 10 % 3  #求余

#判断，返回布尔值
print 5 == 6
print 8.0 != 8.0
print 3 < 3, 3 <= 3
print 4 > 5, 4 >= 0
print 5 in [1,3,5]  #5是list[1,3,5]的一个元素

#逻辑运算
print True and True, True and False
print True or False
print not True
print 5 == 6 or 3 >= 3

#缩进表示代码块
i = 1
x = 1
if i > 0:
    x = x+1
print x

#if语句
i = 1
if i > 0:
    print "positive i"
    i = i + 1
elif i == 0:    #注意else if的写法为：elif
    print "i is 0"
    i = i * 10
else:
    print "negative i"
    i = i - 1
print "new i: ", i

#if嵌套
i = 5
if i > 1:
    print "i is larger than 1"
    print "good"
    if i > 2:
        print "i is larger than 2"
        print "even better"


#pro update

