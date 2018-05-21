


def f(n):
    return  n *n

a = [f(x) for  x in range(10)]
print(a)
print(type(a))


t = ("123", 1)
x,y = t
print(x)
print(y)

print("-------- ----------")
s = (x*2 for x in range(10))
print(s.__next__())
print(next(s))          #python2中的方法等价 s.__next__()
print(s.__next__())

#生成器是可迭代对象 Iterable()

# for i in  s:
#     print(i)



#生成器的两种创建方式

#1.
#s = (x*2 for x in range(10))

#2. yield
print("-------- ----------")
def foo():

    print("foo ...")
    yield 1

    print("foo2 .. ")

    yield 2




#
# for i in foo():
#
#     while True:
#         i = next(foo())
#
#         print(i)


# foo().__iter__() 可迭代对象的拥有的方法


print("fib .........")

def fib(max):

    n, before, after = 0,0,1

    while n < max:

        # print(after)
        yield before

        before,after = after, before+after
        # before = after
        # after = after + before
        n= n+1

g = fib(8)

print(g)
print(next(g))         #print(next(g )) 与print(next(fib(8)))是有区别的 ******
print(next(g))
print(next(g))
print(next(g))


print("send ................")

def bar():
    print("ok1")

    count = yield 1
    print(count)
    # print("ok2")
    yield 2



b = bar()
# b.send(None)            #同next        ok1
next(b)                 #ok1
y =b.send("haha")      #同next只不过将haha传给count参数并输出
print(y)                #2


print("******************")

nested = [[1,2], [3,4], [5]]

def flatten(nested):
    for sublist in nested:
        for element in  sublist:
            yield  element


for num in flatten(nested):
    print(num)


print(list(flatten(nested)))
