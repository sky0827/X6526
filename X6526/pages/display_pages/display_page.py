import time
from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger

class Display_page(Base_page):

    light_theme=(By.XPATH,'//*[@resource-id="com.android.settings:id/dark_mode_img_light"]')  # 浅色主题
    dark_theme=(By.XPATH,'//*[@resource-id="com.android.settings:id/dark_mode_img_dark"]')  # 深色主题
    schedule=(By.XPATH,'//*[@text="Schedule"]')  # 定时切换主题
    auto_brightness=(By.XPATH,'//*[@text="Adaptive brightness"]')  # 自动调节亮度
    keep_screen=(By.XPATH,'//*[@text="Keep screen on"]')  # 屏幕常亮
    screen_timeout=(By.XPATH,'//*[@text="Screen timeout"]')  # 自动熄屏时间
    refresh=(By.XPATH,'//*[@text="Screen refresh rate"]')  # 刷新率
    eye_care=(By.XPATH,'//*[@text="Eye Care"]')  # 护眼模式
    ultra_touch=(By.XPATH,'//*[@text="Ultra Touch"]')  # 超级触控
    font_size=(By.XPATH,'//*[@text="Font size"]')  # 字体大小
    inadvertently_mode=(By.XPATH,'//*[@text="Inadvertently mode"]')  # 防误触
    auto_rotate=(By.XPATH,'//*[@text="Auto-rotate screen"]')  # 自动旋转
    lock_screen=(By.XPATH,'//*[@text="Lock screen"]')  # 锁屏
    status_bar=(By.XPATH,'//*[@text="Status bar"]')  # 状态栏

    def click_lightTheme(self):
        self.get_element(*self.light_theme).click()
        time.sleep(4)

    def click_darkTheme(self):
        self.get_element(*self.dark_theme).click()
        time.sleep(4)

    def click_schedule(self):
        self.get_element(*self.schedule).click()
        time.sleep(1)

    def click_autoBrightness(self):
        self.get_element(*self.auto_brightness).click()
        time.sleep(1)

    def click_keepScreen(self):
        self.get_element(*self.keep_screen).click()
        time.sleep(1)

    def click_screenTimeout(self):
        # self.get_element(*self.screen_timeout).click()
        self.no_element_swipe(*self.screen_timeout)
        time.sleep(1)
        self.back_button()

    def click_refresh(self):
        # self.get_element(*self.refresh).click()
        self.no_element_swipe(*self.refresh)

    def click_eyeCare(self):
        # self.get_element(*self.eye_care).click()
        self.no_element_swipe(*self.eye_care)

    def click_ultraTouch(self):
        # self.get_element(*self.ultra_touch).click()
        self.no_element_swipe(*self.ultra_touch)
        time.sleep(1)
        self.back_button()

    def click_fontSize(self):
        # self.get_element(*self.font_size).click()
        self.no_element_swipe(*self.font_size)
        time.sleep(1)
        self.back_button()

    def click_inadvertentlyMode(self):
        # self.get_element(*self.inadvertently_mode).click()
        self.no_element_swipe(*self.inadvertently_mode)
        time.sleep(1)

    def click_autoRotate(self):
        # self.get_element(*self.auto_rotate).click()
        self.no_element_swipe(*self.auto_rotate)
        time.sleep(1)

    def click_lockScreen(self):
        # self.get_element(*self.lock_screen).click()
        self.no_element_swipe(*self.lock_screen)

    def click_statusBar(self):
        # self.get_element(*self.status_bar).click()
        self.no_element_swipe(*self.status_bar)






