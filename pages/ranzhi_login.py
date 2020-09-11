from base.box import Base, BasePage
from pages.ranzhi_add_user import RanZhiAddUser


class RanZhiLogin(BasePage):
    __url = 'http://localhost/ranzhi/www/sys/user-login.html'
    __user_selector = 'i,account'
    __password_selector = 'i,password'
    __submit_selector = 'i,submit'

    def ran_zhi_login(self, user, password):
        driver = self.driver
        driver.open_url(self.__url)
        driver.get_element(self.__user_selector).send_keys(user)
        driver.get_element(self.__password_selector).send_keys(password)
        driver.get_element(self.__submit_selector).click()
        # driver.sleep(1)

if __name__ == '__main__':
    driver = Base('c')
    ran_zhi =RanZhiLogin(driver)
    ran_zhi.ran_zhi_login('admin', '123456')
    add = RanZhiAddUser(driver)
    add.add_user('lisi', 'lisi', '男', 2, 4, '123456', '123456', 'lisi@qq.com')
    # ranzhi_add.ranzhi_add_user(user,realname,sex,dept,role,password1,password2,email)
