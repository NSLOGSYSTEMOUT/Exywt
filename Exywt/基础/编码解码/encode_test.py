

#python2中默认ASCII
#python3中默认utf-8

# -*- coding:utf-8 -*-

s = "你好as"

# s_to_unicode = s.decode("gbk")
s_to_encode = s.encode("utf-8")
print(s_to_encode.decode("utf-8"))

