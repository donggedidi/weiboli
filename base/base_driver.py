from appium import webdriver


class BaseDriver:
    def get_driver(self):
        desired_caps = dict()
        # 手机参数
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '192.168.56.103:5555'  # 应用参数
        # desired_caps['deviceName']='1cbb96ad7d15'
        desired_caps['appPackage'] = 'com.example.my.myapplication'
        desired_caps['appActivity'] = '.activity.MainActivity'
        desired_caps['noReset'] = True
        # desired_caps['newCommandTimeout'] = 2000

        # 输入中文，不报错，但是输入不成功

        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 使用 Uiautomator2 框架(Toast)
        desired_caps['automationName'] = 'Uiautomator2'

        # 获取driver
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
