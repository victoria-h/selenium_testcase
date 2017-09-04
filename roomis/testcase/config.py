# -*- coding:utf-8 -*-
import unittest
import time
import datetime
import HTMLTestRunner,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class SetUp(unittest.TestCase):

  def Login(self):
    global url
    url = "http://console.qa.roomis.com.cn"
    self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    loginurl= url+"/login"
    self.driver.get(loginurl)
    username1 = self.driver.find_element_by_id("username")
    pass1 = self.driver.find_element_by_id("password")
    username1.send_keys("roomis-k12")
    pass1.send_keys("11111111")
    self.driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
    time.sleep(15)

    def tearDown(self):
        self.driver.close()


