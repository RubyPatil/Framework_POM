from testdata.data import *
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.un="username"
        self.pwd="pwd"
        self.login="//*[text()='Login ']"


    def enter_un(self):
        self.driver.find_element_by_name(self.un).send_keys(UN)

    def enter_pwd(self):
            self.driver.find_element_by_name(self.pwd).send_keys(PWD)

    def click_login(self):
            self.driver.find_element_by_xpath("//*[text()='Login ']").click()

