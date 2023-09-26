from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.app_apges.app_page import App_page
from pages.app_apges.app_specialapp_page import App_specialapp_page

class App_test(Myutil):

    def test_1_app_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        app=App_page(self.driver)
        app_specialapp=App_specialapp_page(self.driver)

        setting.click_app()
        app.click_applist()
        app.click_screenTime()
        app.click_defaultApp()
        app.click_appUpdata()
        app.click_permission()
        app.click_specialApp()
        app_specialapp.click_installUnknownApps()
        app_specialapp.click_wifiControl()
        app_specialapp.click_modifySystem()
        app_specialapp.click_allFiles()
        app_specialapp.click_notDisturb()
        app_specialapp.click_premiumSms()
        app_specialapp.click_usageAccess()
        app_specialapp.click_enhancedNotice()
        app_specialapp.click_noticeAccess()
        app_specialapp.click_batter()
        app_specialapp.click_unrestrictedData()
        app_specialapp.click_deviceAdminApps()

        base.back_button()  # 返回应用界面

        app.click_dispalyOverApp()
        app.click_autoStartApp()

        base.back_button()  # 返回设置界面
