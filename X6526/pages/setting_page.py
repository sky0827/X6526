from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Setting_page(Base_page):

    myPhone=(By.XPATH,'//*[@text="我的手机"]')

    def click_myphone(self):
        self.get_element(*self.myPhone).click()