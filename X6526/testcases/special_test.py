from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.special_pages.special_page import Special_page
from pages.special_pages.special_memfusion_page import Special_memfusion
from pages.special_pages.special_magic_page import Special_magic_page
from pages.special_pages.special_action_page import Special_action_page
import time

class Special_test(Myutil):

    def test_1_special_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        special=Special_page(self.driver)
        special_memfusion=Special_memfusion(self.driver)
        special_magic=Special_magic_page(self.driver)
        special_action=Special_action_page(self.driver)

        setting.click_special()
        special.click_memfusion()
        special_memfusion.click_memfusionButton()
        special_memfusion.click_cancel()
        special_memfusion.click_setRam()
        special_memfusion.click_button2G()
        special_memfusion.click_button4G()
        special_memfusion.click_button1G()
        special_memfusion.click_cancel()

        base.back_button()  # 返回特色功能页面

        special.click_magic()
        special_magic.click_magicRing()
        special_magic.click_magicRing()
        special_magic.click_faceUnlock()
        special_magic.click_faceUnlock()
        special_magic.click_backgroundCall()
        special_magic.click_backgroundCall()
        special_magic.click_chargingAnimation()
        special_magic.click_chargingAnimation()
        special_magic.click_chargeCompletion()
        special_magic.click_chargeCompletion()
        special_magic.click_lowBattery()
        special_magic.click_lowBattery()

        base.back_button()  # 返回特色功能页面

        special.click_actionGesture()
        special_action.click_quickStart()
        special_action.click_tappingWake()
        special_action.click_musicGesturet()
        special_action.click_filpMute()
        special_action.click_raiseEar()
        special_action.click_liftWake()
        special_action.click_screenshots()

        base.back_button()  # 返回特色功能页面
        base.back_button()  # 返回设置页面