# -*- coding:utf-8 -*-
import time
from selenium import webdriver
import config

url = config.domain
username = config.username
password = config.password


# class initenv(unittest.TestCase):
def login(self):
    self.driver= webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    login_url = url + "/login"
    self.driver.get(login_url)
    time.sleep(5)
    username1 = self.driver.find_element_by_id("username")
    pass1 = self.driver.find_element_by_id("password")
    username1.send_keys(username)
    pass1.send_keys(password)
    self.driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
    time.sleep(15)

#
# def tearDown(self):
#     self.driver.close()




