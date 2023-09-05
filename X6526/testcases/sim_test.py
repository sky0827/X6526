from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.sim_pages.sim_page import Sim_page
from pages.sim_pages.sim_data_security_page import Sim_data_security_page
from pages.sim_pages.sim_intelligentnetwork_page import Sim_intelligentnetwork_page
from pages.sim_pages.sim_callsettings_page import Sim_callsettings_page


class Sim_test(Myutil):

    def test_1_sim_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        sim=Sim_page(self.driver)
        sim_data_security=Sim_data_security_page(self.driver)
        sim_inttelligentnetwork=Sim_intelligentnetwork_page(self.driver)
        sim_callsettings=Sim_callsettings_page(self.driver)

        setting.click_sim()
        sim.click_dataSecurity()
        sim_data_security.click_pseudo()
        sim_data_security.click_harassment()
        sim_data_security.click_dataSettingsUsage()

        base.back_button() # 返回到sim卡界面

        sim.click_intalligentNetwork()
        sim_inttelligentnetwork.click_smartNetwork()  # 开启智慧网速分配
        sim_inttelligentnetwork.click_smartNetwork()  # 关闭智慧网速分配
        sim_inttelligentnetwork.click_smartDualChannel()

        base.back_button()  # 返回sim卡界面

        sim.click_callSettings()
        sim_callsettings.click_flashForCalls()  # 开启来电闪光灯
        sim_callsettings.click_flashForCalls()  # 关闭来电闪光灯
        sim_callsettings.click_autoRecordCalls()  # 开启自动通话录音
        sim_callsettings.click_autoRecordCalls()  # 关闭自动通话录音
        sim_callsettings.click_unknownNumber()
        sim_callsettings.click_simNumberSettings()
        sim_callsettings.click_soundsVibration()
        sim_callsettings.click_callerIdDisplay()
        sim_callsettings.click_advancedSettings()
        sim_callsettings.click_about()

        base.back_button()  # 返回sim卡界面

        sim.click_smsSettings()

        base.back_button()  # 返回设置界面






