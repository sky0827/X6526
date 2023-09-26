from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class App_specialapp_page(Base_page):

    install_unknown_apps=(By.XPATH,'//*[@text="Install unknown apps"]')  # 安装未知应用
    wifi_control=(By.XPATH,'//*[@text="Wi-Fi control"]')  # WLAN控制
    modify_system=(By.XPATH,'//*[@text="Modify system settings"]')  # 修改系统设置
    all_files=(By.XPATH,'//*[@text="All files access"]')  # 所有文件访问权限
    not_disturb=(By.XPATH,'//*[@text="Do Not Disturb access"]')  # 勿扰权限
    premium_sms=(By.XPATH,'//*[@text="Premium SMS access"]')  # 付费短信权限
    usage_access=(By.XPATH,'//*[@text="Usage access"]')  # 使用情况访问权限
    enhanced_notice=(By.XPATH,'//*[@text="Enhanced notifications"]')  # 增强型通知
    notice_access=(By.XPATH,'//*[@text="Notification access"]')  # 通知访问权限
    batter=(By.XPATH,'//*[@text="Battery optimization"]')  # 电池优化
    unrestricted_data=(By.XPATH,'//*[@text="Unrestricted data"]')  # 不受流量限制
    device_admin_apps=(By.XPATH,'//*[@text="Device admin apps"]')  # 设备管理应用

    def click_installUnknownApps(self):
        self.get_element(*self.install_unknown_apps).click()
        time.sleep(3)
        self.back_button()

    def click_wifiControl(self):
        self.get_element(*self.wifi_control).click()
        time.sleep(3)
        self.back_button()

    def click_modifySystem(self):
        self.get_element(*self.modify_system).click()
        time.sleep(3)
        self.back_button()

    def click_allFiles(self):
        self.get_element(*self.all_files).click()
        time.sleep(3)
        self.back_button()

    def click_notDisturb(self):
        self.get_element(*self.not_disturb).click()
        time.sleep(1)
        self.back_button()

    def click_premiumSms(self):
        self.get_element(*self.premium_sms).click()
        time.sleep(1)
        self.back_button()

    def click_usageAccess(self):
        self.get_element(*self.usage_access).click()
        time.sleep(3)
        self.back_button()

    def click_enhancedNotice(self):
        # self.get_element(*self.enhanced_notice).click()
        self.no_element_swipe(*self.enhanced_notice)
        time.sleep(1)
        self.back_button()

    def click_noticeAccess(self):
        # self.get_element(*self.notice_access).click()
        self.no_element_swipe(*self.notice_access)
        time.sleep(1)
        self.back_button()

    def click_batter(self):
        # self.get_element(*self.batter).click()
        self.no_element_swipe(*self.batter)
        time.sleep(3)
        self.back_button()

    def click_unrestrictedData(self):
        # self.get_element(*self.unrestricted_data).click()
        self.no_element_swipe(*self.unrestricted_data)
        time.sleep(3)
        self.back_button()

    def click_deviceAdminApps(self):
        # self.get_element(*self.device_admin_apps).click()
        self.no_element_swipe(*self.device_admin_apps)
        time.sleep(1)
        self.back_button()





