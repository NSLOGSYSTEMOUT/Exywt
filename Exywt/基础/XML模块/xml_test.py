# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 下午3:43
# @Author  : ZS
# @Email   : @163.com
# @File    : xml_test.py
# @Software: PyCharm



import  xml.etree.ElementTree as ET

tree = ET.parse("zsxml")
print(tree)
root = tree.getroot()
print(root.tag)

for child in root:

    print(child.tag)

    for i in child:

        print(i.tag , i.next)


