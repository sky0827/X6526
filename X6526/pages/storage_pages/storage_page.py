from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
from common.util import logger

class Storage_page(Base_page):

    # more_options=(By.XPATH,'//*[@accessibility id="More options"]')
    more_options=(AppiumBy.ACCESSIBILITY_ID,'More options')  # 更多
    low_storage=(By.XPATH,'//*[@resource-id="android:id/title"]')  # 低内存管理
    low_storage_cancel=(By.XPATH,'//*[@text="Cancel"]')  # 取消
    low_storage_disable=(By.XPATH,'//*[@text="Disable"]')  # 关闭
    low_storage_enable=(By.XPATH,'//*[@text="Enable"]')  #开启

    def click_moreOptions(self):
        self.get_element(*self.more_options).click()
        pass

    def click_lowStorage(self):
        self.get_element(*self.low_storage).click()

    def click_lowStorageCancel(self):
        self.get_element(*self.low_storage_cancel).click()

    def click_lowStorageDisable(self):
        self.get_element(*self.low_storage_disable).click()

    def click_lowStorageEnable(self):
        self.get_element(*self.low_storage_enable).click()