from selenium import webdriver
from testdata.data import *
from pages.loginpage import LoginPage
from pages.homepage import HomePage
import time

driver=webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/Framework_POM/drivers/chromedriver.exe")
driver.get(URL)
driver.implicitly_wait(10)
driver.maximize_window()


#

lp=LoginPage(driver)
lp.enter_un()

time.sleep(5)
lp.enter_pwd()

time.sleep(5)
lp.click_login()
# driver.find_element_by_name("pwd").send_keys(PWD)
# driver.find_element_by_xpath("//*[text()='Login ']").click()

hp=HomePage(driver)
time.sleep(5)
hp.logout_acti()
driver.quit()