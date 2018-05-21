

import  os

# print(os.getcwd())      #/Users/sai/Desktop/Python/Exywt/练习/模块    获取当前的工作目录

os.chdir('/Users/sai/Desktop/Python/Exywt/基础')      #切换到自定的目录下
# print(os.getcwd())

print(os.curdir)            #.

print(os.pardir)            #..
# os.makedirs(r'abc/ake//bsd')        #创建多层文件夹  注意不同操作系统的/ 与 \  UNIXmac中是/ Windows中是\\ macOS :
# os.removedirs(r'abc/ake//bsd')
# os.removedirs('abc\\ake\\bsd')
# print(os.getcwd())



# os.mkdir("my")
# os.rmdir("my")

# print(os.listdir())         #打印当前路径下的文件夹、文件名
# os.remove("文件")           #只删除文件 不能删除文件夹

# os.renames()
# info = os.stat('/Users/sai/Desktop/Python/Exywt/练习/time模块/时间模块.py')
# print(info)

# print(os.sep)     #获取路径分隔符  不同系统下的不同

# os.system("dir")      #命令行

# print(os.environ)            #获取系统环境变量

# print(os.path.abspath('基础'))        #/Users/sai/Desktop/Python/Exywt/基础/基础 获取绝对路径

# print(os.path.split(r"/Users/sai/Desktop/Python/Exywt/基础/基础"))  文件路径  文件名

print(os.path.dirname("/Users/sai/Desktop/Python/Exywt/基础/时间模块.py"))    #返回path目录 print(os.path.split())的第一个元素


print(os.linesep)

a = set([1,2,3])
b = set([2,3,4])
print(a.union(b))
print(a.issubset(b))