import unittest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from common.util import Util,logger

class Myutil(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps={}
        desired_caps['deviceName']= '109804038D000076'
        desired_caps['platformName']= 'Android'
        desired_caps['platformVersion']= '13'
        desired_caps['appPackage']= 'com.android.settings'
        desired_caps['appActivity']= '.Settings'
        desired_caps['noReset']=True
        desired_caps['autoAcceptAlerts']=True # 接受条款
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        self.driver.close_app()
        self.driver.quit()
