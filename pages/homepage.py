class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.logout="//*[text()='Logout']"

    def logout_acti(self):
        self.driver.find_element_by_xpath(self.logout).click()