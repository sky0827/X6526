import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
from selenium.common.exceptions import NoSuchElementException

class Wifi_preference_page(Base_page):

    auto_switch_data=(By.XPATH,'//*[@text="Auto Switch to Mobile Data"]')  # 自动切换为数据
    ask_before_switching=(By.XPATH,'//*[@text="Ask Before Switching"]')  # 切换时询问
    turn_on_wifi_auto=(By.XPATH,'//*[@text="Turn on Wi‑Fi automatically"]')  # 自动开启wifi
    turn_on_wifi_auto_alert_turnon=(By.XPATH,'//*[@text="Turn on"]')
    open_network_notice=(By.XPATH,'//*[@text="Open Network Notification"]')  # 打开网络通知
    install_certificates=(By.XPATH,'//*[@text="Install certificates"]')  # 安装证书
    network_rating_provider=(By.XPATH,'//*[@text="Network rating provider"]')  # 网络评分服务提供方

    def click_autoAwitchData(self):
        self.get_element(*self.auto_switch_data).click()

    def click_askBeforeSwitching(self):
        self.get_element(*self.ask_before_switching).click()

    def click_turnOnWifiAuto(self):
        self.get_element(*self.turn_on_wifi_auto).click()
        self.no_element_noactioin(*self.turn_on_wifi_auto_alert_turnon)
        # try:
        #     self.get_element(*self.turn_on_wifi_auto_alert_turnon).click()
        # except NoSuchElementException:
        #     pass

    def click_openNetworkNotice(self):
        self.get_element(*self.open_network_notice).click()

    def click_installCertificates(self):
        self.get_element(*self.install_certificates).click()
        time.sleep(1)
        self.back_button()

    def click_networkRatingProvider(self):
        self.get_element(*self.network_rating_provider).click()
        time.sleep(1)
        self.back_button()


