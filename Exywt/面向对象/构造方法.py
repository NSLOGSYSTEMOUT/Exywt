# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 下午4:49
# @Author  : ZS
# @Email   : @163.com
# @File    : 构造方法.py
# @Software: PyCharm


class Bar:



    def __init__(self, name, age):

        self.name = name
        self.age = age

    def foo(self):

        print(self.name)




z = Bar("zc",18)
z.name = 12
z.age = 10
print(z.name, z.age)
z.foo()




