import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Wifi_page(Base_page):

    wifi_button=(By.XPATH,'//*[@text="Wi‑Fi"]')  # wi-fi开关
    add_button=(By.XPATH,'//*[@text="Add Network"]')  # 添加网络
    wifi_preferences=(By.XPATH,'//*[@text="Wi‑Fi Preferences"]')  # WLAN偏好设置
    advanced_options=(By.XPATH,'//*[@text="Advanced Options"]')  # 高级选项

    def click_wifiButton(self):
        self.get_element(*self.wifi_button).click()

    def click_addButton(self):
        # while True:
        #     try:
        #         self.get_element(*self.add_button).click()
        #         break
        #     except NoSuchElementException:
        #         self.driver.swipe(333,1319,333,368)
        self.no_element_swipe(*self.add_button)
        time.sleep(1)
        self.back_button()
        self.back_button()

    def click_wifiPreferences(self):
        self.no_element_swipe(*self.wifi_preferences)
        # while True:
        #     try:
        #         self.get_element(*self.wifi_preferences).click()
        #         break
        #     except NoSuchElementException:
        #         self.driver.swipe(333,1319,333,368)

    def click_advancedOptions(self):
        self.no_element_swipe(*self.advanced_options)
        # while True:
        #     try:
        #         self.get_element(*self.advanced_options).click()
        #         break
        #     except NoSuchElementException:
        #         self.driver.swipe(333,1319,333,368)

