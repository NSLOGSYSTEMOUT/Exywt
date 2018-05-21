# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 下午5:11
# @Author  : ZS
# @Email   : @163.com
# @File    : jicheng.py
# @Software: PyCharm


class father():

    def foo(self):

        print("hello")

    def foo2(self):
        print("foo2")



class son(father):

    def son(self):

        print("son")

    def foo2(self):

        #子类调用父类方法的两种情况
        # super(son, self).foo2()
        father.foo2(self)
        print("sfoo2")




s = son()
s.foo2()
s.son()




#多继承


class f1():

    def a(self):
        print("f1.a1")


class f2():

    def a(self):
        print("f2.a2")



#继承方法的执行为：从左向右执行，先继承左类中的方法
class s1(f2, f1):

    pass

son1 = s1()

son1.a()



class Bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:

            print("aaaah....")
            self.hungry = False
        else:
            print("No Thanks")



class SongBird(Bird):
    
    # 此处重写了init方法不能访问到hungry的属性 添加super调用父类的方法防止被覆盖掉父类中的方法动作行为
    def __init__(self):

        super(SongBird,self).__init__()
        self.sound = "Squawk!"

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()