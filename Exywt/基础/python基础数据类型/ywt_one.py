

# d = {'a': 1, 'b': 2, 'c': 3}
#
# for key in  d:
#     print(key)

#
# for value in d.values():
#     print(value)


# n = d['a']
# print(n)

'''
str='abcdefg'
n=len(d)
print(n)

for ch in "ABC":
    print(ch)
'''


# for x, y in [(1,1), (2,2), (3,3)]:
    # print( x , y)

l = list(range(1, 11))


L = [x * x for x in range(10)]
# print(L)

g = (x * x for x in range(10))
#print(g)
#print(next(g))

#for n in g:
# print(n)


# salary = input("salary:")
# if salary.isdigit():
#     salary = int(salary)
# else:
#     print("input number")
#     exit()
#
#
# name = input("name is :")
# age  = input("age is :")

# msg = '''
# ---------- %s Info ----------
# Name: %s
# age : %s
#
# ---------- end --------------
# ''' % (name, name, age)
# print(msg)

#in py3 不区分整形与长整型了，统称为整型

# print( 90 > 80)
#
# score = int(input("score:"))
#
# if score > 90:
#     print('A')
# elif score > 80:
#     print('B')
# else:
#     print('C')

#字符串

# _name = 'zs'
# _password = '123'
#
#
# for i in  range(3):
#     username = input('username is :')
#     password = input('password is :')
#
#     if _name == username and _password == password:
#         print('welcome %s login' % _name)
#         break
#     else:
#         print('user or password error !')



_name = 'zs'
_password = '123'
count = 0

while count < 3:
    username = input('username is :')
    password = input('password is :')

    if _name == username and _password == password:
        print('welcome %s login' % _name)
        break
    else:
        print('user or password error !')
    count += 1
    print("count =  %d" %count)
else:
    print("last line")