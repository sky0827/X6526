import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Wifi_advancedoptions_page(Base_page):

    saved_networks=(By.XPATH,'//*[@text="Saved networks"]')  # 保存的网络
    wifi_data_usage=(By.XPATH,'//*[@text="Wi‑Fi data usage"]')  # wifi流量用量
    wifi_direct=(By.XPATH,'//*[@text="Wi‑Fi Direct"]')  # wifi直连

    def click_savedNetwork(self):
        self.get_element(*self.saved_networks).click()
        time.sleep(1)
        self.back_button()

    def click_wifiDataUsage(self):
        self.get_element(*self.wifi_data_usage).click()
        time.sleep(1)
        self.back_button()

    def click_direct(self):
        self.get_element(*self.wifi_direct).click()
        time.sleep(1)
        self.back_button()