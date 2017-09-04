
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import time

import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://lms.wg-t.com/login")


    def test_Login(self):
        driver = self.driver
        lmsUsername = "i@example.com"
        lmsPassword = "password"

        emailFieldID = "email"
        passFieldID = "password"
        LoginButtonXpath = "//input[@value='登入']"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_xpath(LoginButtonXpath))


        emailFieldElement.clear()
        emailFieldElement.send_keys(lmsUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(lmsPassword)
        time.sleep(5)
        loginButtonElement.click()
        time.sleep(60)
        assert "课程安排"  in driver.page_source
        driver.get_screenshot_as_file('/Users/wg/Desktop/pic/foo.png')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


