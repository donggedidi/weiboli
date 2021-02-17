import os,sys
from time import sleep

import allure

sys.path.append(os.getcwd())
import pytest

from base.base_read import BaseRead



from base.base_driver import BaseDriver
from page.page import Page

def read_data():
    return BaseRead().base_read("login.yaml","test_login")

class TestLogin:
    @allure.step(title="setup")
    def setup(self):
        self.driver=BaseDriver().get_driver()
        self.page=Page(self.driver)

    @allure.step(title="teardown")
    def teardown(self):
        sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("account","password","result","status"),read_data())
    def test_login(self,account,password,result,status):
        try:
            sleep(2)
            self.page.home.page_home()
            self.page.mine.page_click_mine()
            self.page.login.page_login(account,password)
            if status == True:
                username=self.page.mine.page_get_login_info()
                # print("{}登录成功".format(username))
                self.page.mine.page_click_setting()
                self.page.setting.page_click_logout()
                assert username==account
                print("{}登录成功".format(username))


            else:
                error=self.page.login.page_result(account,password)
                assert error==result
                print("登录失败提示是是：{}".format(error))
        except Exception as e:
            print("error是：{}".format(e))

