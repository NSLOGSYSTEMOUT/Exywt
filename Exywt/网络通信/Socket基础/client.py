# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 下午2:51
# @Author  : ZS
# @Email   : @163.com
# @File    : client.py
# @Software: PyCharm

import socket

sk = socket.socket()

print(sk)

address = ('127.0.0.1',8000)

sk.connect(address)

# sk.send(bytes("hahaha","utf8"))

while True:
    data = input(">>>>")

    if data == 'exit':

        break

    newdata = bytes(data, encoding="utf8")
    sk.send(newdata)

    data = sk.recv(1024)  # 阻塞
    # bytes(data, encoding = "utf8")
    newString = str(data, encoding="utf8")
    print(newString)

sk.close()

