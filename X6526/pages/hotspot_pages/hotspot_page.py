import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Hotspot_page(Base_page):

    personal_hotspot=(By.XPATH,'//*[@text="Personal Hotspot"]')  # 个人热点
    hotspot_settings=(By.XPATH,'//*[@text="Hotspot Settings"]')  # 热点配置
    connection_management=(By.XPATH,'//*[@text="Connection Management"]')  # 连接管理
    turn_off_hotspot=(By.XPATH,'//*[@text="Turn off hotspot automatically"]')  # 自动关闭热点
    # usb_tethering=(By.XPATH,'//*[@text="USB tethering"]')  # usb网络共享
    bluetooth_tethering=(By.XPATH,'//*[@text="Bluetooth tethering"]')  # 蓝牙网络共享
    share_hotspot=(By.XPATH,'//*[@text="Share hotspot"]')

    def click_personalHotspot(self):
        self.get_element(*self.personal_hotspot).click()

    def click_hotspotSettings(self):
        self.get_element(*self.hotspot_settings).click()

    def click_connectionManagement(self):
        self.get_element(*self.connection_management).click()

    def click_turnOffHotspot(self):
        self.get_element(*self.turn_off_hotspot).click()

    # def click_usbTethering(self):
    #     self.get_element(*self.usb_tethering).click()
    #     time.sleep(3)

    def click_bluetoothTethering(self):
        self.get_element(*self.bluetooth_tethering).click()
        time.sleep(3)

    def click_shareHotspot(self):
        self.get_element(*self.share_hotspot).click()
        time.sleep(1)
        self.back_button()

