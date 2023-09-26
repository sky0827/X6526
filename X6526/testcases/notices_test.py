from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.notices_pages.notices_page import Notices_page
from pages.notices_pages.notices_moresettings_page import Notices_moresettings_page
from pages.notices_pages.notices_lockscreen_page import Notices_lockscreen_page

class Notices_test(Myutil):

    def test_1_notices_info(self):

        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        notices=Notices_page(self.driver)
        notices_lockscreen=Notices_lockscreen_page(self.driver)
        notices_moresettings=Notices_moresettings_page(self.driver)

        setting.click_notices()
        notices.click_lockScreen()
        notices_lockscreen.click_displayRule()

        base.back_button()  # 返回通知界面

        notices.click_banners()
        notices.click_moreSettings()
        notices_moresettings.click_swipeLockScreen()
        notices_moresettings.click_noticesStatusBar()  # 关闭
        notices_moresettings.click_noticesStatusBar()  # 开启

        base.back_button()  # 返回通知界面
        base.back_button()  # 返回设置界面




