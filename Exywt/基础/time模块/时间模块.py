

import  time


# print(time.asctime() + "********") asctime将当前时间格式化为字符串
# print(help(time))             时间戳

# print(time.time())

# time.sleep(2)
# print(time.clock()) #计算cpu执行时间

#
# print(time.gmtime()) #time.struct_time(tm_year=2018, tm_mon=1, tm_mday=4, tm_hour=8, tm_min=40, tm_sec=59, tm_wday=3, tm_yday=4, tm_isdst=0)

#本地时间
# print(time.localtime()) #time.struct_time(tm_year=2018, tm_mon=1, tm_mday=4, tm_hour=16, tm_min=45, tm_sec=14, tm_wday=3, tm_yday=4, tm_isdst=0)

#formart 字符串时间
# print(time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime()))  #2018-01-04  17:09:59 *****


#*******strptime 将字符串解析为字符元组
# print(time.strptime('2018-01-04  17:09:59',"%Y-%m-%d  %H:%M:%S"))
#time.struct_time(tm_year=2018, tm_mon=1, tm_mday=4, tm_hour=17, tm_min=9, tm_sec=59, tm_wday=3, tm_yday=4, tm_isdst=-1)

# a = time.strptime('2018-01-04  17:09:59',"%Y-%m-%d  %H:%M:%S")
# print(a.tm_year)
# print(a.tm_mon)
# print(a.tm_mday)

#*******

# print(time.ctime())     #Thu Jan  4 17:21:57 2018   格式一定的
#1970
# print(time.ctime(1524566789))


#结构化时间  转换为时间戳
print(time.mktime(time.localtime()))    #1515058002.0


import datetime

# print(datetime.datetime.now())  #2018-01-04 17:28:12.779053