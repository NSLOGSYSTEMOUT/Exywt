# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 上午11:18
# @Author  : ZS
# @Email   : @163.com
# @File    : Json模块.py
# @Software: PyCharm


import  json

dic = {'name':'zs', 'age':'18'}

f = open('jsontest','w')

# date = json.dumps(dic)
# f.write(date)

json.dump(dic, f)


f.close()
