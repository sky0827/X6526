import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Sound_advanced_page(Base_page):

    dial_pad_tones=(By.XPATH,'//*[@text="Dial pad tones"]')  # 拨号键盘提示音
    screen_lock_sound=(By.XPATH,'//*[@text="Screen locking sound"]')  # 锁屏提示音
    charging_sounds=(By.XPATH,'//*[@text="Charging sounds"]')  # 充电提示音
    touch_sounds=(By.XPATH,'//*[@text="Touch sounds"]')  # 触摸提示音

    def click_dialPadTones(self):
        self.get_element(*self.dial_pad_tones).click()
        time.sleep(1)

    def click_screenLockSound(self):
        self.get_element(*self.screen_lock_sound).click()
        time.sleep(1)

    def click_chargingSounds(self):
        self.get_element(*self.charging_sounds).click()
        time.sleep(1)

    def click_touchSounds(self):
        self.get_element(*self.touch_sounds).click()
        time.sleep(1)


