import time
import unittest
from base.html_test_runner import HTMLTestRunner




class RanzhiRunner:
    def runner(self):
        '''收集并运行用例'''
        # 实例化 TestSuite 类，创建测试套件
        suite = unittest.TestSuite()
        # 添加测试用例到测试套件中
        # dir = r'C:\Users\Administrator\PycharmProjects\selenium09' #绝对路径
        dir = 'cases' #相对路径
        # suite.addTests(unittest.TestLoader().discover(start_dir=dir,pattern='se1112_case1.py'))
        suite.addTests(unittest.TestLoader().discover(start_dir=dir, pattern='ranzhi*.py'))
        # 创建报告文件,b是二进制
        t = time.strftime('%Y-%m-%d_%H-%M-%S')
        report_path = 'results/reports/ranzhi_report%s.html' % t
        report_file = open(report_path, 'wb')

        # 实例化HTMLTestRunner类，运行用例和把测试结果写入到报告文件
        html_test_runner = HTMLTestRunner(stream=report_file,
                       title='然之自动化测试报告',
                       description='报告详细详细')
        # 运行用例
        html_test_runner.run(suite)
        # 关闭报告文件，如果不关闭有可能会导致报告内容为空
        report_file.close()

if __name__ == '__main__':
    RanzhiRunner().runner()