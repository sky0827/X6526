from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Notices_lockscreen_page(Base_page):

    display_rule=(By.XPATH,'//*[@text="Display Rule"]')  # 显示规则

    def click_displayRule(self):
        self.get_element(*self.display_rule).click()
        time.sleep(1)
        self.back_button()