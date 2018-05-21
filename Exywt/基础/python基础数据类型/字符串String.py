#String操作

a = '123'*10   # *重复输出字符串
# print(a[2:])    #通过索引获取字符串中字符，与列表的切片操作是相同的

#关键字in
#print('a' in  'haha')  #判断字符串是否在另一个字符串中在的话返回True否则返回False

#格式字符串  %

#字符串拼接 +
# b = 'nil'
# # print(a+b)
# c = ''.join([a, b])
# print(c)


#String的内置方法

str1 = 'hello kitty {name} {age} {hobby}'

# print(str1.count('l'))            #****统计该字符串中有字符串l的个数
# print(str1.capitalize())          #***首字母大写
# print(str1.center(40,'-'))        #字符串居中，并用字符-填充两边的边距
# print(str1.endswith('ty'))        #****判断字符串是否以某个字符串结尾，返回True 或 False
# print(str1.startswith('he'))      #***判断字符串是够以某个字符串开始， 返回True 或 False
# print(str1.expandtabs(tabsize=10))      #\t处会有10个空he\tllo kitty
# print(str1.find('ty'))                      #***查找到第一个元素并将索引值返回,不存在返回-1
# print(str1.format(name='zs',age='18', hobby='a'))    #******格式化字符串的输出
# print(str1.format_map({'name':'zs', 'age':18 ,'hobby':'a'}))#格式化输出的另一种方式
# print(str1.index('z'))              #*****查找到第一个元素并将索引值返回,不存在报错
# print('1df'.isalnum())            #字符串中是否含有数字，返回True 否则False
# print('1f'.isdecimal())           #判断是否为十进制的数是返回True 否则False
# print('1234'.isdigit())             #****判断是否为数字
# print('adf'.isidentifier())       #检验是否为非法变量
# print('Adf'.islower())              #字符串是否为全小写字母
# print('asA'.isupper())             #字符串是否为全大写字母
# print(' '.isspace())              #是否是一个空格
# print(str1.istitle())             #判断是否为标题每一个单词的首字母要大写
# print(str1.lower())               #字符串中的大写字母变为小写字母
# print(str1.upper())               #字符串中的小写字母变为大写字母
# print('asSA'.swapcase())            #*****字符串中大写变小写  小写变大写
# print('hello'.ljust(40,'*'))         #靠左对齐用*填充
# print('hell0'.rjust(10,'*'))            #靠you左对齐用*填充
# print('      \thello\n'.strip())        #去掉空格左右都去掉

# print('abcde'.replace('a','aaaaa'))   #把字符串a替换成aaaa
# print('asasas'.rfind('b'))             #返回 字符串中存在的最后一个位置返回索引值，若不存在返回-1

# print('abcdefg'.split('c'))             #通过切割掉字符串分割为列表
# a ='abcdefg'.split('c')                 #通过字符串把列表join为字符串
# print('c'.join(a))

# print('my is ha'.rsplit(' ',1))       #右侧通过字符串分割 只分割一次
# print('my is ha'.title())             #所有单词的首字母大写