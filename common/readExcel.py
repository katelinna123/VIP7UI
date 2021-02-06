'''

功能描述：封装读取用例参数的类和方法
编写日期：2021.2.6
编写人：tom
实现步骤：
    1-导包
    2-打开目标文件
    3-获取sheet页
    4-设计获取数据方法
      4.1判断classname是否一致
      4.2判断methodname是否一致
      4.3以上两个都一致后返回对应行数的testdata数据
'''
# #导入需要的包，操作Excel的xlrd包，以及操作本地的os包
import os,xlrd
#
# #获取当前项目的目录
data_dir = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
#
# #定义读取Excel的类
class ReadExcle():

    #定义初始化方法，每次初始化时打开文件，读取固定的sheet表
    def __init__(self):
        data = data_dir + '/testData' + '/data.xlsx'
        self.file = xlrd.open_workbook(data)
        self.sheet = self.file.sheet_by_index(0)
        # self.value = self.sheet.cell_value()
    # 读取表中所有的用例，并返回指定的用例数据
    def read(self,classname,methodname):
        list_data = []
        n = self.sheet.nrows
        print(n)
        for i in range(1,n):
            if self.sheet.cell_value(i-1,0)==classname and self.sheet.cell_value(i-1,1) == methodname:
                list_data.append(self.sheet.cell_value(i-1,2))
        return list_data
        # print(self.sheet.cell_value(0,1))
if __name__ == '__main__':
    va = ReadExcle()
    print(va.read(2,'test_small_message_normal'))