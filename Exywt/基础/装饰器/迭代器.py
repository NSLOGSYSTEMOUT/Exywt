
#生成器都是迭代器


l = [1,2,3,4]
d = iter(l)
print(next(d))
print(next(d))



#迭代器有iter方法 有next方法
print("........")

# for循环内部三件事 1.调用可迭代对象的iter方法返回一个迭代器对象 2.调用迭代器对象的next方法 3.处理StopIteration
for i in  [1,3,34] :
    iter([1,3,34] )


from collections import  Iterator,Iterable
print(isinstance([1,2], list))
print(isinstance(l, list))
print(isinstance(l, Iterable))
print(isinstance(d, Iterator))

#迭代器与生成器的区别：