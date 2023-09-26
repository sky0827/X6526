from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.system_pages.system_page import System_page
from pages.system_pages.system_languages_page import System_languages_page
from pages.system_pages.system_data_page import System_data_page
from pages.system_pages.system_reset_page import System_reset_page

class System_test(Myutil):

    def test_1_system_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        system=System_page(self.driver)
        system_languages=System_languages_page(self.driver)
        system_data=System_data_page(self.driver)
        system_reset=System_reset_page(self.driver)

        setting.click_system()
        system.click_languages()
        system_languages.click_languages()
        system_languages.click_screenKeyboard()
        system_languages.click_physicalKeyboard()
        system_languages.click_spellChecker()
        system_languages.click_personDic()
        system_languages.click_pointerSpeed()
        system_languages.click_textSpeech()

        base.back_button()  # 返回系统界面

        system.click_dataTime()
        system_data.click_autoSet()
        system_data.click_localeDefault()
        system_data.click_use24Hour()
        system_data.click_use24Hour()
        system_data.click_localeDefault()
        system_data.click_setTimeAuto()
        system_data.click_selectTime()
        system_data.click_setTimeAuto()

        base.back_button()  # 返回系统界面

        system.click_navigation()
        system.click_update()
        system.click_power()
        system.click_backUp()
        system.click_reset()
        system_reset.click_resetWifi()
        system_reset.click_resetApp()
        system_reset.click_resetCalibration()
        system_reset.click_resetPhone()

        base.back_button()  # 返回系统界面

        system.click_manual()

        base.back_button()  # 返回设置界面




