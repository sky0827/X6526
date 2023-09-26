from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Notices_page(Base_page):

    lock_screen=(By.XPATH,'//*[@text="Lock Screen"]')  # 锁屏通知
    banners=(By.XPATH,'//*[@text="Banners"]')  # 悬浮通知
    more_settings=(By.XPATH,'//*[@text="More Settings"]')  # 更多通知设置

    def click_lockScreen(self):
        self.get_element(*self.lock_screen).click()

    def click_banners(self):
        self.get_element(*self.banners).click()
        time.sleep(1)
        self.back_button()

    def click_moreSettings(self):
        self.get_element(*self.more_settings).click()



