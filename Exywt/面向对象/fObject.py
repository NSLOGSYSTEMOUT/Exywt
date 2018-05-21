# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午4:17
# @Author  : ZS
# @Email   : @163.com
# @File    : fObject.py
# @Software: PyCharm


class Bar():



    def __init__(self ,name, age,sex):
        print("init zhixing ")
        self.name = name
        self.age = age
        self.sex = sex

        print(self.name, self.age, self.sex)

    def foo(self, age):
        print(self,self.name, age)


# z = Bar()
# z.name = "zs"
# z.foo(666)

z2 = Bar("zs",18,"nam")

z3 = Bar("zss",182,"na")