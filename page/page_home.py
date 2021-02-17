import allure

import page
from base.base_action import BaseAction


class PageHome(BaseAction):
    @allure.step("查询是否有更新app提示")
    def page_if_update(self):
        if self.base_if_exist(page.update_next):
            print("点击系统更新提示：{}".format(self.base_get_text(page.update_next)))
            self.base_click(page.update_next)

    @allure.step("点击我的")
    def page_click_me(self):
        self.base_click(page.me)

    def page_home(self):
        self.page_if_update()
        self.page_click_me()


