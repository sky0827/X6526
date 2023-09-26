from common.myutil import Myutil
from pages.base_page import Base_page
from pages.setting_page import Setting_page
from pages.storage_pages.storage_page import Storage_page
import time

class Storage_test(Myutil):

    def test_1_storage_info(self):
        setting=Setting_page(self.driver)
        base=Base_page(self.driver)
        storage=Storage_page(self.driver)

        setting.click_storage()
        storage.click_moreOptions()
        storage.click_lowStorage()
        storage.click_lowStorageCancel()
        storage.click_moreOptions()
        storage.click_lowStorage()
        storage.click_lowStorageDisable()
        storage.click_moreOptions()
        storage.click_lowStorage()
        storage.click_lowStorageCancel()
        storage.click_moreOptions()
        storage.click_lowStorage()
        storage.click_lowStorageEnable()
        storage.click_moreOptions()
        time.sleep(1)

        base.back_button()
        base.back_button()  # 返回设置界面