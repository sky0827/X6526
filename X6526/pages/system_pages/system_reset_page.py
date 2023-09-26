from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class System_reset_page(Base_page):

    reset_wifi=(By.XPATH,'//*[@text="Reset Wi-Fi settings"]')  # 重置无线
    reset_app=(By.XPATH,'//*[@text="Reset app preferences"]')  # 重置应用
    reset_calibration=(By.XPATH,'//*[@text="Reset calibration parameters"]')  # 重置校准参数
    reset_phone=(By.XPATH,'//*[@text="Erase all data"]')  # 重置手机

    def click_resetWifi(self):
        self.get_element(*self.reset_wifi).click()
        time.sleep(1)
        self.back_button()

    def click_resetApp(self):
        self.get_element(*self.reset_app).click()
        time.sleep(1)
        self.back_button()

    def click_resetCalibration(self):
        self.get_element(*self.reset_calibration).click()
        time.sleep(1)
        self.back_button()

    def click_resetPhone(self):
        self.get_element(*self.reset_phone).click()
        time.sleep(1)
        self.back_button()


