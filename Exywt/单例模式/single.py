# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 下午5:06
# @Author  : ZS
# @Email   : @163.com
# @File    : single.py
# @Software: PyCharm


class Person:

    def __init__(self,name, age):

        self.name = name
        self.age  = age

    def show(self):

        print(self.name, self.age)

# per1 = Person()
# per2 = Person()
# per2 = Person()


# p = None
#
# while True:
#
#     if p:
#         p.show()
#
#     else:
#
#         p = Person("zs", 16)
#         p.show()


class Foo:

    __v = None

    @classmethod
    def get_Instance(cls,name, age):
        if cls.__v:
            return cls.__v

        else:

            cls.__v = Foo(name=name, age=age)

            return  cls.__v

    def __init__(self, name ,age):

        self.name = name
        self.age = age



obj1 = Foo.get_Instance("zs",18)

print(obj1.__dict__)

obj2 = Foo.get_Instance("zstow", 19)

obj1.name = 'zs2'
obj1.age = 19

print(obj1.__dict__)
print(obj2.__dict__)


