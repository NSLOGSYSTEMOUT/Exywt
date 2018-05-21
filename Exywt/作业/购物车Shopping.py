
# a=[[1,2,3],4]         #二级嵌套模式
# print(a[0][1])


# a,b = [2, 3]      #变量对应赋值 a = 2   b = 3
# print(a)
# print(b)

# len(product_list) 计算数组的长度

product_list = [

    ("mac", 9000),
    ("kindle",800),
    ("tesla",900000),
    ("book",105),
    ("bike", 2000),
]

saving = input("please input you saving :")
shoping_car = []

if saving.isdigit():

    while True:

        #打印商品内容

        saving = int(saving)

        # for i in  product_list:
        #     print(product_list.index(i),i)

        # for i in  enumerate(product_list):
        #     print(i)

        # 编号默认从0开始 设置为1
        for i, v in enumerate(product_list, 1):
            print(i, ">>>>>", v)

        choice = input("选择购买商品编号【退出:q】：")

        #验证输入是否合法
        if choice.isdigit():

            choice = int(choice)

            if choice > 0 and choice <= len(product_list):
                #取出用户选择购的商品
                p_item = product_list[choice - 1]
                if p_item[1] < saving:

                    #购买的商品添加到购物车计算余额
                    saving -= p_item[1]
                    shoping_car.append(p_item)
                else:
                    print("余额不足 %s", saving)
                print(p_item[1])
                print(p_item)

            else:
                print("编码不存在")
        elif choice == "q":

            print("-----购买如下商品-----")
            for i in shoping_car:
                print(i)
            print("还剩 %s yuan" % saving)

            break           #跳出循环

        else:
            print("invalid input")







