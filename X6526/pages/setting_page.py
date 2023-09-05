from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Setting_page(Base_page):

    myPhone=(By.XPATH,'//*[contains(@text,"My Phone")]')
    sim=(By.XPATH,'//*[contains(@text,"SIM & Network Settings")]')
    wifi=(By.XPATH,'//*[contains(@text,"Wi‑Fi")]')
    bluetooth=(By.XPATH,'//*[contains(@text,"Bluetooth")]')
    hotspot=(By.XPATH,'//*[contains(@text,"Hotspot & Tethering")]')
    moreconnections=(By.XPATH,'//*[contains(@text,"More Connections")]')
    display=(By.XPATH,'//*[contains(@text,"Display & Brightness")]')
    sound=(By.XPATH,'//*[contains(@text,"Sound & Vibration")]')

    def click_myphone(self):
        self.get_element(*self.myPhone).click()

    def click_sim(self):
        self.get_element(*self.sim).click()

    def click_wifi(self):
        self.get_element(*self.wifi).click()

    def click_bluetooth(self):
        self.get_element(*self.bluetooth).click()

    def click_hotspot(self):
        self.get_element(*self.hotspot).click()

    def click_moreconnections(self):
        self.get_element(*self.moreconnections).click()

    def click_display(self):
        self.no_element_swipe(*self.display)

    def click_sound(self):
        self.no_element_swipe(*self.sound)

