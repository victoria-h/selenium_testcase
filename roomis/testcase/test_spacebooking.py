# -*- coding:utf-8 -*-
import unittest
import time
import datetime
import HTMLTestRunner,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from config import *
import initenv
class Testspacebooking(unittest.TestCase):

  def setUp(self):
    # global url
    # url = "http://console.qa.roomis.com.cn"
    # self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    # loginurl= url+"/login"
    # self.driver.get(loginurl)
    # username1 = self.driver.find_element_by_id("username")
    # pass1 = self.driver.find_element_by_id("password")
    # username1.send_keys("roomis-k12")
    # pass1.send_keys("11111111")
    # self.driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
    # time.sleep(15)
    initenv.Login(self)

  def test_1createbooking(self):
    new_date = time.strftime('%Y-%m-%d', time.localtime())
    start_time = time.strftime('%H:%M', time.localtime())
    now = datetime.datetime.now()
    d2 = now + datetime.timedelta(minutes=15)
    end_time=d2.strftime("%H:%M")
    # print (new_date)
    # print (start_time)
    # print (end_time)
    url=geturl()
    createbookingurl= url+"/console/booking/spaces/200000165/events/new?date="+new_date+"&start_time="+start_time+"&end_time="+end_time
    # print(createbookingurl)
    self.driver.get(createbookingurl)
    time.sleep(15)
    bookingname=self.driver.find_element_by_id("booking-event-name")
    bookingname.send_keys("空间预约s1")
    bookingtype=self.driver.find_element_by_id("booking-event-extern-form-name")
    Select(bookingtype).select_by_value("3")
    time.sleep(15)
    self.driver.find_element_by_css_selector("button").submit()
    time.sleep(15)
    pageurl = self.driver.current_url
    assert "successs" not in pageurl
    print (pageurl)
    global newstring
    newstring=pageurl.split("/success")[0]
    print (newstring)
    self.driver.get_screenshot_as_file("/Users/zhaopanhong/PycharmProjects/selenium_testcase/roomis/pic/1.png")

  def test_2canclebooking(self):
    self.driver.get(newstring)
    time.sleep(15)
    self.driver.find_element_by_link_text("取消预约").click()
    time.sleep(15)
    self.driver.find_element_by_css_selector("#cancelBookingEvent > div > div > div.modal-footer.no-borders.text-center > button.btn.btn-primary.ladda-button.btn-custom.m-r-md > span.ladda-label").click()
    time.sleep(25)
    # assert "DONE" not in self.driver.page_source


  def tearDown(self):
      self.driver.close ()
def Suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Testspacebooking("test_1createbooking"))
    suiteTest.addTest(Testspacebooking("test_2canclebooking"))
    return suiteTest


# if __name__ == '__main__':
#
#     filePath = "/Users/zhaopanhong/PycharmProjects/selenium_testcase/roomis/test_spacebookingResult.html"
#     file_result = open(filePath, 'wb')
#
#
#     runner = HTMLTestRunner.HTMLTestRunner(stream=file_result,title='spacebooking Test Report',description='This  is spacebooking test  Report')
#     runner.run(Suite())
if __name__ == "__main__":
  suite = unittest.TestLoader().loadTestsFromTestCase(Testspacebooking)
  unittest.TextTestRunner(verbosity=2).run(suite)