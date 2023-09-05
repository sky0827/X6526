import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Dispaly_statusbar_page(Base_page):

    internet_speed=(By.XPATH,'//*[@text="Show Internet Speed"]')  # 显示网速
    battery_percentage=(By.XPATH,'//*[@text="Show Battery Percentage"]')  # 显示电量
    notice_icon=(By.XPATH,'//*[@text="Show Notification Icon"]')  # 显示通知图标

    def click_internetSpeed(self):
        self.get_element(*self.internet_speed).click()
        time.sleep(1)

    def click_batteryPercentage(self):
        self.get_element(*self.battery_percentage).click()
        time.sleep(1)

    def click_noticeIcon(self):
        self.get_element(*self.notice_icon).click()
        time.sleep(1)
