# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 上午10:59
# @Author  : ZS
# @Email   : @163.com
# @File    : 利用属性实现分页.py
# @Software: PyCharm


class Page:

    def __init__(self, current_page):

        try:
            p = int(current_page)
        except Exception as e:

            p = 1

        self.page = p


    def start(self):

        val = (self.page-1)*10
        return val

    def end(self):

        val = self.page*10

        return val


li = []

for i in range(1000):
    li.append(i)

while True:
    p = input("输入查看的页数：")
    # p = int(p)
    obj = Page(p)

    # start = (p - 1) * 10
    # end = p * 10
    #
    # print(li[start:end])
    # @property修饰加在start 与end方法前修饰改为成员变量的形式
    print(li[obj.start():obj.end()])