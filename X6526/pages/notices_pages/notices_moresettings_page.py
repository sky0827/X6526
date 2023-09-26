from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Notices_moresettings_page(Base_page):

    swipe_lock_screen=(By.XPATH,'//*[@text="Swipe Down on Lock Screen"]')  # 锁屏时可下拉操作
    notices_status_bar=(By.XPATH,'//*[@text="Notification Icons on Status Bar"]')  # 状态栏显示通知图标

    def click_swipeLockScreen(self):
        self.get_element(*self.swipe_lock_screen).click()
        time.sleep(1)
        self.back_button()

    def click_noticesStatusBar(self):
        self.get_element(*self.notices_status_bar).click()
        time.sleep(1)
