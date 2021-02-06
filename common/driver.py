'''
功能描述：启动appium的指定app，通过指定参数运行,返回运行对象
编写人：tom
编写日期：2021/2/6

步骤分析：1、定义app参数
        2、启动app
'''

from appium import webdriver
import os,time
from log import logger
from readConfig import ReadConfig

class Driver():

    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = '4723'
        self.desire_caps = ReadConfig().get_APP_params()
        # self.deviceName = "28f2902"
        # self.platformName = "Android"
        # self.platformVersion = "10"
        # self.appPackage = "com.ss.android.article.news"
        # self.appActivity = "com.ss.android.article.news.activity.MainActivity"
        # self.noReset = True
        # self.unicodeKeyboard = True


    def startUp(self):
        logger.info('启动头条App中---')
        desire_caps = {
            "deviceName":self.desire_caps['devicename'],
            "platformName":self.desire_caps['platformname'],
            "platformVersion": self.desire_caps['platformversion'],
            "appPackage":self.desire_caps['apppackage'],
            "appActivity": self.desire_caps['appactivity'],
            "noReset": self.desire_caps['noreset'],
            "unicodeKeyboard": self.desire_caps['unicodekeyboard']
        }

        driver = webdriver.Remote('http://'+self.ip+':'+self.port+'/wd/hub', desire_caps)
        time.sleep(4)
        logger.info("启动头条App成功！")
        return driver
        # print(desire_caps)

if __name__ == '__main__':
    d = Driver()
    print(d.desire_caps)