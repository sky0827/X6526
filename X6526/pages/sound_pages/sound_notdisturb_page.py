import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Sound_notdisturb_page(Base_page):

    not_disturb=(By.XPATH,'//*[@text="Do Not Disturb"]')  # 勿扰模式
    people=(By.XPATH,'//*[@text="People"]')  # 联系人
    apps=(By.XPATH,'//*[@text="Apps"]')  # 应用
    alarms=(By.XPATH,'//*[@text="Alarms & other interruptions"]')  # 闹钟和其他例外项
    schedules=(By.XPATH,'//*[@text="Schedules"]')  # 时间表
    quick_settings=(By.XPATH,'//*[@text="Duration for Quick Settings"]')  # 在快捷设置中开启时的持续时长
    display_options_notice=(By.XPATH,'//*[@text="Display options for hidden notifications"]')  # 隐藏通知的显示方式

    def click_notDisturb(self):
        self.get_element(*self.not_disturb).click()
        time.sleep(1)

    def click_people(self):
        self.get_element(*self.people).click()
        time.sleep(1)
        self.back_button()

    def click_apps(self):
        self.get_element(*self.apps).click()
        time.sleep(1)
        self.back_button()

    def click_alarms(self):
        self.get_element(*self.alarms).click()
        time.sleep(1)
        self.back_button()

    def click_schedules(self):
        self.get_element(*self.schedules).click()
        time.sleep(1)
        self.back_button()

    def click_quickSettings(self):
        self.get_element(*self.quick_settings).click()
        time.sleep(1)
        self.back_button()

    def click_displayOptionsNotice(self):
        self.get_element(*self.display_options_notice).click()
        time.sleep(1)
        self.back_button()
