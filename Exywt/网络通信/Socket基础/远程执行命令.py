# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 下午5:46
# @Author  : ZS
# @Email   : @163.com
# @File    : 远程执行命令.py
# @Software: PyCharm


import os

print(os.uname)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))