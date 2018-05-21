

# dic = str({'1':'111'})
#
# f = open('test','w')
#
# f.write(dic)


# f = open('test','r')

# date = f.read()
#
# f.close()
# print(date)
#
# toDic = eval(date)
# print(toDic['1'])


import json
def foo():
    print('OK')



f = open('dumpdfootest','w')
date = json.dumps(foo())
f.write(date)
f.close()
