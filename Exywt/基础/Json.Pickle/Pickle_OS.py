# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 下午3:16
# @Author  : ZS
# @Email   : @163.com
# @File    : Pickle_OS.py
# @Software: PyCharm


import pickle
def foo():
    print('OK')


f = open('pickletest','wb')
date = pickle.dumps(foo)
f.write(date)



f.close()
