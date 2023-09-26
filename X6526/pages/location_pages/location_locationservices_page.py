import time

from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Location_locationservices_page(Base_page):

    emergency_location=(By.XPATH,'//*[@text="Emergency Location Service"]')  # google位置信息精确度
    google_location=(By.XPATH,'//*[@text="Google Location Accuracy"]')  # google位置记录
    google_location_history=(By.XPATH,'//*[@text="Google Location History"]')  # 紧急位置信息服务
    wifi_scanning=(By.XPATH,'//*[@text="Wi‑Fi scanning"]')  # WLAN扫描
    bluettooth=(By.XPATH,'//*[@text="Bluetooth scanning"]')  # 蓝牙扫描

    def click_emergencyLocation(self):
        self.get_element(*self.emergency_location).click()
        time.sleep(2)
        self.back_button()

    def click_googleLocation(self):
        self.get_element(*self.google_location).click()
        time.sleep(2)
        self.back_button()

    def click_googleLocationHistory(self):
        self.get_element(*self.google_location_history).click()
        time.sleep(1)
        self.back_button()

    def click_wifiScanning(self):
        self.get_element(*self.wifi_scanning).click()
        time.sleep(1)
        self.back_button()

    def click_bluettooth(self):
        self.get_element(*self.bluettooth).click()
        time.sleep(1)
        self.back_button()

