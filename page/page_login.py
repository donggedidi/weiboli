import allure

import page
from base.base_action import BaseAction


class PageLogin(BaseAction):
    @allure.step("输入用户名")
    def page_input_account(self,account):
        allure.attach("登录账户是：{}".format(account))
        self.base_input(page.account_id,account)

    @allure.step("输入密码")
    def page_input_password(self,password):
        allure.attach("密码是：{}".format(password))
        self.base_input(page.password_id,password)

    @allure.step("点击登录按钮")
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    @allure.step("判断登录结果")
    def page_result(self,account,password):
        if self.base_if_exist(page.fail_login):
            error=self.base_get_text(page.error)
            self.base_click(page.got_it_btn)
            return error
        # elif len(self.base_find_elements(page.account_text))>1:
        elif len(password)==0:
            pwds=self.base_find_elements(page.password_text)
            # for pwd in pwds:
            #     break

            return pwds[1].text

        elif len(account)==0:
            accs = self.base_find_elements(page.account_text)
            # for acc in accs:
            #     break

            return accs[1].text

        else:
            print("没走上面")


    def page_login(self,account,password):
        self.page_input_account(account)
        self.page_input_password(password)
        self.page_click_login_btn()
