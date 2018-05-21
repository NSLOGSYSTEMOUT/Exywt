# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 下午3:20
# @Author  : ZS
# @Email   : @163.com
# @File    : 异常处理.py
# @Software: PyCharm

'''
while True:

    try:

        number = input("输入序列号")
        i = int(number)
        pass

    except IndexError as e:

        pass

    except ValueError as e:

        pass

    except Exception as  e:

        print(e)
        i = 1
        pass

    else:
        #没有出错时执行
        print('没有出错时执行')
        pass

    finally:

        #最终都会执行
        print('最终都会执行')
        pass

        # raise  Exception("主动触发异常")


print(i)

'''


#自定义异常

class MyException(Exception):

    def __init__(self,message):
        self.message = message



    def __str__(self):
        return self.message




obj = MyException("my exception")

print(obj)


try:

    raise MyException("主动触发的异常错误")

except MyException as e:

    print(e)   #调用 __str__方法并打印出返回值



#assert 条件断言 用于用户强制服从，不服从报错 可以捕获但一般不捕获

# assert 1==3
