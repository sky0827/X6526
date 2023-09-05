import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Sim_callsettings_page(Base_page):

    flash_for_calls=(By.XPATH,'//*[@text="Flash for Calls"]')  # 来电闪光灯
    auto_record_calls=(By.XPATH,'//*[@text="Auto-record Calls"]')  # 自动通话录音
    unkunown_number=(By.XPATH,'//*[@text="Unknown Numbers Identification"]')  # 陌生号码识别
    sim_network_settings=(By.XPATH,'//*[@text="SIM & Network Settings"]')  # sim卡与网络
    sounds_vibration=(By.XPATH,'//*[@text="Sounds & Vibration"]')  # 声音和震动
    caller_id_display=(By.XPATH,'//*[@text="Caller ID Display"]')  # 来电显示
    advanced_settings=(By.XPATH,'//*[@text="Advanced Settings"]')  # 高级设置
    about=(By.XPATH,'//*[@text="About"]')  # 关于

    def click_flashForCalls(self):
        self.get_element(*self.flash_for_calls).click()

    def click_autoRecordCalls(self):
        self.get_element(*self.auto_record_calls).click()

    def click_unknownNumber(self):
        self.get_element(*self.unkunown_number).click()
        time.sleep(1)
        self.back_button()

    def click_simNumberSettings(self):
        self.get_element(*self.sim_network_settings).click()
        time.sleep(1)
        self.back_button()

    def click_soundsVibration(self):
        self.get_element(*self.sounds_vibration).click()
        time.sleep(1)
        self.back_button()

    def click_callerIdDisplay(self):
        self.get_element(*self.caller_id_display).click()
        time.sleep(1)
        self.back_button()

    def click_advancedSettings(self):
        self.get_element(*self.advanced_settings).click()
        time.sleep(1)
        self.back_button()

    def click_about(self):
        self.get_element(*self.about).click()
        time.sleep(1)
        self.back_button()