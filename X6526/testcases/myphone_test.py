from common.myutil import Myutil
from common.util import Util
from pages.base_page import Base_page
from pages.myphone_page import Myphone_page
from pages.setting_page import Setting_page

class Myphonr_test(Myutil):

    def test_1_myphone_info(self):
        setting=Setting_page(self.driver)
        setting.click_myphone()
        myphone=Myphone_page(self.driver)
        myphone.find_adndroid_version()