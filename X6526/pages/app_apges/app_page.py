import time

from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class App_page(Base_page):

    applist=(By.XPATH,'//*[@text="App list"]')  # 应用列表
    screen_time=(By.XPATH,'//*[@text="Screen time"]')  # 设备使用时间
    default_app=(By.XPATH,'//*[@text="Default apps"]')  # 默认应用
    app_updata=(By.XPATH,'//*[@text="App Update"]')  # 应用更新
    permission=(By.XPATH,'//*[@text="Permission manager"]')  # 权限管理
    special_app=(By.XPATH,'//*[@text="Special app access"]')  # 特殊应用权限
    dispaly_over_app=(By.XPATH,'//*[@text="Display over other apps"]')  # 显示在其他应用上层
    auto_start_app=(By.XPATH,'//*[@text="Auto-start management"]')  # 自启动管理

    def click_applist(self):
        self.get_element(*self.applist).click()
        time.sleep(2)
        self.back_button()

    def click_screenTime(self):
        self.get_element(*self.screen_time).click()
        time.sleep(1)
        self.back_button()

    def click_defaultApp(self):
        self.get_element(*self.default_app).click()
        time.sleep(1)
        self.back_button()

    def click_appUpdata(self):
        self.get_element(*self.app_updata).click()
        time.sleep(3)
        self.back_button()

    def click_permission(self):
        self.get_element(*self.permission).click()
        time.sleep(2)
        self.back_button()

    def click_specialApp(self):
        self.get_element(*self.special_app).click()

    def click_dispalyOverApp(self):
        self.get_element(*self.dispaly_over_app).click()
        time.sleep(2)
        self.back_button()

    def click_autoStartApp(self):
        self.get_element(*self.auto_start_app).click()
        time.sleep(1)
        self.back_button()


