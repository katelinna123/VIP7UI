'''
功能描述：定义在控制台输出日志的方法，提供给其他模块使用
编写人：tom
编写日期：2021/2/6

步骤分析：1、定义log方法
            1.1定义输出级别和输出方式
        2、返回log方法
            2.1提前定义调用对象，方便其他模块使用
'''


import unittest
from driver import Driver
from log import logger
from readExcel import ReadExcle

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info('测试类开始执行---')
        # cls.excel_data = ReadExcle().read()
        cls.driver= Driver().startUp()

    def setUp(self):
        logger.info('测试用例开始执行')
        self.driver.launch_app()
    # def test_0001(self):
    #     logger.info('用例执行中')
    def tearDown(self):
        logger.info('测试用例执行完毕')
        self.driver.close_app()
    @classmethod
    def tearDownClass(cls):
        logger.info('测试类执行完毕')
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()