'''
功能描述：定义在控制台输出日志的方法，提供给其他模块使用
编写人：tom
编写日期：2021/2/6

步骤分析：1、定义log方法
            1.1定义输出级别和输出方式
        2、返回log方法
            2.1提前定义调用对象，方便其他模块使用
'''

import logging

def log():
    logging.basicConfig(level=logging.INFO,format="%(name)s-%(asctime)s-%(levelno)s-%(levelname)s  -%(filename)s-[line:%(lineno)d]   -%(message)s")
    logger = logging.getLogger("appiumUI")
    return logger
logger = log()
logger.info('123')