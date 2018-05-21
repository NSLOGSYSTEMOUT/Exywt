# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午5:06
# @Author  : ZS
# @Email   : @163.com
# @File    : 类的创建字段.py
# @Software: PyCharm


#静态字段属于类

# class Provience:
#
#     #静态字段
#     country='china'
#
#     def __init__(self, name):
#
#         #普通字段
#         self.name = name
#
#
#
# obj = Provience("sh")
#
# print(obj.country)
# print(obj.name)
#
#
# obj2 = Provience("sz")
#
# print(obj2.country)
# print(obj2.name)
#
# print(Provience.country)


#成员变量


class foo:

    def __init__(self):

        self.name = "name"

    @property
    def per(self):
        # print("per ")
        return  1

    @per.setter
    def per(self,val):
        # self.val = val
        print(val)

    @per.deleter
    def per(self):
        print("per delter")


objFoo = foo()

r = objFoo.per
print(r)

objFoo.per = 123
del objFoo.per




class fooPlus:

    def f1(self):
        return  "123fooPlus"

    def f2(self,val):
        print(val)


    def f3(self):
        print("fooPlus del ")


#   per = property(f1,f2,f3) 默认对应的参数
    per = property(fget=f1,fset=f2,fdel=f3,doc="描述信息")

print("*************")
objPlus = fooPlus()



result = objPlus.per
print(result)
objPlus.per = 1234
del objPlus.per

'''
                                        
class Rectangle:                     
                                     
    def __init__(self):              
                                     
        self.width = 0               
        self.height= 0               
                                     
    def setSize(self, size):         
        self.width, self.height = size
                                     
                                     
    def getSize(self):               
                                     
        return  self.width, self.heig
                                     
                                     
    size = property(getSize, setSize)
                
r = Rectangle()
r.width = 10        
r.height = 20       
print(r.size)       
r.size = (100,200)  
print(r.width)  
'''


class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value

        else:
            self.__dict__[name] = value


    def __getattr__(self, name):

        if name == 'size':
            return self.width, self.height

        else:
            raise AttributeError



r = Rectangle()
r.size = (10,20)
print(r.size)
print(r.height, r.width)
r.height = 100
r.width = 200
print(r.size)

print("使用list构造方法显式的将迭代器转化为列表")
class TestIterator:

    value = 0

    def __next__(self):
        self.value += 1

        if self.value > 10 :raise StopIteration
        return self.value

    def __iter__(self):
        return  self


ti = TestIterator()
print(list(ti))























