

# 搜索路径：sys.path
import calculate

from calculate import  add,sub      #从模块中调用方法，
print(calculate.add(1,2))

print(add(2,4))
print(sub(2,3))


import Web

# print(Web.main.x)      module 'Web' has no attribute 'main'

from  Web import  main

print(main.x)