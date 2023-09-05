import time

from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Sim_page(Base_page):

    data_security=(By.XPATH,'//*[@text="Data & Security"]') # 流量与安全
    intalligent_network=(By.XPATH,'//*[@text="Intelligent Network Optimization"]') # 智能网络优化
    call_settings=(By.XPATH,'//*[@text="Call Settings"]')  # 通话设置
    sms_settings=(By.XPATH,'//*[@text="SMS Settings"]')  # 短信设置

    def click_dataSecurity(self):
        self.get_element(*self.data_security).click()

    def click_intalligentNetwork(self):
        self.get_element(*self.intalligent_network).click()

    def click_callSettings(self):
        self.get_element(*self.call_settings).click()

    def click_smsSettings(self):
        self.get_element(*self.sms_settings).click()
        time.sleep(1)
        self.back_button()
