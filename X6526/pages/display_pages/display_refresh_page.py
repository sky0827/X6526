import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Display_refresh_page(Base_page):

    hz_90=(By.XPATH,'//*[contains(@text,"High refresh")]')
    hz_60=(By.XPATH,'//*[contains(@text,"Regular refresh")]')
    auto_switch=(By.XPATH,'//*[@text="Auto-switch Refresh Rate"]')  # 自动调节刷新率

    def click_hz90(self):
        self.get_element(*self.hz_90).click()
        time.sleep(1)

    def click_hz60(self):
        self.get_element(*self.hz_60).click()
        time.sleep(1)

    def click_autoSwitch(self):
        self.get_element(*self.auto_switch).click()
        time.sleep(1)