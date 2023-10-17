import csv
import os
import time
import pymysql

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, browser):
        """
        传入一个浏览器类型，实例化一个浏览器对象
        :param browser: 形如 c
        """

        # push test
        # push all
        if browser == 'chrome' or browser == 'c':
            self.__driver = webdriver.Chrome()
        elif browser == 'firefox' or browser == 'f':
            self.__driver = webdriver.Firefox()
        elif browser == 'ie' or browser == 'i':
            self.__driver = webdriver.Ie()
        else:
            raise Exception('请给正确的浏览器')

    def open_url(self, url):
        """
        根据传入的网页连接打开网页
        :param url: 网页连接
        :return:
        """
        self.__driver.get(url)

    def __convert_selector_to_locator(self, selector):
        """
        将选择器转化为定位器
        :param selector: 形如'i,account'
        :return: locator 形如(By.ID,account)
        """
        selector_key = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if selector_key == 'id' or selector_key == 'i':
            locator = (By.ID, selector_value)
        elif selector_key == 'xpath' or selector_key == 'x':
            locator = (By.XPATH, selector_value)
        elif selector_key == 'css_selector' or selector_key == 's':
            locator = (By.CSS_SELECTOR, selector_value)
        elif selector_key == 'class' or selector_key == 'c':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_key == 'name' or selector_key == 'n':
            locator = (By.NAME, selector_value)
        elif selector_key == 'tag_name' or selector_key == 't':
            locator = (By.TAG_NAME, selector_value)
        elif selector_key == 'link_text' or selector_key == 'l':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_key == 'partial_link_text' or selector_key == 'p':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        else:
            raise Exception('请使用正确的选择器')
        return locator

    def get_element(self, selector):
        """
        根据传入的选择器获取页面元素
        :param selector: 形如'i,account'
        :return: 页面元素的对象
        """
        locator = self.__convert_selector_to_locator(selector)
        element = self.__driver.find_element(*locator)
        return element

    def get_elements(self, selector):
        """
        根据传入的选择器获取多个对象
        :param selector: 形如'i,account'
        :return: 页面元素对象的列表
        """
        locator = self.__convert_selector_to_locator(selector)
        elements = self.__driver.find_elements(*locator)
        return elements

    def sleep(self, second):
        """
        固定休眠
        :param second: 休眠时常，单位：s
        :return:
        """
        time.sleep(second)

    def implicitly_wait(self, second=10):
        self.__driver.implicitly_wait(second)

    def web_driver_wait(self, selector, second=10):
        locator = self.__convert_selector_to_locator(selector)
        wait = WebDriverWait(self.__driver, second, poll_frequency=0.5)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def switch_to_frame(self, selector):
        """
        根据frame的选择器，进行frame切换
        :param selector: 形如'i,account'
        :return:
        """
        frame = self.get_element(selector)
        self.__driver.switch_to.frame(frame)

    def select_by_index(self, selector, index):
        """
        根据选项的下标选中该选项
        :param selector: 形如'i,account'
        :param index: 选项的下标 形如：1
        :return:
        """
        Select(self.get_element(selector)).select_by_index(index)

    def select_by_value(self, selector, value):
        """
        根据选项的value值选中该选项
        :param selector: 形如'i,account'
        :param value: 选项的value值 形如：'80024'
        :return:
        """
        Select(self.get_element(selector)).select_by_value(value)

    def select_by_visible_text(self, selector, text):
        """
        根据选项的text选中该选项
        :param selector: 形如'i,account'
        :param text: 选项的value值 形如：'管理员'
        :return:
        """
        Select(self.get_element(selector)).select_by_visible_text(text)

    def switch_to_parent_frame(self):
        """
        返回上一层的frame
        :return:
        """
        self.__driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        """
        返回主frame
        :return:
        """
        self.__driver.switch_to.default_content()

    def alert_accept(self):
        """
        确定弹窗
        :return:
        """
        self.__driver.switch_to.alert.accept()

    def alert_dismiss(self):
        """
        取消弹窗
        :return:
        """
        self.__driver.switch_to.alert.dismiss()

    def close(self):
        self.__driver.close()

    def quit(self):
        self.__driver.quit()

    def switch_to_last_window(self):
        """
        切换到最新打开的页面
        :return:
        """
        self.__driver.switch_to.window(self.__driver.window_handles[-1])

    def move_to_element(self, selector):
        action = ActionChains(self.__driver)
        element = self.get_element(selector)
        action.move_to_element(element).perform()

    def save_screen_shot(self, name):
        cmd = 'echo %homepath%'
        dir_name = [i for i in os.popen(cmd)][0]
        path = '%s\\Pictures\\%s.png' % (dir_name.strip(), name)
        print(path)
        self.__driver.save_screenshot(path)

    def execute_js(self, code):
        """
        执行js代码
        :param code:
        :return:
        """
        self.__driver.execute_script(code)


class CsvHelp:
    def get_csv_data(self, file_path, mode='r', encoding='utf8'):
        """
        获取表格文件的数据
        :param file_path: 文件路径
        :param mode: 默认只读
        :param encoding: 默认ｕｔｆ８
        :return: 列表
        """
        file = open(file_path, mode=mode, encoding=encoding)
        csv_data = csv.reader(file)
        flag = True
        res = []
        for i in csv_data:
            if flag:
                flag = False
                continue
            res.append(tuple(i))
        file.close()
        return res


class BasePage:
    def __init__(self, driver_obj: Base):
        self.driver = driver_obj


class MySqlHelp:
    def __init__(self, user, password, host='localhost', port=3306):
        self.db = pymysql.connect(host=host, user=user, password=password, port=port)

    def get_data(self, sql):
        res = []
        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            res.append(tuple(i))
        cursor.close()
        cursor.close()
        self.db.close()
        return res


if __name__ == '__main__':
    driver = Base('c')
    driver.open_url('https://www.baidu.com/')
    driver.execute_js('window.scrollBy(0,2000)')
