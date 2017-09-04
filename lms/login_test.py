
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://lms.wg-t.com/login")
email1 = driver.find_element_by_id("email")
pass1 = driver.find_element_by_id("password")
email1.send_keys("i@example.com")
pass1.send_keys("password")
driver.find_element_by_id("submit").click()

driver.close()