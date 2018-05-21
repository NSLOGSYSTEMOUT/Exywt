

# def show_info():
#     print("ob")
#
# show_info()
#
# def add(a ,b):
#     return  a+b
#
#
# print(add(10, 20))


def logger(n):

    with open("日志记录","a") as f:

        f.write("end action%s\n" %n)

def action(n):
    print("start with action%s\n" %n)
    logger(n)


action(1)
action(2)
action(3)
