
#集合对象是一组无序的可哈希的值（不可变类型）
# s = set('asdfv')
# print(s)            #{'f', 's', 'a', 'v', 'd'}
#
# s1 = ['aa','aa','bb']
# s2 = set(s1)
# print(s2,type(s2))           #{'bb', 'aa'} <class 'set'>
#
# s3 =list(s2)
# print(s3 , type(s3))        #['bb', 'aa'] <class 'list'>


li= [2,3,"abc"]
s = set(li)
print(s)

# d = {s:"123"}     TypeError: unhashable type: 'set'

#集合本身是无序的不能为集合创建索引或者切片操作，只能循环遍历或者使用in ，not in来访问或判断集合元素

# print(2 in  li)     #True

# s.add("4")
# print(s)
# s.update('ops')
# print(s)            #{2, 3, 'o', 's', 'p', 'abc'}

# s.update('ooos')
# print(s)            #{2, 3, 'p', 'abc', 'o', 's'}


# s.update([12,'abc'])
# print(s)                #{2, 3, 12, 'abc'}

# s.pop()                 #随机删除set中一个
# print(s)

# s.clear()                 #清空集合

#
print(set("abccccaabb") == set("abc"))      #True 等价

#子集 超集

print(set("abc") < set("abcdd"))        #True


a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

#交集
print(a.intersection(b))        #{4, 5}
print(a & b)                    #{4, 5}

#并集 union
print(a.union(b))               #{1, 2, 3, 4, 5, 6, 7, 8}
print(a|b)                      #{1, 2, 3, 4, 5, 6, 7, 8}

#a中有的b中没有 in a not in b 差集
print(a.difference(b))          #{1, 2, 3}
print(a-b)                      #{1, 2, 3}

#反向交集
print(a.symmetric_difference(b)) #{1, 2, 3, 6, 7, 8}
print(a^b)                      #{1, 2, 3, 6, 7, 8}



#父集超集
print(a.issuperset(b))  #a>b
print(a.issubset(b))  #子集 a<b