from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Special_magic_page(Base_page):

    magic_ring=(By.XPATH,'//*[contains(@text,"Display important")]')  # 灵动岛
    face_unlock=(By.XPATH,'//*[@text="Face Unlock"]')  # 人脸解锁
    background_call=(By.XPATH,'//*[@text="Background Call"]')  # 后台通话
    charging_animation=(By.XPATH,'//*[@text="Charging Animation"]')  # 充电动画
    charge_completion=(By.XPATH,'//*[@text="Charge Completion Reminder"]')  # 充电完成提醒
    low_battery=(By.XPATH,'//*[@text="Low Battery Reminder"]')  # 低电提醒

    def click_magicRing(self):
        time.sleep(1)
        self.get_element(*self.magic_ring).click()
        time.sleep(1)

    def click_faceUnlock(self):
        self.get_element(*self.face_unlock).click()
        time.sleep(1)

    def click_backgroundCall(self):
        self.get_element(*self.background_call).click()
        time.sleep(1)

    def click_chargingAnimation(self):
        self.get_element(*self.charging_animation).click()
        time.sleep(1)

    def click_chargeCompletion(self):
        self.get_element(*self.charge_completion).click()
        time.sleep(1)

    def click_lowBattery(self):
        self.get_element(*self.low_battery).click()
        time.sleep(1)


