from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class System_data_page(Base_page):

    auto_set=(By.XPATH,'//*[@text="Auto-set Time"]')  # 自动设置时间
    locale_default=(By.XPATH,'//*[@text="Use Locale Default"]')  # 使用默认语言区域时间
    use_24_hour=(By.XPATH,'//*[@text="Use 24-hour Format"]')  # 使用24小时制
    set_time_auto=(By.XPATH,'//*[@text="Set Time Zone Automatically"]')  # 自动设置时区
    select_time=(By.XPATH,'//*[@text="Select Time Zone"]')  # 手动选择时区

    def click_autoSet(self):
        self.get_element(*self.auto_set).click()
        time.sleep(1)
        self.back_button()

    def click_localeDefault(self):
        self.get_element(*self.locale_default).click()
        time.sleep(1)

    def click_use24Hour(self):
        self.get_element(*self.use_24_hour).click()
        time.sleep(1)

    def click_setTimeAuto(self):
        self.get_element(*self.set_time_auto).click()
        time.sleep(1)

    def click_selectTime(self):
        self.get_element(*self.select_time).click()
        time.sleep(1)
        self.back_button()


