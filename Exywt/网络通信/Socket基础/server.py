# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 下午2:51
# @Author  : ZS
# @Email   : @163.com
# @File    : server.py
# @Software: PyCharm

import  socket

print("启动server waiting")

sk = socket.socket()

print(sk)

# 192.168.1.38
address = ('127.0.0.1',8000)

sk.bind(address)

sk.listen(3)

'''
# conn客户端的socket对象
conn,addr = sk.accept()

while True:
    receive = conn.recv(1024)

    if not receive:
        break

    newreceive = str(receive, "utf8")
    print(newreceive)

    data = input(">>>>")
    newdata = bytes(data, encoding="utf8")
    conn.send(newdata)
    # print(conn)
    
    
'''

while True:
    conn, addr = sk.accept()

    while True:

        try:
            receive = conn.recv(1024)
        except Exception as  e:

            print(e)
            break
        finally:

            if not receive:
                break

            newreceive = str(receive, "utf8")
            print(newreceive)

            data = input(">>>>")
            newdata = bytes(data, encoding="utf8")
            conn.send(newdata)
            # print(conn)


conn.close()
sk.close()

