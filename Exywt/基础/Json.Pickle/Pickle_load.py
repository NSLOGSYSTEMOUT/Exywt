# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 下午3:25
# @Author  : ZS
# @Email   : @163.com
# @File    : Pickle_load.py
# @Software: PyCharm

import pickle
 

#可以序列对象但是函数需要存在于这个文件中。
def foo():
    print("haha")

f = open('pickletest','rb')

data = f.read()
data = pickle.loads(data)

data()

f.close()