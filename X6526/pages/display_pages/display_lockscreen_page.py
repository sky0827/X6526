import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Dispaly_lockscreen_page(Base_page):

    lockscreen_notice_settings=(By.XPATH,'//*[@text="Lock screen notification display Settings"]')  # 锁屏通知设置
    add_text_onlock=(By.XPATH,'//*[@text="Add text on lock screen"]')  # 添加锁屏文字
    lock_screen_overlay=(By.XPATH,'//*[@text="Lock screen overlay"]')  # 覆盖锁屏

    def click_lockscreenNoticeSettings(self):
        self.get_element(*self.lockscreen_notice_settings).click()
        time.sleep(1)
        self.back_button()

    def click_addTextOnlock(self):
        self.get_element(*self.add_text_onlock).click()
        time.sleep(1)
        self.back_button()
        self.back_button()

    def click_lockSreccnOverlay(self):
        self.get_element(*self.lock_screen_overlay).click()
        time.sleep(1)
        self.back_button()