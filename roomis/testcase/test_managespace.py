import unittest
import time
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import config.py

class Testmanagespace(unittest.TestCase):

  def setUp(self):
  #   global url
  #   url = "http://console.qa.roomis.com.cn"
  #   self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
  #   loginurl= url+"/login"
  #   self.driver.get(loginurl)
  #   username1 = self.driver.find_element_by_id("username")
  #   pass1 = self.driver.find_element_by_id("password")
  #   username1.send_keys("roomis-k12")
  #   pass1.send_keys("11111111")
  #   self.driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
  #   time.sleep(15)
      config.SetUp.Login()

  def test_createspace(self):
    url = "http://console.qa.roomis.com.cn"
    createspaceurl= url+"/console/spaces/new"
    self.driver.get(createspaceurl)
    time.sleep(15)
    spacename=self.driver.find_element_by_name("name")
    spacename.send_keys("空间se8")
    spacedisplayname=self.driver.find_element_by_name("displayName")
    spacedisplayname.send_keys("班牌se8")
    self.driver.find_element_by_link_text("下一步").click()
    time.sleep(15)
    spacecapacity=self.driver.find_element_by_name("capacity")
    spacecapacity.send_keys("100")
    self.driver.find_element_by_link_text("下一步").click()
    time.sleep(15)
    self.driver.find_element_by_link_text("保存").click()
    time.sleep(15)
    # assert "空间se7" in self.driver.page_source


  def test_deletespace(self):
      deletespaceurl = url + "/console/spaces/200000172"
      print (deletespaceurl)
      self.driver.get(deletespaceurl)
      time.sleep(15)
      deletebutton=self.driver.find_element_by_css_selector("#submitForm > div:nth-child(2) > div > div > button")
      deletebutton.click()
      time.sleep(15)
      self.driver.find_element_by_class_name("confirm").click()
      time.sleep(15)
      # assert "您访问的网页不存在" in self.driver.page_source

  def tearDown(self):
      self.driver.close ()
if __name__ == "__main__":
  suite = unittest.TestLoader().loadTestsFromTestCase(Testmanagespace)
  unittest.TextTestRunner(verbosity=2).run(suite)