
#python中唯一的映射类型的，采用key value模式存储数据
#不可变类型：整型、字符串、元组
#可变类：列表、字典

# a = ([1,2,3],)
# print(a[0][0])
# a[0][0] = 2
# print(a[0][0])

dic = {
    'name':'zs',
    'age':18,
    'hobby':{'girle_name':'girlename', 'age':18},

    'ishandsome':True,
       }


# print(dic)
# print(dic['name'])
# print(len(dic))

# dic2 = dict((["naem" , "zs"],))     #python的容错率
# print(dic2)


#字典的操作  字典是无序的

dict1 = {"name":"zsupdate"}
dict1["age"]=180
dict1.setdefault("hobby", "girles")    #查找字典中是否有age的key如果有的话不会做出修改，没有的话插入，setdefault有返回值返回有的值18
# print(dict1)

# print(dic.values())
# print(dic.items())             #返回所有的item
# print(dic.keys())              #打印所有的key


# dic.update(dict1)       #将字典dict1中如果相同的key 但是value不同改为dict1中的值，如果没有key则添加，key相同内容覆盖
# print(dic)

# a = dic.popitem()
# print(a, dic)            #默认删除最后一个随机删除的
# dic.clear()               #清空字典
# del dic['name']           #删除自定中指定的键值对
# age = dic.pop('age')      #删除自定中指定的键值对并返回该键值对的值


#其他操作 以及涉及到的方法

dict2= dic.fromkeys(['one','two'],'test')
# print(dict2) {'two': 'test', 'one': 'test'}


# print(sorted(dic))       #排序默认对key排序

#字典的嵌套
#字典的遍历

# for i in  dic:                #遍历时推荐使用****
    # print(i,':',dic[i])
    # print(i, dic[i])

for i,v in  dic.items():
    print(i, v)

