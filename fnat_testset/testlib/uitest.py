# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UITest(unittest.TestCase):
    def __init__(self):
        pass
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.16.9.9/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_d_h_c_p_configuration(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//img[@alt='setup']").click()
        driver.find_element_by_css_selector("span.ui-jf-icon.ui-jf-arrow-next").click()
        driver.find_element_by_css_selector("#dhcpIp > span.ui-btn-inner > span.ui-btn-text").click()
        driver.find_element_by_css_selector("#ipConfigSubmit > span.ui-btn-inner").click()
        driver.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        driver.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
    def test_re(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(0.5)
        driver.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        time.sleep(15)
        self.assertEqual("images/gatewaygreen.png", driver.find_element_by_id("gateHeadIcon").get_attribute("src"))

    def test_l_l_d_penable(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        time.sleep(15)
        self.assertTrue(self.is_element_present(By.ID, "switchTitle"))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


