from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Special_page(Base_page):

    memfusion=(By.XPATH,'//*[@text="MemFusion"]')  # 内存融合
    magic=(By.XPATH,'//*[@text="Magic Ring"]')  # 灵动岛
    action_gesture=(By.XPATH,'//*[@text="Action and gesture"]')  # 动作与手势
    accessibility=(By.XPATH,'//*[@text="Accessibility"]')  # 无障碍

    def click_memfusion(self):
        self.get_element(*self.memfusion).click()

    def click_magic(self):
        self.get_element(*self.magic).click()

    def click_actionGesture(self):
        self.get_element(*self.action_gesture).click()

    def click_accessibility(self):
        self.get_element(*self.accessibility).click()
