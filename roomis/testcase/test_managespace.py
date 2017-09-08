# -*- coding: utf-8 -*-
import time
import unittest

import config
import initenv

url = config.domain


class Testmanagespace(unittest.TestCase):
    def setUp(self):
    #     #   global url
    #     #   url = "http://console.qa.roomis.com.cn"
    #     #   self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    #     #   loginurl= url+"/login"
    #     #   self.driver.get(loginurl)
    #     #   username1 = self.driver.find_element_by_id("username")
    #     #   pass1 = self.driver.find_element_by_id("password")
    #     #   username1.send_keys("roomis-k12")
    #     #   pass1.send_keys("11111111")
    #     #   self.driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
    #     #   time.sleep(15)
    #
        initenv.login(self)

    def test_createspace(self):
        createspaceurl = url + "/console/spaces/new"
        print(createspaceurl)
        self.driver.get(createspaceurl)
        time.sleep(15)
        assert "添加新空间" in self.driver.title
        spacename=self.driver.find_element_by_name("name")
        spacename.send_keys(config.spacename)
        spacedisplayname=self.driver.find_element_by_name("displayName")
        spacedisplayname.send_keys(config.displayname)
        self.driver.find_element_by_link_text("下一步").click()
        time.sleep(15)
        spacecapacity=self.driver.find_element_by_name("capacity")
        spacecapacity.send_keys(config.spacecapacity)
        self.driver.find_element_by_link_text("下一步").click()
        time.sleep(15)
        self.driver.find_element_by_link_text("保存").click()
        time.sleep(15)
        assert "空间列表" in self.driver.title
        assert config.spacename in self.driver.page_source

    def test_deletespace(self):
        deletespaceid = '200000177'
        deletespaceurl = url + "/console/spaces/" + deletespaceid
        # print (deletespaceurl)
        self.driver.get(deletespaceurl)
        time.sleep(15)
        assert "编辑空间信息" in self.driver.title

        deletebutton=self.driver.find_element_by_css_selector("#submitForm > div:nth-child(2) > div > div > button")
        deletebutton.click()
        time.sleep(15)
        self.driver.find_element_by_class_name("confirm").click()
        time.sleep(15)
        assert "您访问的网页不存在" in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testmanagespace)
    unittest.TextTestRunner(verbosity=2).run(suite)
