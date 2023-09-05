from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.sound_pages.sound_page import Sound_page
from pages.sound_pages.sound_notdisturb_page import Sound_notdisturb_page
from pages.sound_pages.sound_advanced_page import Sound_advanced_page

class Sound_test(Myutil):

    def test_1_sound_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        sound=Sound_page(self.driver)
        sound_not_disturb=Sound_notdisturb_page(self.driver)
        sound_advanced=Sound_advanced_page(self.driver)

        setting.click_sound()
        sound.click_notDisturb()
        sound_not_disturb.click_notDisturb()  # 开启勿扰模式
        sound_not_disturb.click_notDisturb()  # 关闭勿扰模式
        sound_not_disturb.click_people()
        sound_not_disturb.click_apps()
        sound_not_disturb.click_alarms()
        sound_not_disturb.click_schedules()
        sound_not_disturb.click_quickSettings()
        sound_not_disturb.click_displayOptionsNotice()

        base.back_button()  # 返回声音与震动界面

        sound.click_s1Ringtone()
        sound.click_s2Ringtone()
        sound.click_noticeSound()
        sound.click_dts()
        sound.click_haptic()
        sound.click_haptic()
        sound.click_increasing()
        sound.click_increasing()
        sound.click_vibrateForCalls()
        sound.click_advancedOptions()
        sound_advanced.click_dialPadTones()  # 关闭
        sound_advanced.click_dialPadTones()  # 开启
        sound_advanced.click_screenLockSound()  # 开启
        sound_advanced.click_screenLockSound()  # 关闭
        sound_advanced.click_chargingSounds()  # 关闭
        sound_advanced.click_chargingSounds()  # 开启
        sound_advanced.click_touchSounds()  # 开启
        sound_advanced.click_touchSounds()  # 关闭



