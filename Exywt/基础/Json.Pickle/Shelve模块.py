# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 下午3:50
# @Author  : ZS
# @Email   : @163.com
# @File    : Shelve模块.py
# @Software: PyCharm


import shelve


f = shelve.open('Shelve_test')



# f['info'] = {'name':'zschange' , 'age':'18'}            #存入数据


#key必须为字符串
data = f.get('info')                                #取出数据
print(data)


# dic = {'name':'zs' , 'age':'18'}
# print(dic.get('sex','age'))