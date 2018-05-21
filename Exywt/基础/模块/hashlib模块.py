
#加密
import  hashlib



# m=hashlib.md5()
# print(m)
#
#
# m.update('hello word'.encode('utf-8'))
#
# print(m)
#
# print(m.hexdigest())
#
# m.update("lex".encode('utf-8'))
# print(m.hexdigest())
#
# print(hashlib.md5("foo".encode('utf-8')).hexdigest())


s = hashlib.sha256()
s.update('hello wrod'.encode("utf8"))
print(s.hexdigest())