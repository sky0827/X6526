from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.location_pages.location_page import Location_page
from pages.location_pages.location_locationservices_page import Location_locationservices_page

class Location_test(Myutil):

    def test_1_location_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        location=Location_page(self.driver)
        location_locationservices=Location_locationservices_page(self.driver)

        setting.click_location()
        location.click_location()  # 关闭
        location.click_location()  # 开启
        location.click_seeAll()
        location.click_appLocationPermissions()
        location.click_locationServices()
        location_locationservices.click_emergencyLocation()
        location_locationservices.click_googleLocation()
        location_locationservices.click_googleLocationHistory()
        location_locationservices.click_wifiScanning()
        location_locationservices.click_bluettooth()

        base.back_button()  # 返回位置界面
        base.back_button()  # 返回设置界面