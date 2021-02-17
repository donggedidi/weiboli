import allure

import page
from base.base_action import BaseAction


class PageMine(BaseAction):
    @allure.step("点击登录图片")
    def page_click_mine(self):
        self.base_click(page.login_image)

    @allure.step("获取登录成功的信息")
    def page_get_login_info(self):
        return self.base_get_text(page.login_account)

    @allure.step("点击设置页面")
    def page_click_setting(self):
        self.base_click(page.setting_btn)

    def page_mine(self):
        self.page_click_mine()