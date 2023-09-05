from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.hotspot_pages.hotspot_page import Hotspot_page
from pages.hotspot_pages.hotspot_hotspotsettings_page import Hotspot_hotspotsettings_page
from pages.hotspot_pages.hotspot_connection_page import Hotspot_connection_page

class Hotspot_test(Myutil):

    def test_1_hotspot_info(self):
        setting=Setting_page(self.driver)
        hotspot=Hotspot_page(self.driver)
        hotspot_hotspotsettings=Hotspot_hotspotsettings_page(self.driver)
        base=Base_page(self.driver)
        hotspot_connection=Hotspot_connection_page(self.driver)

        setting.click_hotspot()
        hotspot.click_personalHotspot()  # 开启个人热点
        hotspot.click_hotspotSettings()
        hotspot_hotspotsettings.click_name()
        hotspot_hotspotsettings.click_password()
        hotspot_hotspotsettings.click_security()
        hotspot_hotspotsettings.click_apBand()

        base.back_button()  # 返回热点界面

        hotspot.click_shareHotspot()
        hotspot.click_connectionManagement()
        hotspot_connection.click_blocklist()
        hotspot_connection.click_oneTime()
        hotspot_connection.click_maximum()

        base.back_button()  # 返回热点界面

        hotspot.click_turnOffHotspot()  # 开启自动关闭热点
        hotspot.click_turnOffHotspot()  # 关闭自动关闭热点

        # hotspot.click_usbTethering()  # 开启usb网络
        # hotspot.click_usbTethering()  # 关闭usb网络
        hotspot.click_bluetoothTethering()  # 开启蓝牙网络
        hotspot.click_bluetoothTethering()  # 关闭蓝牙网络

        hotspot.click_personalHotspot()  # 关闭个人热点

        base.back_button()  # 返回设置界面

