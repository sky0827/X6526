import time

from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Location_page(Base_page):

    location=(By.XPATH,'//*[@text="Location"]')  # 位置信息
    see_all=(By.XPATH,'//*[@text="See all"]')  # 查看所有
    app_location_permissions=(By.XPATH,'//*[@text="App location permissions"]')  # 应用位置权限
    location_services=(By.XPATH,'//*[@text="Location services"]')  # 位置信息服务

    def click_location(self):
        self.get_element(*self.location).click()
        time.sleep(1)

    def click_seeAll(self):
        self.get_element(*self.see_all).click()
        time.sleep(1)
        self.back_button()

    def click_appLocationPermissions(self):
        self.get_element(*self.app_location_permissions).click()
        time.sleep(2)
        self.back_button()

    def click_locationServices(self):
        self.get_element(*self.location_services).click()

