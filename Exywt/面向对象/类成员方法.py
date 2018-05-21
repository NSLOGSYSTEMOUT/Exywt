# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 下午4:59
# @Author  : ZS
# @Email   : @163.com
# @File    : 类成员方法.py
# @Software: PyCharm



class Foo:

    #普通方法 对象调用
    def Bar(self):
        print("bar")

    #静态方法 保存在类中 类调用
    @staticmethod
    def sta():
        print("123")


    @staticmethod
    def sta2(name):
        print(name)

    #类方法

    @classmethod
    def classMt(cls):

        print(cls)
        print("cls method")


foo = Foo()

foo.Bar()

Foo.sta()
Foo.sta2("name")

Foo.classMt()