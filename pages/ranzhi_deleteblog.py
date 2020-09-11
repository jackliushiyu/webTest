from base.box import BasePage, Base
from pages.ranzhi_login import RanZhiLogin


class RanZhiDeleteBlog(BasePage):
    def delete_blog(self):
        driver = self.driver
        driver.sleep(2)
        driver.get_element('x,//*[@id="s-menu-4"]/button').click()
        driver.sleep(1)
        driver.switch_to_frame('i,iframe-4')
        driver.get_element('x,//*[@id="mainNavbar"]/div[2]/ul/li[3]').click()
        driver.sleep(1)
        driver.get_element('x,//*[@id="articles"]/section/div/div[2]/span[4]/a[2]').click()
        driver.alert_accept()

    # def delete_blog_by_title(self,title):
    #     driver = self.driver
    #     driver.sleep(1)
    #     driver.get_element('x,//*[@id="s-menu-4"]/button').click()
    #     driver.sleep(1)
    #     driver.switch_to_frame('i,iframe-4')
    #     driver.get_element('x,//*[@id="mainNavbar"]/div[2]/ul/li[3]').click()
    #     driver.sleep(1)
    #     blogs = driver.get_elements('c,card')
    #     for i in blogs:

if __name__ == '__main__':
    driver = Base('c')
    RanZhiLogin(driver).ran_zhi_login('admin', '123456')
    RanZhiDeleteBlog(driver).delete_blog()
    # RanZhiDeleteBlog(driver).delete_blog_by_title('cs')