from base.box import Base, BasePage


class RanZhiAddUser(BasePage):

    def add_user(self, user, real_name, sex, dept, role, password1, password2, email):
        driver = self.driver
        driver.sleep(2)
        # 定位后台管理按钮
        # driver.find_element(By.XPATH, '//*[@id="s-menu-superadmin"]/button').click()
        driver.get_element('x,//*[@id="s-menu-superadmin"]/button').click()
        # 定位iframe
        # driver.switch_to.frame(frame)
        driver.switch_to_frame('i,iframe-superadmin')
        # 点击添加成员
        # driver.find_element(By.XPATH, '//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()
        driver.get_element('x,//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()
        # 等待1s
        # time.sleep(1)
        driver.sleep(1)
        # 找到用户名，赋值
        # driver.find_element(By.ID, 'account').send_keys('zhangsan')
        driver.get_element('i,account').send_keys(user)
        # 找到真实姓名，赋值
        # driver.find_element(By.ID, 'realname').send_keys('zhangsan')
        driver.get_element('i,realname').send_keys(real_name)
        # 找到性别，点击
        # driver.find_element(By.ID, 'gender1').click()
        if sex == '男':
            driver.get_element('i,gender1').click()
        else:
            driver.get_element('i,gender2').click()
        # 找到下拉选择框，使用select接收选择对象，利用select_by_index()赋值，相同方法还有select_by_value()等
        # select =Select(driver.find_element(By.ID, 'dept')).select_by_index(2)
        driver.select_by_index('i,dept', dept)
        # # 找到角色下拉选，重复上面下拉选的操作
        # Select(driver.find_element(By.ID, 'role')).select_by_index(2)
        driver.select_by_index('i,role', role)
        # # 找到密码输入框和确认密码输入框输入密码
        # driver.find_element(By.ID, 'password1').send_keys('123456')
        # driver.find_element(By.ID, 'password2').send_keys('123456')
        driver.get_element('i,password1').send_keys(password1)
        driver.get_element('i,password2').send_keys(password2)
        # # 找到邮件输入框，输入邮箱地址
        # driver.find_element(By.ID, 'email').send_keys('123456@163.com')
        driver.get_element('i,email').send_keys(email)
        # # 找到保存按钮，点击
        # driver.find_element(By.ID, 'submit').click()
        driver.get_element('i,submit').click()

    def add_user_by_csv_data(self,data):
        driver = self.driver
        driver.sleep(2)
        # 定位后台管理按钮
        # driver.find_element(By.XPATH, '//*[@id="s-menu-superadmin"]/button').click()
        driver.get_element('x,//*[@id="s-menu-superadmin"]/button').click()
        # 定位iframe
        # driver.switch_to.frame(frame)
        driver.switch_to_frame('i,iframe-superadmin')
        # 点击添加成员
        # driver.find_element(By.XPATH, '//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()
        driver.get_element('x,//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()
        for i in data:
            driver.get_element('i,account').send_keys(i[0])
            driver.get_element('i,realname').send_keys(i[1])
            if i[2] == '男':
                driver.get_element('i,gender1').click()
            else:
                driver.get_element('i,gender2').click()
            driver.select_by_index('i,dept', i[3])
            driver.select_by_index('i,role', i[4])
            driver.get_element('i,password1').send_keys(i[5])
            driver.get_element('i,password2').send_keys(i[6])
            driver.get_element('i,email').send_keys(i[7])
            driver.get_element('i,submit').click()
            driver.sleep(2)
            driver.get_element('l,添加成员').click()

if __name__ == '__main__':
    driver = Base('c')

