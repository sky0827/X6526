import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Bluetooth_page(Base_page):

    bluetooth_button=(By.XPATH,'//*[@text="Bluetooth"]')  # 蓝牙
    device_name=(By.XPATH,'//*[@text="Device Name"]')  # 设备名称
    received_files=(By.XPATH,'//*[@text="Received Files"]')  # 接收的文件
    show_codec_modes=(By.XPATH,'//*[@text="Show Codec Modes"]')  # 显示编解码方式
    all_buttons=(By.XPATH,'//*[@resource-id="android:id/switch_widget"]')

    #  打开蓝牙开关
    def open_bluetoonth_button(self):
        self.blue_button=self.get_all_buttons(*self.all_buttons)[0]  #蓝牙开关按钮
        self.element_button_ison(self.blue_button)

    #  关闭蓝牙开关
    def close_bluetooth_button(self):
        self.blue_button=self.get_all_buttons(*self.all_buttons)[0]  #蓝牙开关按钮
        self.element_button_isoff(self.blue_button)

    def click_deviceName(self):
        time.sleep(1)
        self.no_element_swipe(*self.device_name)
        time.sleep(1)
        self.back_button()
        self.back_button()

    def click_receivedFiles(self):
        self.no_element_swipe(*self.received_files)
        time.sleep(1)
        self.back_button()

    # def click_showCodecModes(self):
    #     self.no_element_swipe(*self.show_codec_modes)
    def open_showCodecMode_button(self):
        self.no_element_swipe(*self.show_codec_modes)
        self.showCodedMode_button=self.get_all_buttons(*self.all_buttons)[1]  # 显示编解码开关按钮
        self.element_button_ison(self.showCodedMode_button)

    def close_showCodecMode_button(self):
        self.no_element_swipe(*self.show_codec_modes)
        self.showCodeMode_button=self.get_all_buttons(*self.all_buttons)[1]
        self.element_button_isoff(self.showCodeMode_button)


