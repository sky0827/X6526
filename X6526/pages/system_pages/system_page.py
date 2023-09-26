from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class System_page(Base_page):

    languages=(By.XPATH,'//*[contains(@text,"Languages")]')  # 语言和输入法
    data_time=(By.XPATH,'//*[contains(@text,"Date")]')  # 日期和时间
    navigation=(By.XPATH,'//*[@text="System navigation"]')  # 系统导航
    update=(By.XPATH,'//*[@text="System update"]')  # 系统升级
    power=(By.XPATH,'//*[@text="Scheduled power on/off and restart"]')  # 定时开关机
    back_up=(By.XPATH,'//*[@text="Back up to Google Drive"]')  # 备份到云盘
    reset=(By.XPATH,'//*[@text="Reset Phone"]')  # 重置手机
    manual=(By.XPATH,'//*[@text="Manual Guide"]')  # 手册指南

    def click_languages(self):
        self.get_element(*self.languages).click()

    def click_dataTime(self):
        self.get_element(*self.data_time).click()

    def click_navigation(self):
        self.get_element(*self.navigation).click()
        time.sleep(1)
        self.back_button()

    def click_update(self):
        self.get_element(*self.update).click()
        time.sleep(1)
        self.back_button()

    def click_power(self):
        self.get_element(*self.power).click()
        time.sleep(1)
        self.back_button()

    def click_backUp(self):
        self.get_element(*self.back_up).click()
        time.sleep(3)
        self.back_button()

    def click_reset(self):
        self.get_element(*self.reset).click()

    def click_manual(self):
        self.get_element(*self.manual).click()
        time.sleep(3)
        self.back_button()




