import unittest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
class TestLogin(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    self.driver.get("http://console.qa.roomis.com.cn/login")
    username1 = self.driver.find_element_by_id("username")
    pass1 = self.driver.find_element_by_id("password")
    username1.send_keys("roomis-k12")
    pass1.send_keys("11111111")
    self.driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
    time.sleep(15)
  def test_createbooking(self):
    new_date = time.strftime('%Y-%m-%d', time.localtime())
    start_time = time.strftime('%H:%M', time.localtime())
    now = datetime.datetime.now()
    d2 = now + datetime.timedelta(minutes=15)
    end_time=d2.strftime("%H:%M")
    print (new_date)
    print (start_time)
    print (end_time)
    createbookingurl= "http://console.qa.roomis.com.cn/console/booking/spaces/200000154/events/new?date="+new_date+"&start_time="+start_time+"&end_time="+end_time
    print(createbookingurl)
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
    print (pageurl)
    newstring=pageurl.split("/success")[0]
    print (newstring)
    self.driver.get_screenshot_as_file("/Users/zhaopanhong/PycharmProjects/selenium_testcase/roomis/pic/1.png")

   # def test_canclebooking(self):
    self.driver.get(newstring)
    time.sleep(15)
    self.driver.find_element_by_link_text("取消预约").click()
    time.sleep(15)
    self.driver.find_element_by_css_selector("#cancelBookingEvent > div > div > div.modal-footer.no-borders.text-center > button.btn.btn-primary.ladda-button.btn-custom.m-r-md > span.ladda-label").click()


  def tearDown(self):
      self.driver.close ()
if __name__ == "__main__":
  suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
  unittest.TextTestRunner(verbosity=2).run(suite)