import unittest
from base.box import Base, CsvHelp
from ddt import ddt, data, unpack
from pages.ranzhi_add_user import RanZhiAddUser
from pages.ranzhi_delete_user_by_user_name import RanZhiDeleteUser
from pages.ranzhi_deleteblog import RanZhiDeleteBlog
from pages.ranzhi_login import RanZhiLogin
from pages.ranzhi_send_blog import RanZhiSendBlog



# data = CsvHelp().get_csv_data(r'C:\Users\THINK\Desktop\test44.csv')
@ddt
class SuiBia(unittest.TestCase):
    csv_data = CsvHelp().get_csv_data(r'data\test44.csv')

    def setUp(self):
        self.driver = Base('c')

    def tearDown(self):
        # self.driver.switch_to_default_content()
        self.driver.close()

    @data(*csv_data)
    @unpack
    def test_001(self, user, password):
        RanZhiLogin(self.driver).ran_zhi_login(user, password)
        self.driver.sleep(2)
        result = self.driver.get_element('x,/html/body/div[2]/div/div/div[1]/div').text
        self.assertIn('登录失败', result, msg='随便都能登录')

    @unittest.skip('stop')
    def test_01(self):
        for i in self.users:
            RanZhiLogin(self.driver).ran_zhi_login(*i)
            self.driver.sleep(2)
            result = self.driver.get_element('x,/html/body/div[2]/div/div/div[1]/div').text
            self.assertIn('登录失败', result, msg='随便都能登录')

    @unittest.skip('stop')
    def test_1(self):
        RanZhiAddUser(self.driver).add_user(*self.user)
        self.driver.sleep(2)
        result = self.driver.get_elements('c,text-center')[-1].text.split(' ')[2]
        self.assertEqual(self.user[0], result, msg='%s添加失败' % self.user[0])

    @unittest.skip('stop')
    def test_2(self):
        RanZhiSendBlog(self.driver).send_blog_by_params(*self.blog)
        self.driver.sleep(2)
        result = self.driver.get_elements('c,card-heading')[0].text
        self.assertEqual(self.blog[4], result, msg='添加博客失败')

    @unittest.skip('stop')
    def test_3(self):
        RanZhiDeleteBlog(self.driver).delete_blog()
        result = []
        self.driver.sleep(2)
        for i in self.driver.get_elements('c,card-heading'):
            print(i.text)
            result.append(i.text)
        self.assertNotIn(self.blog[4], result, msg='%s删除失败' % self.blog[4])

    @unittest.skip('stop')
    def test_4(self):
        RanZhiDeleteUser(self.driver).delete('mike')


if __name__ == '__main__':
    unittest.main()

# driver = Base('c')
# RanZhiLogin(driver).ran_zhi_login('admin', '123456')
# driver.switch_to_default_content()
# RanZhiAddUser(driver).add_user('mike', 'mike', '女', 2, 1, '123456', '123456', 'mike@qq.com')
# driver.switch_to_default_content()
# RanZhiSendBlog(driver).send_blog_by_params(1,0,2,3,'添加一个博客','博客','这是我写的第一个博客')
# driver.switch_to_default_content()
# RanZhiDeleteBlog(driver).delete_blog()
# driver.switch_to_default_content()
# RanZhiDeleteUser(driver).delete('mike')
