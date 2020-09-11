from base.box import Base, BasePage
from pages.ranzhi_login import RanZhiLogin


class RanZhiSendBlog(BasePage):
    def send_blog(self):
        driver = self.driver
        driver.sleep(2)
        driver.get_element('x,//*[@id="s-menu-4"]/button').click()
        driver.switch_to_frame('i,iframe-4')
        driver.get_element('x,//*[@id="mainNavbar"]/div[2]/ul/li[3]').click()
        driver.sleep(1)
        driver.get_element('x,/html/body/div/div/div[1]/div[1]').click()
        driver.sleep(1)

        driver.get_element('i,categories_chosen').click()
        driver.get_element('x,//*[@id="categories_chosen"]/div/ul/li[1]').click()

        driver.get_element('i,users_chosen').click()
        # driver.get_element('x,//*[@id="users_chosen"]/div/ul/li[1]').click()
        l = driver.get_elements('c,active-result')
        print(len(l))
        for i in l:
            print(i.text)

        driver.get_element('i,groups1').click()

        driver.get_element('i,title').send_keys('MyBlog')

        driver.get_element('i,keywords').send_keys('life')

        driver.switch_to_frame('x,//*[@id="ajaxForm"]/table/tbody/tr[6]/td/div[2]/div[2]/iframe')

        driver.get_element('c,article-content').send_keys('life is wonderful!')

        driver.switch_to_parent_frame()

        # driver.get_element('i,submit').click()

    def send_blog_by_params(self, categories_chosen, private, users_chosen, group, title, keywords, article_content):
        driver = self.driver
        driver.get_element('x,//*[@id="s-menu-4"]/button').click()
        driver.switch_to_frame('i,iframe-4')
        driver.get_element('x,//*[@id="mainNavbar"]/div[2]/ul/li[3]').click()
        driver.sleep(1)
        driver.get_element('x,/html/body/div/div/div[1]/div[1]').click()
        driver.sleep(1)

        driver.get_element('i,categories_chosen').click()
        # print('x,//*[@id="categories_chosen"]/div/ul/li[%d]' % categories_chosen)
        driver.get_element('x,//*[@id="categories_chosen"]/div/ul/li[%d]' % categories_chosen).click()
        # 是否为私密，私密不输入授权用户，和授权分组
        if private == 1:
            driver.get_element('i,private').click()
        else:
            driver.get_element('i,users_chosen').click()
            driver.get_element('x,//*[@id="users_chosen"]/div/ul/li[%d]' % users_chosen).click()
            # 选择授权用户可能有多个
            # users = users_chosen.split(',')
            # user_selects = driver.get_elements('c,active-result')
            # for i in user_selects:
            #     if us
            driver.get_element('i,groups%d'% group).click()
        driver.get_element('i,title').send_keys(title)

        driver.get_element('i,keywords').send_keys(keywords)

        driver.switch_to_frame('x,//*[@id="ajaxForm"]/table/tbody/tr[6]/td/div[2]/div[2]/iframe')

        driver.get_element('c,article-content').send_keys(article_content)

        driver.switch_to_parent_frame()

        driver.get_element('i,submit').click()

if __name__ == '__main__':
    driver = Base('c')

    RanZhiLogin(driver).ran_zhi_login('admin', '123456')

    RanZhiSendBlog(driver).send_blog_by_params(1,0,1,1,'111','111','hello')