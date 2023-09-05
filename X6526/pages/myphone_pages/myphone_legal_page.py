from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Myphone_legal_page(Base_page):

    third_party_licenses=(By.XPATH,'//*[@text="Third-party licenses"]') # 第三方许可
    google_legal=(By.XPATH,'//*[@text="Google legal"]') # google法律信息
    google_paly_system=(By.XPATH,'//*[@text="Google Play system update licenses"]') # googleplay系统更新许可
    system_web=(By.XPATH,'//*[@text="System WebView licenses"]') # 系统webview许可
    terms_of_use=(By.XPATH,'//*[@text="Terms of Use"]') # 用户协议
    privacy_policy=(By.XPATH,'//*[@text="Privacy Policy"]') # 隐私政策

    def click_thirdPartyLicenses(self):
        self.get_element(*self.third_party_licenses).click()
        time.sleep(4)
        self.back_button()

    def click_googleLgal(self):
        self.get_element(*self.google_legal).click()
        time.sleep(2)
        self.back_button()

    def click_googlePlaySystem(self):
        self.get_element(*self.google_paly_system).click()
        time.sleep(1)
        self.back_button()

    def click_systemWeb(self):
        self.get_element(*self.system_web).click()
        time.sleep(3)
        self.back_button()

    def click_termsOfUse(self):
        self.get_element(*self.terms_of_use).click()
        time.sleep(1)
        self.back_button()

    def click_privacyPolicy(self):
        self.get_element(*self.privacy_policy).click()
        time.sleep(1)
        self.back_button()