from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Myphone_page(Base_page):

    androidVersion=(By.XPATH,'//*[@text="13"]')

    def find_adndroid_version(self):
        self.get_element(*self.androidVersion)
        print('yes')

