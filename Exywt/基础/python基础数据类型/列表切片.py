

names=['name0','name1','name2','name3','name4','name5']
# print(names[0])

#增删改查

#切片
# print(names[0:])  #取到最后
# print(names[0:-1]) #取到倒数第二个
# print(names[0:-1:2]) #步长默认为1从左到右一次取值
# print(names[0::2]) #从左到右隔一个取值
# print(names[3:0:-2])

# names.append('name6')    #默认插入到最后一个
# print(names)
#
# names.insert(0,'name-1')  #插入到任意指定位置
# print(names)

# names[0]='movename0'      #修改指定位置
# names[1:3] = ["rename1" , "rename2"]
# print(names)

#删除 remove pop  del

# names.remove('name0')
# name = names.pop(1)   #pop删除返回被删除的值
# print(name)

# del names
# names = 'names'
# print(names)

#列表内置方法
# print(names.count('name0'))  #count 统计某个元素在列表中出现的次数

# names2 = ['name-1','name-2']
# names.extend(names2)              #names2拼接到names后
# print(names)

# print(names.index('name5'))       #返回name5的索引

# names.reverse()     #数组逆序没有返回值
# print(names)

# number = ['2','9','4','3']  #数组排序
# number.sort()
# print(number)

#python2 版本中可用
# a = range(10)
# a[1:3]= ['a', 'b']
# print(a)

for i in range(5):
    print(i)





