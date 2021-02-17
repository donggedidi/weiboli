from selenium.webdriver.common.by import By
"""homepage"""
me=By.XPATH,"//*[@text='我的']"
update_next=By.XPATH,"//*[contains(@text,'下次再说')]"

"""mine"""
login_image=By.ID,"com.example.my.myapplication:id/head_img"
setting_btn=By.ID,"com.example.my.myapplication:id/personal_setting"
login_account=By.ID,"com.example.my.myapplication:id/user_name"

"""login"""
account_id=By.ID,"com.example.my.myapplication:id/et_user_name"
password_id=By.ID,"com.example.my.myapplication:id/et_psw"
account_text=By.XPATH,"//*[contains(@text,'请输入用户名')]"
password_text=By.XPATH,"//*[@text='请输入密码']"
login_btn=By.ID,"com.example.my.myapplication:id/btn_login"
not_exist=By.XPATH,"//*[@text='用户不存在']"
got_it_btn=By.XPATH,"//*[@text='我知道了']"
fail_login=By.ID,"com.example.my.myapplication:id/alertTitle"
error=By.ID,"android:id/message"

"""logout"""
logout_btn=By.ID,"com.example.my.myapplication:id/setting_quit"