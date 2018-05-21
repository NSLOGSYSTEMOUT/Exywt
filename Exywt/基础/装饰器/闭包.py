

#如果在一个内部函数，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包
#关于闭包
def outer():

    x = 10
    def inner():  #内部函数
        print(x)    #外部的变量

    return  inner   #内部函数inner闭包

# outer()()

f = outer()
f()

