'''
功能描述：测试用例：发布文章
编写人：tom
编写日期：2021/2/6

步骤分析：1、定义测试类
        2、写测试方法
        3、打印日志


'''
import time
import  unittest
from driver import Driver
from log import logger
from MyTest import MyTest
from readExcel import ReadExcle


class Smalltxtmsg(MyTest):



    def test_public_mes1(self):
        logger.info('执行第一条用例')

        classname_test = self.__class__.__name__
        method_name = self._testMethodName
        test_data = ReadExcle().read(classname_test,method_name)
        logger.info("这是测试数据："+test_data[0])
        self.driver.find_element_by_id('com.ss.android.article.news:id/bpx').click()
        time.sleep(1)
    def test_public_mes2(self):
        logger.info('执行第二条用例')
        self.driver.find_element_by_id('com.ss.android.article.news:id/bpx').click()
        time.sleep(1)
    def test_public_mes3(self):
        logger.info('执行第三条用例')
        self.driver.find_element_by_id('com.ss.android.article.news:id/bpx').click()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()

