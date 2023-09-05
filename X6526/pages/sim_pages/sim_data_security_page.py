import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Sim_data_security_page(Base_page):

    pseudo=(By.XPATH,'//*[@text="Pseudo base Station Interception"]') # 伪基站拦截
    harassment=(By.XPATH,'//*[@text="Harassment Filter"]')  # 骚扰拦截
    data_settings_usage=(By.XPATH,'//*[@text="Data Settings & Data Usage"]')  # 流量设置及使用

    def click_pseudo(self):
        self.get_element(*self.pseudo).click()
        time.sleep(1)
        self.back_button()

    def click_harassment(self):
        self.get_element(*self.harassment).click()
        time.sleep(1)
        self.back_button()

    def click_dataSettingsUsage(self):
        self.get_element(*self.data_settings_usage).click()
        time.sleep(1)
        self.back_button()




