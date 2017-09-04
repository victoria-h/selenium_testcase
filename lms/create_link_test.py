
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
        driver.get('http://lms.wg-t.com/course/177/syllabus#/learning-activity/web_link/new')
        time.sleep(5)

    def test_Createhomework(self):
        driver = self.driver
        time.sleep(30)
        titleFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_name("title"))
        titleFieldElement.send_keys("线上链接10")
        try:
            driver.find_element_by_class_name("select2-line-content")
        except:
            print("element does not exist")

        #unitselect = driver.find_element_by_class_name("select2-drop-mask")
        unitselect = driver.find_element_by_id("select2-results-2")
        all_options = unitselect.find_elements_by_class_name("select2-result-label")

        for option in all_options:
            print("Value is: %s" % option.get_attribute("value"))
            option.click()


        time.sleep(50)

        titleFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_name("link"))
        titleFieldElement.send_keys("http://www.baidu.com/")
        time.sleep(10)
        driver.find_element_by_css_selector("body > div.wrapper > div.main-content > div.content-under-nav-2.with-loading > div.ng-scope > div > div.new-activity > div:nth-child(2) > form > div.form-buttons.text-center.activity-submit-area > button.button.button-green.medium").click()

        time.sleep(10)

        driver.find_element_by_link_text("线上链接10").click()


        time.sleep(30)

        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/iframe"))
        searchFieldElement = WebDriverWait(driver, 10).until(lambda drivers: drivers.find_element_by_name("wd"))
        searchFieldElement.send_keys("创课")
        driver.find_element_by_id("su").click()

        time.sleep(10)

        driver.get_screenshot_as_file('/Users/wg/Desktop/pic/link10.png')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


