import unittest
from base.box import Base, CsvHelp
from ddt import ddt, data, unpack
from pages.ranzhi_add_user import RanZhiAddUser
from pages.ranzhi_login import RanZhiLogin




@ddt
class RanZhiAddUserCase(unittest.TestCase):
    user_data = CsvHelp().get_csv_data(r'..\data\test_add_user.csv')

    # print(user_data)
    def setUp(self):
        # 实例化chrome浏览器对象,并登录
        self.driver = Base('c')
        RanZhiLogin(self.driver).ran_zhi_login('admin', '123456')

    def tearDown(self):
        # 关闭页面
        self.driver.close()

    @data(user_data)
    @unpack
    def test_add_user(self, user, real_name, sex, dept, role, password1, password2, email):
        print(user)
        RanZhiAddUser(self.driver).add_user(user, real_name, sex, int(dept), int(role), password1, password2, email)
        self.driver.sleep(2)
        result = self.driver.get_elements('c,text-center')[-1].text.split(' ')[2]
        self.assertEqual(self.user[0], result, msg='%s添加失败' % self.user[0])

if __name__ == '__main__':
    unittest.main()