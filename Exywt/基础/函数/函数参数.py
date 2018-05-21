



# def print_info(name="zs", age=16):
#
#     print("name is : %s" %name)
#     print("age is : %d" %age)
#
#
# print_info()                        #默认参数
# print_info("zss",1)                 # 必须参数
# print_info(age=12, name="zs")       #关键字参数


# def add(*x):
#     print(x)                        #(1, 2, 3, 4)
#
#     sum = 0
#     for i in x:
#
#         sum += i
#     return sum
#
# print(add(1,2,3,4))



# def print_info(**args):
#
#     print(args)                          #{'name': 'zs', 'job': 'teacher', 'sex': 'man', 'age': 18}
    # print("name is : %s" %name)
    # print("age is : %s" %age)
    # print("sex is : %s" % sex)
    # print("job is : %s" % job)

# print_info(name="zs",age=18,sex="man", job="teacher")


def print_info(*args, **keyword):
    # print(args)                                 #('zs', 18)
    # print(keyword)                              #print_info("zs",18,sex="man", job="teacher")

    for i in keyword:
        print("%s : %s" %(i, keyword[i]))           #job : teacher sex : man


print_info("zs",18,sex="man", job="teacher")

#关于不定长参数 * 放在**左边 默认参数放最左边

