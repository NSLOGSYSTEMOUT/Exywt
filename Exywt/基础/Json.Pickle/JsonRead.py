# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 上午11:26
# @Author  : ZS
# @Email   : @163.com
# @File    : JsonRead.py
# @Software: PyCharm

import json


f = open('jsontest','r')

# data = f.read()
# data = json.loads(data)

data = json.load(f)

print(data['name'])