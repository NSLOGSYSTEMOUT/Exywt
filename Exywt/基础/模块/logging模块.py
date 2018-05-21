


import  logging   #日志 模块


'''
#灵活配置日志级别、日志格式，输出位置 不能输出到控制台的模式

logging.basicConfig(level=logging.DEBUG,   #级别
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a , %d %b %Y %H:%M:%S',
                    filename='logtest.log',
                    filemode='a'
                    )


logging.debug("debug logging1")
logging.info("info logging2")

logging.warning("warning logging")
logging.error("error logging")
logging.critical("critical logging")
'''



logger = logging.getLogger()

#用于写入日志文件 问文件输出流的对象
fh = logging.FileHandler('test.log')

#在创建一个用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')



fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.setLevel(logging.DEBUG)
logger.debug("logger debug ")
logger.info("info logging2")

logger.warning("warning logging")
logger.error("error logging")
logger.critical("critical logging")


import os
import time
import logging


