from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.moreconnections_pages.moreconnections_page import Moreconnections_page

class Moreconnections_test(Myutil):

    def test_1_moreconnections_info(self):
        setting=Setting_page(self.driver)
        moreconnections=Moreconnections_page(self.driver)
        base=Base_page(self.driver)

        setting.click_moreconnections()
        moreconnections.click_airplan()  # 开启飞行模式
        moreconnections.click_airplan()  # 关闭飞行模式
        moreconnections.click_vpn()
        moreconnections.click_privateDns()
        moreconnections.click_cast()
        moreconnections.click_usb()
        moreconnections.click_printing()
        moreconnections.click_otg()  # 开启OTG
        moreconnections.click_otg()  # 关闭OTG
        moreconnections.click_nearbyShare()

        base.back_button()  # 返回设置界面



