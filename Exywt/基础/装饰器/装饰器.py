

import  time

# start = time.time()
# print(start)            #1514358229.418227当前的时间
# time.sleep(1)
# end = time.time()
# print(end)
# print(end-start)


def foo():

    start = time.time()
    print("foo")
    time.sleep(1)
    end = time.time()
    print(end-start)
#
# foo()

'''
def foo():

    print("foo")
    time.sleep(1)

#1.函数当做func参数传入 计算一个函数执行消耗的时间
def show_time(func):

    start = time.time()
    func()
    end = time.time()
    print("gap is %s" %(end-start))

show_time(foo)    #改变的函数的调用方式
'''

#
#2，装饰器函数
def show_time(func):

    def  inner():
        start = time.time()
        func()              #执行原来的功能函数
        end = time.time()
        print("gap time is : %s" % (end - start))

    return inner


# foo = show_time(foo)
# print(foo)
#
# foo()             #执行inner函数

@show_time      #相当于f = show_time(f)

def f():
    print("foo")
    time.sleep(1)
# f =  show_time(f)
# f()   #在调用




#功能函数➕参数


def show_time_two(func):

    def inner(*x,**y):
        start = time.time()
        func(*x,**y)
        end = time.time()

        print("time2 gap is : %s" %(end-start))
    return inner


@show_time_two

def add(*a,**b):

    sum = 0
    for i in  a:
        sum += i

    print("summary is %d" %sum)
    time.sleep(1)

add(1,2,5,7)


#装饰器参数

def logger(flag=" "):
    def show_time_two(func):

        def inner(*x, **y):
            start = time.time()
            func(*x, **y)
            end = time.time()

            print("time2 gap is : %s" % (end - start))

            if flag == 'true':
                print("调用日志函数 。。。")

        return inner

    return  show_time_two

@logger('true')

def add(*a,**b):

    sum = 0
    for i in  a:
        sum += i

    print("summary is %d" %sum)
    time.sleep(1)

add(1,2,5,7)


@logger()
def bar():
    print("hello bar")
    time.sleep(3)

bar()



def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

