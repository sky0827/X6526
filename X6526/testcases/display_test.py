from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.display_pages.display_page import Display_page
from pages.display_pages.display_schedule_page import Display_schedule_page
from pages.display_pages.display_refresh_page import Display_refresh_page
from pages.display_pages.dispaly_eyecare_page import Dispaly_eyecare_page
from pages.display_pages.display_lockscreen_page import Dispaly_lockscreen_page
from pages.display_pages.display_statusbar_page import Dispaly_statusbar_page

class Display_test(Myutil):

    def test_1_dispaly_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        dispaly=Display_page(self.driver)
        displaySchedule=Display_schedule_page(self.driver)
        displayRefresh=Display_refresh_page(self.driver)
        dispalyEyecare=Dispaly_eyecare_page(self.driver)
        displayLockscreen=Dispaly_lockscreen_page(self.driver)
        displayStatusbar=Dispaly_statusbar_page(self.driver)

        setting.click_display()
        dispaly.click_darkTheme()
        dispaly.click_lightTheme()
        dispaly.click_schedule()
        displaySchedule.click_off()
        displaySchedule.click_custom()
        displaySchedule.click_sunset()
        displaySchedule.click_off()

        base.back_button()  # 返会显示与亮度页面

        dispaly.click_autoBrightness()  # 关闭自动调节亮度
        dispaly.click_autoBrightness()  # 开启自动调节亮度
        dispaly.click_keepScreen()  # 开启屏幕常亮
        dispaly.click_keepScreen()  # 关闭屏幕常亮
        dispaly.click_screenTimeout()
        dispaly.click_refresh()
        displayRefresh.click_hz90()
        displayRefresh.click_hz60()
        displayRefresh.click_autoSwitch()

        base.back_button()  # 返会显示与亮度页面

        dispaly.click_eyeCare()
        dispalyEyecare.click_eyeCare()  # 开启护眼模式
        dispalyEyecare.click_eyeCare()  #关闭护眼模式
        dispalyEyecare.click_customSchedule()

        base.back_button()  # 返会显示与亮度页面

        dispaly.click_ultraTouch()
        dispaly.click_fontSize()
        dispaly.click_inadvertentlyMode()  # 关闭防误触
        dispaly.click_inadvertentlyMode()  # 开启防误触
        dispaly.click_autoRotate()  # 开启自动旋转
        dispaly.click_autoRotate()  # 关闭自动旋转
        dispaly.click_lockScreen()
        displayLockscreen.click_lockscreenNoticeSettings()
        displayLockscreen.click_addTextOnlock()
        displayLockscreen.click_lockSreccnOverlay()

        base.back_button()   # 返会显示与亮度页面

        dispaly.click_statusBar()
        displayStatusbar.click_internetSpeed()  # 关闭显示网速
        displayStatusbar.click_internetSpeed()  # 开启显示网速
        displayStatusbar.click_batteryPercentage()  # 关闭显示电量
        displayStatusbar.click_batteryPercentage()  # 开启显示电量
        displayStatusbar.click_noticeIcon()  # 关闭显示通知图标
        displayStatusbar.click_noticeIcon()  # 开启显示通知图标

        base.back_button()  # 返回到显示与亮度界面
        base.back_button()  # 返回到设置界面







