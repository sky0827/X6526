import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Sim_intelligentnetwork_page(Base_page):

    smart_network=(By.XPATH,'//*[@text="Smart Network Allocation"]')  # 智能网速分配
    smart_dual_channel=(By.XPATH,'//*[@text="Smart Dual Channel"]')  # 智慧双通道

    def click_smartNetwork(self):
        self.get_element(*self.smart_dual_channel).click()

    def click_smartDualChannel(self):
        self.get_element(*self.smart_dual_channel).click()
        time.sleep(1)
        self.back_button()