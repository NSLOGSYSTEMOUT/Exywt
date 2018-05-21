
#能调用方法的是对象

# f = open("小重山", "r", encoding="utf-8")
# data=f.read(5)          #取五个字符，默认全部取出
# print(data)
# f.close()

# f2 = open("xiaochongshan","w")
# f2 = open("小重山2", "a")              #写入同一个文件首先清空原文件在写入 "a"参数为append模式 添加在文件后
# f2.write("\n hello world")
# f2.close()


# f = open("小重山", "r", encoding="utf-8")

# data =f.readline()
# print(data)
# print(f.readline())
# print(f.readlines())          #打印列表类型



# number = 0          #修改第六行

# for i in  f.readlines():
#
#     number += 1
#
#     if number == 6:
#         i = "".join([i.strip(), "I like it"])
#
#         print(i.strip())
#
#     else:
#         print(i.strip())

# print(f.tell())         #获取当前光标的位置
# print(f.read(10))
# print(f.tell())
#
# print(f.read(3))
# f.seek(0)               #移动光标的位置
# print(f.read(2))
#
#


'''
import sys,time

for i in range(20):


    # sys.stdout.write("*")
    # sys.stdout.flush()

    print("*", end=" ", flush=True)
    time.sleep(0.2)
'''

# f = open("小重山", "a", encoding="utf-8")
#
# f.truncate(5)                        #清空f模式为w写模式


# f = open("小重山","r+",encoding="utf8")
# print(f.read())
# f.write("write something")




# number = 0
#
# f = open("小重山", "r+", encoding="utf8")
#
# for line in f:
#     number += 1
#
#     if number == 6:
#         # line = " ".join([line.strip(), "hello line 6"])
#         f.write("hello line two 6")
#     print(line.strip())
# f.close()

# f_read = open("小重山","r")                        #将文件复制到另一个文件中
# f_write = open("小重山2", "w")
#
# number = 0
# for line in  f_read:
#     number += 1
#
#     if number == 5:
#         # line = "hello line 5\n"
#         line = "".join([line.strip() , "hello line 5\n"])
#         print(line)
#     f_write.write(line)
#
# f_write.close()

#with 管理创建多个文件对象 
with open("小重山","r") as f_read, open("小重山2", "w") as f_write:        #将文件复制到另一个文件中
    for line in f_read:

        f_write.write(line)
