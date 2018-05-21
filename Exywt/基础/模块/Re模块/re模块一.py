

#正则表达式小型的高度专业化的编程语言 内嵌pythond中通过re模块实现

#string提供的方法是完全匹配


#正则表达式模糊匹配

import re


#元字符
# ret = re.findall('w\w{2}l','hello wrold')

#.通配符
# ret = re.findall('w..l','hello wrold')  #.只能代指任意一个字符
#
# print(ret)


#^ 从起始位置算
# ret = re.findall('^s...o', 'sfdsfsdhsdfeo')
# print(ret)


#$只算末尾位置

# ret = re.findall('a..x$','ksldjflsauix')
# print(ret)


#*: 重复匹配

# ret = re.findall('z.*s', 'sdlfzdss dfd zsdsdkfjddzs   sdlkfjdl')

# print(ret)


#+ [1, 到无限大]
# ret = re.findall('a+b', 'aaaabsdfaweraaaabbbbbb  dsbbsd')       #['aaaab', 'aaaab']
# print(ret)


#？ [0,1]

# ret = re.findall('a?b', 'aaabdfbbbdassblfj')        #['ab', 'b', 'b', 'b', 'b']
# print(ret)

#a 为1到5次
# ret = re.findall('a{1,5}b','ddaaaaabllbabiaaabkaab')
# print(ret)


# ret = re.findall('a*b','ddaaaaaadaaaabbbbbbllbabiaaabkaab')
# print(ret)

# *等于{0，到无穷大}  +等价{1，到无穷大}   ？等价{0，1}


#字符集


#[c,d]  c ,或d  [] 只能匹配一个字符
# ret = re.findall('a[c , d]x', 'acx')

# ret = re.findall('[a-z]', 'achgtrzhtx')        #['a', 'c', 'h', 'g', 't', 'r', 'z', 'h', 't', 'x']
# print(ret)

#[]取消元字符的特殊功能
# ret = re.findall('a[w,*,., \,,]','aw*da.a,')
# print(ret)                    ['aw', 'a.', 'a,']

# ret = re.findall('[1-9, a-z, A-Z]', '12fksljfSDf')      #['1', '2', 'f', 'k', 's', 'l', 'j', 'f', 'S', 'D', 'f']
# print(ret)

#^放在[]中取反的意思除了r外的其他元素 []中的所有元素
# ret = re.findall('[^r,a]','asd,kfjRr')     #['s', 'd', 'k', 'f', 'j', 'R']
# print(ret)


# \
#\后边跟元字符去除特殊功能
#\跟普通字符实现特殊功能

# \d 匹配任何十进制数字        = [0-9]
# \D 匹配任何非数字字符        = [^0-9]
# \s 匹配空白字符             = [\t\n\r\f\v]
# \S 匹配非空白字符           = [^\t\n\r\f\v]
# \w 匹配任何字母数字字符       = [a-zA-Z0_9_]
# \W 匹配任何任何非字母数字字符   = [^a-zA-Z0_9_]
# \b 匹配一个单词边界，也就是单词和空格间的位置

# print(re.findall('\d{11}','fasfdfd123441232376543'))    #['12344123237']

# print(re.findall('\sasd','fasfdf asd123441232376543'))

# print(re.findall(r'i\b','i am a list'))




##############

#匹配第一个满足条件的结果
# ret = re.search('a..x','wasdxdfdsasdx')
# print(ret)        #<_sre.SRE_Match object; span=(1, 5), match='asdx'>
# print(ret.group())


# ret = re.search('a\.','a.gj').group()  #a.

# ret = re.search('a\+','a+gj').group()  #a+
# print(ret)



# ret = re.findall('\\\\','abc\de')

# ret = re.findall(r'\\','abc\de')
# print(ret)

# m = re.search(r'\bblow','blow')
# print(m)


# ret = re.findall('\\\\','abc\de')

# ret = re.findall(r'\\','abc\de')
# print(ret)

#######
# ()  ?P<>

#前面* + ？是贪婪匹配后面加？使其变为惰性匹配
# print(re.findall('abc*?','abccc'))      #['ab']

# print(re.search('(as)+','sdjafasas').group())   #asas

# ret = re.search('(?P<id>\d{3})','weee34tfdfdstt123/ooo')
# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weee34tfdfdstt123/o1o2o')
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))


# finall()所有结果返回到一个列表中
#search()返回一个对象，对象可调用group()返回结果

#match() 只在字符串开始匹配,返回一个对象，对象可调用group()返回结果

# ret = re.match('asd','asddfasd')
# print(ret.group())


#split()
# ret = re.split('[j,s ]','adjksd')
# print(ret)        ['ad', 'k', 'd'

#sub() 替换
# ret = re.sub('a..s', 's..b','kakjsijjakks')
# print(ret)      #ks..bijjs..b


#compile()
# obj = re.compile('\.com')
# ret = obj.findall('sdlfaslkdf.comlsdf')
# print(ret)



# ret  = re.findall('www.(\w+).com','www.baidu.com')
# print(ret)          ['baidu']

ret  = re.findall('www.(?:\w+).com','www.baidu.com')
print(ret)              #['www.baidu.com']


# ret2 = re.finditer('\d','1233sdf2')
# print(next(ret2))


print(re.escape("www baidu com"))       #www\ baidu\ com