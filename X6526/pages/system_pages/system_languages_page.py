from pages.base_page import Base_page
from appium.webdriver.common.appiumby import By
from common.util import logger
import time

class System_languages_page(Base_page):

    languages=(By.XPATH,'//*[@text="Languages"]')  # 语言
    screen_keyboard=(By.XPATH,'//*[@text="On-screen keyboard"]')  # 屏幕键盘
    physical_keyboard=(By.XPATH,'//*[@text="Physical Keyboard"]')  # 实体键盘
    spell_checker=(By.XPATH,'//*[@text="Spell Checker"]')  # 拼写检查
    person_dic=(By.XPATH,'//*[@text="Personal Dictionary"]')  # 个人字典
    pointer_speed=(By.XPATH,'//*[@text="Pointer Speed"]')  # 指针速度
    text_speech=(By.XPATH,'//*[@text="Text-to-speech output"]')  # 文字转语音

    def click_languages(self):
        self.get_element(*self.languages).click()
        time.sleep(1)
        self.back_button()

    def click_screenKeyboard(self):
        self.get_element(*self.screen_keyboard).click()
        time.sleep(1)
        self.back_button()

    def click_physicalKeyboard(self):
        self.get_element(*self.physical_keyboard).click()
        time.sleep(1)
        self.back_button()

    def click_spellChecker(self):
        self.get_element(*self.spell_checker).click()
        time.sleep(1)
        self.back_button()

    def click_personDic(self):
        self.get_element(*self.person_dic).click()
        time.sleep(1)
        self.back_button()

    def click_pointerSpeed(self):
        self.get_element(*self.pointer_speed).click()
        time.sleep(1)
        self.back_button()

    def click_textSpeech(self):
        self.get_element(*self.text_speech).click()
        time.sleep(3)
        self.back_button()



