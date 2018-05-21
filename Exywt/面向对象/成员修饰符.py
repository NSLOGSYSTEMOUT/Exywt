# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 下午2:01
# @Author  : ZS
# @Email   : @163.com
# @File    : 成员修饰符.py
# @Software: PyCharm


class foo:


    v = "123"

    __v = "123"  #私有的静态常量可用静态方法访问

    def __init__(self, name, age):

        self.name = name
        # self.age = age
        self.__age = age        #私有外部无法访问


    def  show(self):
        # return self.__age
        return self.__v

    @staticmethod
    def  stat():
        return  foo.__v


    def __f1(self):

        print("这是个私有的方法")

    def f2(self):

        return self.__f1()

obj = foo("zs",10)

print(obj.name)
print(obj.show() )

print(foo.stat())
obj.f2()


print("继承后的私有问题")

class f:

    def __init__(self):

        self.father = 123
        self.__gen = 123



class s(f):

    #子类无法访问父类中的私有字段
    def __init__(self,name):

        self.name = name
        self.__age = 18
        super(s, self).__init__()

    def show(self):

        # print(self.name)
        # print(self.__age)
        print(self.father)


    def __call__(self, *args, **kwargs):

        print("obj()对象加括号默认执行call方法")

sObj = s("name")

# print(sObj.father)
sObj.show()
sObj()

s("name")()



class FOO:


    def __init__(self):
        pass


    def __int__(self):

        return 11

    def __str__(self):

        return "string"

fObj = FOO()

print(fObj , type(fObj))

#int 执行 __int__方法并将返回值赋值给int对象
r = int(fObj)

str = str(fObj)

print(r)
print(str)



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
        return  item+10

    def __setitem__(self, key, value):

        print(key, value)

    def __delitem__(self, key):
        print(key)


    def __del__(self):

        print("析构函数 对象销毁的时候自动执行 python内部触发")


objtest1 = test("zs1",18)



print(objtest1)
objtest2 = test("zs2",19)

#两个对象相加时自动执行第一个对象的__add__方法，第二个对象会当做参数传递进入
r = objtest1 + objtest2

print(r, type(r))


#__dict__将对象中封装的所有内容通过字典的形式返回
print(objtest1.__dict__)
# print(test.__dict__)

#会自动执行objtest1中的__getitem__方法，10当做参数传递给item
print(objtest1[10])

objtest1[10] = 124
del objtest1[1000000]

# li = [11,22,33,44]
li = list([11,22,33,44])

li[3]= 66
r1 = li[3]

print(r1)


