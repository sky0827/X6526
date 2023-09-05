from common.myutil import Myutil
from pages.base_page import Base_page
from pages.myphone_pages.myphone_page import Myphone_page
from pages.setting_page import Setting_page
from pages.myphone_pages.myphone_legal_page import Myphone_legal_page

class Myphone_test(Myutil):

    def test_1_myphone_info(self):
        setting=Setting_page(self.driver)
        myphone=Myphone_page(self.driver)
        base=Base_page(self.driver)
        myphone_legal=Myphone_legal_page(self.driver)

        setting.click_myphone()
        self.driver.swipe(364,1323,364,277) # 下滑到底部

        # 电子保卡
        myphone.click_eWarrantCard()

        # 法律信息
        myphone.click_legalInfomation()
        myphone_legal.click_thirdPartyLicenses()
        myphone_legal.click_googleLgal()
        myphone_legal.click_googlePlaySystem()
        myphone_legal.click_systemWeb()
        myphone_legal.click_termsOfUse()
        myphone_legal.click_privacyPolicy()

        base.back_button()

        # 用户体验改进计划
        myphone.click_userExperience()

        # 更多信息
        myphone.click_moreInfomation()

        base.back_button() # 返回设置界面
