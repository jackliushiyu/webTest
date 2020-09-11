from base.box import Base
from selenium import webdriver
from selenium.webdriver.common.by import By

# import pymysql
#
#
# db = pymysql.connect(host='localhost', user='root', password='', port=3306)
#
# cursor = db.cursor()
# #  ranzhi.sys_user
# sql = 'select * from  ranzhi.sys_user'
#
# cursor.execute(sql)
#
# print(cursor.execute(sql))
#
# data = cursor.fetchall()
#
# for i in data:
#     print(i)
#
# db.close()

# driver = webdriver.Chrome()
#
# driver.get('https://www.baidu.com/')
# # driver.open_url('https://www.baidu.com/')
# driver.find_element(By.XPATH, '//*[contains(text(),"特朗普")]').click()
# l = driver.window_handles
# driver.switch_to.window(l[-1])
# driver.find_element(By.XPATH, '//*[@id="channel-all"]/div/ul/li[11]/a').click()

driver = Base('c')

driver.open_url('https://www.mail.163.com/')
driver.sleep(2)
driver.switch_to_frame('x,//*[@id="loginDiv"]/iframe')
driver.get_element('x,//*[@id="account-box"]/div[2]/input').send_keys('15243344')

