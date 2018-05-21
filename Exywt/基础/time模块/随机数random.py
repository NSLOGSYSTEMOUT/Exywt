
import  random

print(random.random())

print(random.randint(1,10))     #随机输出1-10的整数包括10

print(random.choice("hela"))    #hela中随机选取一个
print(random.choice([1,2,3,"a","b"]))   #列表中随机选取一个

# print(random.shuffle())  #???原地指定序列


print(random.sample(['123',4,[1,2] ,'c'], 2))       #从列表中随机选取两个

print(random.randrange(1,3))        ##随机输出1-3的整数 不包括3   ******


print('vcconde .....')

def v_code():

    code = " "

    for i in range(5):

        # if  i == random.randint(0,2):
        #
        #     add = random.randrange(10)
        #
        # else:
        #     add = chr(random.randrange(65,91))
        #
        # code += str(add)

        add = random.choice([random.randrange(10), chr(random.randrange(65,91))])
        code += str(add)

    print(code)


v_code()


