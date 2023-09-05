from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.bluetooth_pages.bluetooth_page import Bluetooth_page


class Bluetooth_test(Myutil):

    def test_1_bluetooth_info(self):
        setting=Setting_page(self.driver)
        bluetooth=Bluetooth_page(self.driver)
        base=Base_page(self.driver)

        setting.click_bluetooth()
        bluetooth.click_bluetoothButton()  # 打开蓝牙开关
        bluetooth.click_deviceName()
        bluetooth.click_receivedFiles()
        bluetooth.click_showCodecModes()  # 打开显示编解码
        bluetooth.click_showCodecModes()  # 关闭显示编解码
        bluetooth.click_bluetoothButton()  # 关闭蓝牙开关

        base.back_button()  # 返回设置界面
