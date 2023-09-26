import time

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
    notices=(By.XPATH,'//*[contains(@text,"Notification Center")]')
    storage=(By.XPATH,'//*[contains(@text,"Storage")]')
    app=(By.XPATH,'//*[contains(@text,"App Management")]')
    location=(By.XPATH,'//*[contains(@text,"Location")]')
    special=(By.XPATH,'//*[contains(@text,"Special Function")]')
    system=(By.XPATH,'//*[contains(@text,"System")]')

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

    def click_notices(self):
        self.no_element_swipe(*self.notices)

    def click_storage(self):
        self.no_element_swipe(*self.storage)

    def click_app(self):
        self.no_element_swipe(*self.app)

    def click_location(self):
        self.no_element_swipe(*self.location)

    def click_special(self):
        self.no_element_swipe(*self.special)

    def click_system(self):
        self.no_element_swipe(*self.system)


