import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Sound_page(Base_page):

    not_disturb=(By.XPATH,'//*[@text="Do Not Disturb"]')  # 勿扰模式
    s1_ringtone=(By.XPATH,'//*[@text="SIM1 ringtone"]')  # sim1铃声
    s2_ringtone=(By.XPATH,'//*[@text="SIM2 ringtone"]')  # sim2铃声
    notice_sound=(By.XPATH,'//*[@text="Notification sound"]')  # 通知提示音
    dts=(By.XPATH,'//*[@text="DTS Sound"]')  # DTS音效
    haptic=(By.XPATH,'//*[@text="Haptic vibration"]')  # 触感震动
    increasing=(By.XPATH,'//*[@text="Increasing incoming ringtone"]')  # 来电铃声渐响
    vibrate_for_calls=(By.XPATH,'//*[@text="Vibrate for calls"]')  # 来电震动
    advanced_options=(By.XPATH,'//*[@text="Advanced options"]')  # 高级选项

    def click_notDisturb(self):
        self.get_element(*self.not_disturb).click()

    def click_s1Ringtone(self):
        self.get_element(*self.s1_ringtone).click()
        time.sleep(1)
        self.back_button()

    def click_s2Ringtone(self):
        self.get_element(*self.s2_ringtone).click()
        time.sleep(1)
        self.back_button()

    def click_noticeSound(self):
        self.get_element(*self.notice_sound).click()
        time.sleep(1)
        self.back_button()

    def click_dts(self):
        self.no_element_swipe(*self.dts)
        time.sleep(1)
        self.back_button()

    def click_haptic(self):
        self.no_element_swipe(*self.haptic)
        time.sleep(1)

    def click_increasing(self):
        self.no_element_swipe(*self.increasing)
        time.sleep(1)


    def click_vibrateForCalls(self):
        self.no_element_swipe(*self.vibrate_for_calls)
        time.sleep(1)
        self.back_button()

    def click_advancedOptions(self):
        self.no_element_swipe(*self.advanced_options)


