class Base_page:
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,*loc):
        return self.driver.find_element(*loc)

    def get_elements(self,*loc):
        return self.driver.find_elements(*loc)