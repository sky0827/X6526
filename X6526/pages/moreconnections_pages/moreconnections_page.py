from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class Moreconnections_page(Base_page):

    airplane=(By.XPATH,'//*[@text="Airplane mode"]')  # 飞行模式
    vpn=(By.XPATH,'//*[@text="VPN"]')  # VPN
    private_dns=(By.XPATH,'//*[@text="Private DNS"]')  # 私人DNS
    cast=(By.XPATH,'//*[@text="Cast"]')  # 投射
    usb=(By.XPATH,'//*[@text="USB"]')
    printing=(By.XPATH,'//*[@text="Printing"]') # 打印
    otg=(By.XPATH,'//*[@text="OTG"]')  # OTG
    nearby_share=(By.XPATH,'//*[@text="Nearby Share"]')  # 附近分享

    def click_airplan(self):
        self.get_element(*self.airplane).click()
        time.sleep(3)

    def click_vpn(self):
        self.get_element(*self.vpn).click()
        time.sleep(1)
        self.back_button()

    def click_privateDns(self):
        self.get_element(*self.private_dns).click()
        time.sleep(1)
        self.back_button()

    def click_cast(self):
        self.get_element(*self.cast).click()
        time.sleep(1)
        self.back_button()

    def click_usb(self):
        self.get_element(*self.usb).click()
        time.sleep(1)
        self.back_button()

    def click_printing(self):
        self.get_element(*self.printing).click()
        time.sleep(1)
        self.back_button()

    def click_otg(self):
        self.get_element(*self.otg).click()
        time.sleep(1)

    def click_nearbyShare(self):
        self.get_element(*self.nearby_share).click()
        time.sleep(1)
        self.back_button()
