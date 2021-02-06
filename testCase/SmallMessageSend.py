'''
功能描述：测试用例：发布微头条
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


class Smalltxtmsg(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().startUp()
        logger.info('开始执行--微头条发布--测试用例')

    def tearDown(self):
        logger.info('--微头条发布--用例执行完成')
        self.driver.quit()

    def test_public_mes(self):
        self.driver.find_element_by_id('com.ss.android.article.news:id/bpx').click()
        time.sleep(1)
        # 选择微头条
        self.driver.find_elements_by_id('com.ss.android.article.news:id/bxm')[0].click()
        time.sleep(2)
        # 输入文本内容
        self.driver.find_element_by_id('com.ss.android.article.news:id/bmj').send_keys('又是充满活力的一天！喜喜')
        time.sleep(1)

        # 填写完成点击发布
        self.driver.find_element_by_id('com.ss.android.article.news:id/a96').click()


if __name__ == '__main__':
    unittest.main()