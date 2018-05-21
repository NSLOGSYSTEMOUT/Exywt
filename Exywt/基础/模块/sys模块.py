

import  sys    #命令行参数list 第一个元素是程序本身的路径

#argv 命令行参数包括脚本名称
print(sys.argv)

def post():
    print("post")

def download():
    print("download")


if sys.argv[0] == 'post':
    post()


elif sys.argv[0] == 'download':
    download()
else:


    print("none")




# sys.exit(n)   退出程序、程序正常退出时exit(0)


# print(sys.path)      #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值

print(sys.platform+"返回操作系统平台的名称")  #返回操作系统平台的名称

import  os


# print(os.path.join(['a','b']))  #将多个路径组合后返回

if sys.platform  == 'win32':

    os.system('dir')

else:
    os.system('ls')

#stdout表中输出流 一个类文件的对象
sys.stdout.write("please:")



# print(sys.modules.__doc__)
# print(dir(sys.modules))
#
# print(help(sys.modules))
#
# print(dir(sys))
