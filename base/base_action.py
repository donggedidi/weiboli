import pytest


from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

class BaseAction:
    def __init__(self,driver):
        self.driver=driver

    def base_find_element(self,feature,time=30,poll=0.2):
        # print("查找{}".format(feature))
        return WebDriverWait(self.driver,time,poll).until(lambda x:x.find_element(*feature))

    def base_find_elements(self,feature,time=30,poll=0.2):
        # print("查找{}".format(feature))
        return WebDriverWait(self.driver,time,poll).until(lambda x:x.find_elements(*feature))

    def base_click(self,feature):

        # print("准备点击{}".format(feature))
        el=self.base_find_element(feature)
        # print("找到{}了".format(feature))
        el.click()

    def base_get_text(self,feature):
        text=self.base_find_element(feature).text
        return text

    def base_input(self,feature,value):
        input_box=self.base_find_element(feature)
        input_box.clear()
        input_box.send_keys(value)

    def base_if_exist(self, loc):
        try:

            if self.base_find_element(loc, time=2):

                return True
        except Exception as e:

            return False

    def base_if_exists(self, loc):
        try:

            if self.base_find_elements(loc, time=2):

                return True
        except Exception as e:

            return False

    def base_tap(self,x_value,y_value):
        TouchAction(self.driver).tap(x=x_value,y=y_value).perform()

