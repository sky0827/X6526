from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Special_action_page(Base_page):

    quick_start=(By.XPATH,'//*[@text="Quick start"]')  # 快速启动
    tapping_wake=(By.XPATH,'//*[@text="Tapping wake"]')  # 轻敲唤醒
    music_gesture=(By.XPATH,'//*[@text="Music gesture"]')  # 音乐手势
    filp_mute=(By.XPATH,'//*[@text="Flip mute"]')  # 翻转静音
    raise_ear=(By.XPATH,'//*[@text="Raise to Ear"]')  # 拿起接听
    lift_wake=(By.XPATH,'//*[@text="Lift to wake"]')  # 拿起设备唤醒
    screenshots=(By.XPATH,'//*[@text="Screenshots"]')  # 截屏

    def click_quickStart(self):
        self.get_element(*self.quick_start).click()
        time.sleep(1)
        self.back_button()

    def click_tappingWake(self):
        self.get_element(*self.tapping_wake).click()
        time.sleep(1)
        self.back_button()

    def click_musicGesturet(self):
        self.get_element(*self.music_gesture).click()
        time.sleep(1)
        self.back_button()

    def click_filpMute(self):
        self.get_element(*self.filp_mute).click()
        time.sleep(1)
        self.back_button()

    def click_raiseEar(self):
        self.get_element(*self.raise_ear).click()
        time.sleep(1)
        self.back_button()

    def click_liftWake(self):
        self.get_element(*self.lift_wake).click()
        time.sleep(1)
        self.back_button()

    def click_screenshots(self):
        self.get_element(*self.screenshots).click()
        time.sleep(1)
        self.back_button()


