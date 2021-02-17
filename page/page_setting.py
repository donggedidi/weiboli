import page
from base.base_action import BaseAction


class PageSetting(BaseAction):

    def page_click_logout(self):
        self.base_click(page.logout_btn)