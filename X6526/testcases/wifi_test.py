from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.wifi_pages.wifi_page import Wifi_page
from pages.wifi_pages.wifi_preference_page import Wifi_preference_page
from pages.wifi_pages.wifi_advancedoptions_page import Wifi_advancedoptions_page


class Wifi_test(Myutil):

    def test_1_wifi_info(self):
        setting=Setting_page(self.driver)
        wifi=Wifi_page(self.driver)
        wifi_preference=Wifi_preference_page(self.driver)
        base=Base_page(self.driver)
        wifi_advancedoptions=Wifi_advancedoptions_page(self.driver)


        setting.click_wifi()
        wifi.click_wifiButton()  # 关闭wifi
        wifi.click_wifiButton()  # 开启wifi
        wifi.click_addButton()
        wifi.click_wifiPreferences()
        wifi_preference.click_autoAwitchData()  # 关闭自动切换数据
        wifi_preference.click_autoAwitchData()  # 开启自动切换数据
        wifi_preference.click_askBeforeSwitching()  # 开启切换询问
        wifi_preference.click_askBeforeSwitching()  # 关闭切换询问
        wifi_preference.click_turnOnWifiAuto()  # 开启自动开启wifi
        wifi_preference.click_turnOnWifiAuto()  # 关闭自动开启wifi
        wifi_preference.click_openNetworkNotice()  # 开启打开网络通知
        wifi_preference.click_openNetworkNotice()  # 关闭打开网络通知
        wifi_preference.click_installCertificates()
        wifi_preference.click_networkRatingProvider()

        base.back_button()  # 返回WiFi界面

        wifi.click_advancedOptions()
        wifi_advancedoptions.click_savedNetwork()
        wifi_advancedoptions.click_wifiDataUsage()
        wifi_advancedoptions.click_direct()

        base.back_button()  # 返回wifi界面
        base.back_button()  # 返回设置界面








