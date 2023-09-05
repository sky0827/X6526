from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Myphone_page(Base_page):

    e_warranty_card=(By.XPATH,'//*[@text="E-warranty Card"]')  # 电子保卡
    legal_infomation=(By.XPATH,'//*[@text="Legal information"]') # 法律信息
    user_experience=(By.XPATH,'//*[@text="User Experience Improvement Plan"]') # 用户体验改进计划
    more_information=(By.XPATH,'//*[@text="More Information"]') # 更多信息

    def click_eWarrantCard(self):
        self.get_element(*self.e_warranty_card).click()
        time.sleep(6)
        self.back_button()

    def click_legalInfomation(self):
        self.get_element(*self.legal_infomation).click()

    def click_userExperience(self):
        self.get_element(*self.user_experience).click()
        time.sleep(2)
        self.back_button()

    def click_moreInfomation(self):
        self.get_element(*self.more_information).click()
        time.sleep(2)
        self.back_button()



