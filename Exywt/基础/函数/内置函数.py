

#内置函数

# print(all([1,2,3,""]))
# print(eval('1+3*2'))


#filter 过滤
str = ['a','b','c','d']
def func(s):

    if s!='a':

        return  s
ret = filter(func, str)     #['b', 'c', 'd']     过滤函数
print(ret)                  #<filter object at 0x1005f9f28>
print(list(ret))            #ret是一个迭代器



#map 处理
str1 = ['d','a','b']
def func1(s):
    return  s+"alix"

ret1 = map(func1, str1)
print(ret1 )                 #<map object at 0x1007040f0>

print(list(ret1))           #['dalix', 'aalix', 'balix']


#reduce 结果是一个值
from  functools import  reduce

def add(x,y):
    return  x+y

print(reduce(add,range(1,10)))      #45
print(reduce(add,[1,2,3,4]))


def add1(a,b):
    return  a+b

result = lambda  a,b:a+b
print(list(result))