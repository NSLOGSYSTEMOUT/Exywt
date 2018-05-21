# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 下午4:53
# @Author  : ZS
# @Email   : @163.com
# @File    : 类的特殊成员.py
# @Software: PyCharm


class test:

    '''当前类是干什么的'''

    def __init__(self, name, age):

        self.age = age
        self.name = name


    def __str__(self):

        return  "%s-%s"  %(self.name , self.age)

    # 两个对象相加时自动执行第一个对象的__add__方法，第二个对象会当做参数传递进入
    def __add__(self, other):

        return self.age+other.age

    def __getitem__(self, item):
        # return  item+10

        if type(item) == slice:

            print("调用内部希望切片处理")

        else:
            print("调用内部希望做索引处理")

        print(item, type(item))

    def __setitem__(self, key, value):

        print(key, value)

    def __delitem__(self, key):
        print(key)


    def __iter__(self):

        return iter([12,13,14])


    def __del__(self):

        print("析构函数 对象销毁的时候自动执行 python内部触发")


li = test("name",18)

# li[123]
# li[1:4:2]


#如果类中有__iter__方法 对象--》可迭代对象
#对象.__iter__()的返回值：迭代器
#获取li对象中的__iter__方法并获取返回其值
#循环获取的对象
for i in li:

    print(i)



#类都是type类的对象