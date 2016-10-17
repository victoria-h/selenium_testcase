
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver

import time

import unittest

class CreatehomeworkTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://lms.wg-t.com/login")
        driver = self.driver

        emailFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_id("email"))
        passFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_id("password"))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_id("submit"))


        emailFieldElement.clear()
        emailFieldElement.send_keys("i@example.com")
        passFieldElement.clear()
        passFieldElement.send_keys("password")
        time.sleep(5)
        loginButtonElement.click()
        time.sleep(5)
        driver.get('http://lms.wg-t.com/course/177/syllabus#/learning-activity/homework/new')
        time.sleep(5)

    def test_Createhomework(self):
        driver = self.driver
        time.sleep(30)
        titleFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_id("title"))
        titleFieldElement.send_keys("个人线上作业1")
        try:
             driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/form/div[4]/button[1]")
        except:
             print("element does not exist")

             driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/form/div[4]/button[1]").click()

        time.sleep(10)
        driver.get_screenshot_as_file('/Users/wg/Desktop/pic/createhomework1.png')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


