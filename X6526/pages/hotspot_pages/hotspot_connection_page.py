import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Hotspot_connection_page(Base_page):

    blocklist=(By.XPATH,'//*[@text="Blocklist"]')  # 黑名单
    one_time=(By.XPATH,'//*[@text="One-time Data Limit"]')  # 单次流量限额
    maximum=(By.XPATH,'//*[@text="Maximum Number of Connected Devices"]')  # 最大连接设备数

    def click_blocklist(self):
        self.get_element(*self.blocklist).click()
        time.sleep(1)
        self.back_button()

    def click_oneTime(self):
        self.get_element(*self.one_time).click()
        time.sleep(1)
        self.back_button()

    def click_maximum(self):
        self.get_element(*self.maximum).click()
        time.sleep(1)
        self.back_button()
