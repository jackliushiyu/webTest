# s = 'HelloWorld'
# print(s[0])
# print(len(s))
# print('\033[35;1mYou Lose!!!\033[0m')
# print(type(s))
# s2 = input("按下 enter 键退出，其他任意键显示...\n")
# print(s2)
# l = ['1', '2', '3']
# l.pop()
# print(l[2])
#
# class Good_job:
#     def __init__(self,a):
#         self.a = a
#     def goodJob(self,str):
#         print('%s goodJob' % str)
#         # pass
# gj = Good_job()
# gj.goodJob('lib')


from selenium import webdriver
import time

def main():
    b = webdriver.Chrome()
    b.get('https://www.baidu.com')
    time.sleep(5)
    b.quit()
    pass
if __name__ == '__main__':
    main()