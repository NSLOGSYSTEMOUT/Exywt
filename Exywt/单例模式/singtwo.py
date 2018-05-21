# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 下午5:50
# @Author  : ZS
# @Email   : @163.com
# @File    : singtwo.py
# @Software: PyCharm

# 如果希望之执行普通的除法，那么可以在程序前加上下面的语句
# from  __future__ import division


# print(list([1,2,3]+[1,2,3]))
# print(list("string"))
#
# number = [1,5]
# number[1:1] = [2,3,4]
# del number[1:4]
# number.append(3)
# print(number)

# string = 'aasdfdfd'
# table = ("df","sb")
#
# # print(string.translate("d","b"))
#
#
# a = {"name":"zs", "age":18}
# print({}.fromkeys(["name", "age"]))
#
# b = {"sex":"nan", "name":"newname"}
# a.update(b)
# print(a.values())
#
# print(1,2,3)
#
# x, y ,z = 1,2,3
# x,y = y ,x
#
# print(x, y ,z )
#
#
# values = 1,2,3
# print(values)
#
#
#
# soundrel = {"name":"zs", "age":18}
# key ,value = soundrel.popitem()
# print(key, value)
#
# vles = [x*x for x in range(10) if x%3 == 0]
# print(vles)
#
#
# x1 = ["hello", "world"]
# y1=x1
# y1[1] = "python"
# del x1
# print( y1)


def change(n):
    print(n[0])
    n[0] = "Mr. Cumby"



names = ["Mrs.Entity", "Mrs.Thing"]

change(names[:])
print(names)


def print_parame(x,y,z=2,*pospar, **keypar):

    print( x, y, z)
    print(pospar)
    print(keypar)

print_parame(1,2,3,4,5,6,foo = 1, bar = 2,name = "age")

print_parame(1,2,3,4)

params = {"name":"zs" , "age":18}


class Rectangle:

    def __init__(self):

        self.width = 0
        self.height= 0

    def setSize(self, size):
        self.width, self.height = size


    def getSize(self):

        return  self.width, self.height


    size = property(getSize, setSize)

# r = Rectangle()
# r.width = 10
# r.height = 20
#
# print(r.getSize())
# r.setSize((100,200))
# print(r.width)


r = Rectangle()
r.width = 10
r.height = 20
print(r.size)
r.size = (100,200)
print(r.width)

