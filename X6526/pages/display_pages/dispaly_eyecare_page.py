import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Dispaly_eyecare_page(Base_page):

    eye_care=(By.XPATH,'//*[@text="Eye Care"]')  # 护眼模式
    custom_schedule=(By.XPATH,'//*[@text="Custom schedule"]')  # 定时开启

    def click_eyeCare(self):
        self.get_element(*self.eye_care).click()
        time.sleep(1)

    def click_customSchedule(self):
        self.get_element(*self.custom_schedule).click()
        time.sleep(1)
        self.back_button()