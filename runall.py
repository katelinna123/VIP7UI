'''
功能描述：自动化程序的入口，从此处加载用例
编写人：tom
编写日期：2021/2/6

步骤分析：1、定义app参数
        2、启动app
'''
'''
功能描述：读取config.ini文件内容，获取指定的 配置项
编写日期：2020.11.28
编写人：tom
实现步骤：
    1-加载所有的测试用例
        testcase
    2-运行测试用例生产报告
        htmltestrunner
    3-发送邮件通知
        sedemail
'''

import unittest,os,HTMLTestRunner
import configEmail,time


class RunTest():

    def __init__(self):
        # self.time_stamp = time.strftime('%Y%m%d-%H%S%M', time.localtime())
        # self.report_dir = os.path.dirname(__file__) + '/report/report' + self.time_stamp + '.html'
        pass
    def loadCase(self):
        case_dir = os.path.dirname(__file__)+'/testCase'
        suit = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='Pub*.py')
        return suit
    def del_report(self):
        dir_report = os.path.dirname(__file__) + '/report'
        for root,dirs,files in os.walk(dir_report):
            for name in files:
                if name.startswith('report'):
                    os.remove(os.path.join(root,name))
                    # print()
    def loadRunner(self,report_dir):
        self.del_report()
        with open(report_dir,'wb') as file:
            runner = HTMLTestRunner.HTMLTestReportCN(stream=file,title='接口自动化测试报告',description='玩安卓登录接口测试报告')
            runner.run(self.loadCase())


if __name__ == '__main__':
    time_stamp = time.strftime('%Y%m%d-%H%S%M', time.localtime())
    report_dir = os.path.dirname(__file__) + '/report/report' + time_stamp + '.html'
    rt = RunTest()
    rt.loadRunner(report_dir)
    # configEmail.ConfigEmail().sendMail(report_dir)
    # for i in rt.loadCase():
    #     print(i)