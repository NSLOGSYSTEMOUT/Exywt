# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 下午5:00
# @Author  : ZS
# @Email   : @163.com
# @File    : cmd_client.py
# @Software: PyCharm

import socket

sk = socket.socket()

print(sk)

address = ('127.0.0.1',8000)

sk.connect(address)



while True:
    data = input(">>>>")

    if data == 'exit':

        break

    newdata = bytes(data, encoding="utf8")
    sk.send(newdata)

    data = sk.recv(1024)  # 阻塞

    newString = str(data, encoding="utf8")
    print(newString)

sk.close()