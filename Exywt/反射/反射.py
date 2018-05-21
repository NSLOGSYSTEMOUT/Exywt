# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 上午11:17
# @Author  : ZS
# @Email   : @163.com
# @File    : 反射.py
# @Software: PyCharm

'''
class Person:

    def __init__(self, name , age):
        self.name = name
        self.age = age


    def show(self):

        return  "%s -- %s" %(self.name, self.age)


one = Person("zs", 18)

one.__dict__["name"] = "changename"
# one.__dict__["changeName"]

print(one.__dict__["name"])

#获取属性值
attrbute = getattr(one, "name")
print(attrbute)


func  =  getattr(one,"show")
r = func()
print(r)

print(hasattr(one, "name"))

#become before name值赋值给  name
setattr(one,"name","become before name")
print(one.name)


delattr(one,"name")
print(one.name)             #'Person' object has no attribute 'name'

'''

class Person:

    stat = '123'

    def __init__(self, name, age):

        self.name = name
        self.age  = age


print(getattr(Person, "stat"))

import s2

print(s2.NAME)

r1 = getattr(s2,"NAME")
print(r1)
print(s2.func())
r2 = getattr(s2,"func")
print(r2())

cls = getattr(s2, "Foo")

obj = cls()
print(obj.name)


inStr = input("输入页码")

if hasattr(s2, inStr):

    func = getattr(s2,inStr)
    string = func()
    print(string)

else:
    print("404错误")




