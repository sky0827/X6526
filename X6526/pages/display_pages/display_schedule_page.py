import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Display_schedule_page(Base_page):

    off=(By.XPATH,'//*[@text="Off"]')  # 关闭
    custom=(By.XPATH,'//*[@text="Custom schedule"]')  # 定时切换
    sunset=(By.XPATH,'//*[@text="Sunset to sunrise"]')  # 日落到日出

    def click_off(self):
        self.get_element(*self.off).click()
        time.sleep(1)

    def click_custom(self):
        self.get_element(*self.custom).click()
        time.sleep(1)

    def click_sunset(self):
        self.get_element(*self.sunset).click()
        time.sleep(1)

