from base.base_action import BaseAction
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_mine import PageMine
from page.page_setting import PageSetting


class Page(BaseAction):
    @property
    def home(self):
        return PageHome(self.driver)

    @property
    def mine(self):
        return PageMine(self.driver)

    @property
    def login(self):
        return PageLogin(self.driver)

    @property
    def setting(self):
        return PageSetting(self.driver)