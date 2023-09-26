from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Hotspot_hotspotsettings_page(Base_page):

    name=(By.XPATH,'//*[contains(@text,"Name")]')  # 名称
    password=(By.XPATH,'//*[contains(@text,"Password")]')  # 密码
    security=(By.XPATH,'//*[contains(@text,"Security")]')  # 安全
    ap_band=(By.XPATH,'//*[contains(@text,"AP Band")]')  # AP频段

    def click_name(self):
        self.get_element(*self.name).click()
        time.sleep(2)
        self.back_button()
        self.back_button()

    def click_password(self):
        self.get_element(*self.password).click()
        time.sleep(1)
        self.back_button()
        self.back_button()

    def click_security(self):
        self.get_element(*self.security).click()
        time.sleep(1)
        self.back_button()

    def click_apBand(self):
        # self.get_element(*self.ap_band).click()
        # time.sleep(1)
        # self.back_button()
        if self.check_element_click(*self.ap_band) == True:
            self.get_element(*self.ap_band).click()
            time.sleep(1)
            self.back_button()
        else:
            pass

