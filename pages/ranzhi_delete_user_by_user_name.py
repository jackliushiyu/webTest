from base.box import BasePage, Base
from pages.ranzhi_login import  RanZhiLogin


class RanZhiDeleteUser(BasePage):
    def delete(self,user_name):
        # 获取Base对象
        driver = self.driver
        driver.sleep(2)
        driver.get_element('x,//*[@id="s-menu-superadmin"]/button').click()
        driver.sleep(2)
        driver.switch_to_frame('i,iframe-superadmin')
        driver.get_element('x,//*[@id="mainNavbar"]/div[2]/ul/li[2]').click()
        driver.sleep(2)
        # 通过class获取所有用户信息
        users = driver.get_elements('c,text-center')
        # 删除表头
        users.pop(0)
        #遍历用户信息列表,找到对应的下标,用找到的下标
        # for i in users:
        #     if i.text.split(' ')[2] == user_name:
        #         driver.get_elements('c,deleter')[users.index(i)].click()
        #         driver.alert_accept()
        #         break
        for i in range(len(users)):
            if driver.get_element('x,/html/body/div/div/div/div[2]/div/div/table/tbody/tr[%d]/td[3]'%(i+1)).text == user_name:
                driver.get_element('x,/html/body/div/div/div/div[2]/div/div/table/tbody/tr[%d]/td[11]/a[3]'%(i+1)).click()
                driver.alert_accept()
                break

if __name__ == '__main__':
    driver = Base('c')
    RanZhiLogin(driver).ran_zhi_login('admin', '123456')
    RanZhiDeleteUser(driver).delete('liu')