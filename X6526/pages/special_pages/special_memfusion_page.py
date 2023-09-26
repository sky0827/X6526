import time

from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Special_memfusion(Base_page):

    memfusion_button=(By.XPATH,'//*[@resource-id="android:id/switch_widget"]')  # 内存融合
    set_ram=(By.XPATH,'//*[@text="Set virtual RAM"]')  # 扩展容量选择
    cancel=(By.XPATH,'//*[@text="Cancel"]')
    button_1G=(By.XPATH,'//*[@text="1GB"]')
    button_2G=(By.XPATH,'//*[@text="2GB"]')
    button_4G=(By.XPATH,'//*[@text="4GB"]')

    def click_memfusionButton(self):
        time.sleep(1)
        self.get_element(*self.memfusion_button).click()

    def click_setRam(self):
        self.get_element(*self.set_ram).click()

    def click_cancel(self):
        self.get_element(*self.cancel).click()

    def click_button1G(self):
        self.get_element(*self.button_1G).click()
        time.sleep(1)

    def click_button2G(self):
        self.get_element(*self.button_2G).click()
        time.sleep(1)

    def click_button4G(self):
        self.get_element(*self.button_4G).click()
        time.sleep(1)


