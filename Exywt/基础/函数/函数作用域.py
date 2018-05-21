
# if True:
#     x =3
#
# print(x)
#
#
#
# x = int(2.9)
#
# g_count = 0

count = 10

def outer():

    global  count
    print(count)       #函数内部没有count的定义可以访问全局的count变量，函数内定义了count变量会屏蔽全局的变量需要声明global为全局变量
    count = 100
    print(count)


outer()