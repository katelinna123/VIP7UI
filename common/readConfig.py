'''

功能描述：封装读取配置信息的方法,提供给其他模块使用
编写日期：2021.2.6
编写人：tom
实现步骤：
    1-导入configparser包
    2-定义读取的类
    3-定义读取的方法
    4-在方法中返回相应的信息


'''
import configparser,os

class ReadConfig():

    #获取config.ini的路径
    dir_path = os.path.dirname(os.path.dirname(__file__))
    file_path = dir_path+'/config.ini'

    # 实例化的初始内容，此时实例化ConfigParser类
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file_path,encoding='utf-8')
        # self.sec = self.conf.sections()
        # self.ops = self.conf.options()

    #定义获取数据库账号密码的方法，并以字典的形式返回db的账号密码
    def get_APP_params(self):
        # desire_caps = {
        #     "deviceName": self.conf.get('deviceName'),
        #     "platformName": platformName,
        #     "platformVersion": self.platformVersion,
        #     "appPackage": self.appPackage,
        #     "appActivity": self.appActivity,
        #     "noReset": self.noReset,
        #     "unicodeKeyboard": self.unicodeKeyboard
        # }
        # return desire_caps
        res = self.conf.items('APP')
        return dict(res)
    #返回单个option值
    def readEmail(self,option='all'):
        if option == 'all':
            return dict(self.conf.items('Email'))
        else:
            return self.conf.get('Email',option)
    #读取数据库的配置参数，提供给使用数据库的模块使用



#调试本模块的方法
if __name__ == '__main__':
    rd = ReadConfig()
    # print(rd.get_DB())
    # print(rd.readEmail())
    # print(rd.readEmail('host'))
    # print(rd.get_MYSQL())
    print(rd.get_APP_params())