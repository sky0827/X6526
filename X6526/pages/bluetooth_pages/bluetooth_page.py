import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Bluetooth_page(Base_page):

    bluetooth_button=(By.XPATH,'//*[@text="Bluetooth"]')  # 蓝牙
    device_name=(By.XPATH,'//*[@text="Device Name"]')  # 设备名称
    received_files=(By.XPATH,'//*[@text="Received Files"]')  # 接收的文件
    show_codec_modes=(By.XPATH,'//*[@text="Show Codec Modes"]')  # 显示编解码方式

    def click_bluetoothButton(self):
        self.get_element(*self.bluetooth_button).click()
        time.sleep(2)

    def click_deviceName(self):
        self.no_element_swipe(*self.device_name)
        time.sleep(1)
        self.back_button()
        self.back_button()

    def click_receivedFiles(self):
        self.no_element_swipe(*self.received_files)
        time.sleep(1)
        self.back_button()

    def click_showCodecModes(self):
        self.no_element_swipe(*self.show_codec_modes)


