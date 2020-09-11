from base.box import Base
from pages.ranzhi_add_user import RanZhiAddUser
from pages.ranzhi_delete_user_by_user_name import RanZhiDeleteUser
from pages.ranzhi_deleteblog import RanZhiDeleteBlog
from pages.ranzhi_login import RanZhiLogin
from pages.ranzhi_send_blog import RanZhiSendBlog

driver = Base('c')
RanZhiLogin(driver).ran_zhi_login('admin', '123456')
driver.implicitly_wait(10)
driver.switch_to_default_content()
driver.get_element('x,//*[@id="s-menu-superadmin"]/button').click()
# RanZhiAddUser(driver).add_user('mike', 'mike', '女', 2, 1, '123456', '123456', 'mike@qq.com')
# driver.switch_to_default_content()
# RanZhiSendBlog(driver).send_blog_by_params(1,0,2,3,'添加一个博客','博客','这是我写的第一个博客')
# driver.switch_to_default_content()
# RanZhiDeleteBlog(driver).delete_blog()
# driver.switch_to_default_content()
# RanZhiDeleteUser(driver).delete('mike')