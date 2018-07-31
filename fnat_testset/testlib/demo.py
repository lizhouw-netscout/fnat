__author__ = 'bzhang4'
from selenium import webdriver
import time


class UITest():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.16.9.9/"
    def dhcp_config_retest(self):
        browser = self.driver
        browser.get(self.base_url)
        browser.find_element_by_xpath("//img[@alt='setup']").click()
        browser.find_element_by_css_selector("span.ui-jf-icon.ui-jf-arrow-next").click()
        browser.find_element_by_css_selector("#dhcpIp > span.ui-btn-inner > span.ui-btn-text").click()
        browser.find_element_by_css_selector("#ipConfigSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        time.sleep(35)
        browser.quit()
    def dhcp_config(self):
        browser = self.driver
        browser.get(self.base_url)
        browser.find_element_by_xpath("//img[@alt='setup']").click()
        browser.find_element_by_css_selector("span.ui-jf-icon.ui-jf-arrow-next").click()
        browser.find_element_by_css_selector("#dhcpIp > span.ui-btn-inner > span.ui-btn-text").click()
        browser.find_element_by_css_selector("#ipConfigSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        #browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        #time.sleep(15)
        #browser.quit()
    def static_config_retest(self,ip,subnet,gw,dns):
        browser = self.driver
        browser.get(self.base_url)
        browser.find_element_by_xpath("//img[@alt='setup']").click()
        browser.find_element_by_css_selector("span.ui-jf-icon.ui-jf-arrow-next").click()
        browser.find_element_by_css_selector("#dhcpStatic > span.ui-btn-inner > span.ui-btn-text > span.btnText").click()
        browser.find_element_by_id("ipcfgIp").clear()
        browser.find_element_by_id("ipcfgIp").send_keys(ip)
        browser.find_element_by_id("ipcfgSub").clear()
        browser.find_element_by_id("ipcfgSub").send_keys(subnet)
        browser.find_element_by_id("ipcfgGate").clear()
        browser.find_element_by_id("ipcfgGate").send_keys(gw)
        browser.find_element_by_id("ipcfgDns").clear()
        browser.find_element_by_id("ipcfgDns").send_keys(dns)
        browser.find_element_by_css_selector("#ipConfigSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        time.sleep(110)
        browser.quit()
    def static_config(self,ip,subnet,gw,dns):
        browser = self.driver
        browser.get(self.base_url)
        browser.find_element_by_xpath("//img[@alt='setup']").click()
        browser.find_element_by_css_selector("span.ui-jf-icon.ui-jf-arrow-next").click()
        browser.find_element_by_css_selector("#dhcpStatic > span.ui-btn-inner > span.ui-btn-text > span.btnText").click()
        browser.find_element_by_id("ipcfgIp").clear()
        browser.find_element_by_id("ipcfgIp").send_keys(ip)
        browser.find_element_by_id("ipcfgSub").clear()
        browser.find_element_by_id("ipcfgSub").send_keys(subnet)
        browser.find_element_by_id("ipcfgGate").clear()
        browser.find_element_by_id("ipcfgGate").send_keys(gw)
        browser.find_element_by_id("ipcfgDns").clear()
        browser.find_element_by_id("ipcfgDns").send_keys(dns)
        browser.find_element_by_css_selector("#ipConfigSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        #driver.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        #time.sleep(2)
        #browser.quit()
    def tcp_config_retest(self,tcp_target,tcp_port):
        browser = self.driver
        browser.get(self.base_url + "settings.html")
        browser.find_element_by_xpath("//div[@id='pageSettings']/div[2]/ul/li[6]/div/div/a/span").click()
        browser.find_element_by_css_selector("#wwwTcp > span.ui-btn-inner > span.ui-btn-text").click()
        browser.find_element_by_id("wwwtarget").clear()
        browser.find_element_by_id("wwwtarget").send_keys(tcp_target)
        browser.find_element_by_id("wwwport").clear()
        browser.find_element_by_id("wwwport").send_keys(tcp_port)
        browser.find_element_by_css_selector("#wwwSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        time.sleep(100)
        browser.quit()
    def tcp_config(self,tcp_target,tcp_port):
        browser = self.driver
        browser.get(self.base_url + "settings.html")
        browser.find_element_by_xpath("//div[@id='pageSettings']/div[2]/ul/li[6]/div/div/a/span").click()
        browser.find_element_by_css_selector("#wwwTcp > span.ui-btn-inner > span.ui-btn-text").click()
        browser.find_element_by_id("wwwtarget").clear()
        browser.find_element_by_id("wwwtarget").send_keys(tcp_target)
        browser.find_element_by_id("wwwport").clear()
        browser.find_element_by_id("wwwport").send_keys(tcp_port)
        browser.find_element_by_css_selector("#wwwSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        #browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        #time.sleep(20)
        #browser.quit()
    def ping_config_retest(self,ping_target):
        browser = self.driver
        browser.get(self.base_url + "settings.html")
        browser.find_element_by_xpath("//div[@id='pageSettings']/div[2]/ul/li[6]/div/div/a/span").click()
        browser.find_element_by_css_selector("#wwwPing > span.ui-btn-inner").click()
        browser.find_element_by_id("wwwtarget").clear()
        browser.find_element_by_id("wwwtarget").send_keys(ping_target)
        browser.find_element_by_css_selector("#wwwSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        time.sleep(100)
        browser.quit()
    def ping_config(self,ping_target):
        browser = self.driver
        browser.get(self.base_url + "settings.html")
        browser.find_element_by_xpath("//div[@id='pageSettings']/div[2]/ul/li[6]/div/div/a/span").click()
        browser.find_element_by_css_selector("#wwwPing > span.ui-btn-inner").click()
        browser.find_element_by_id("wwwtarget").clear()
        browser.find_element_by_id("wwwtarget").send_keys(ping_target)
        browser.find_element_by_css_selector("#wwwSubmit > span.ui-btn-inner").click()
        browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
        #browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
        #time.sleep(20)
        #browser.quit()

    def proxy_on_config(self,server,port,username,password):
        browser = self.driver
        browser.get(self.base_url + "settings.html")
        browser.find_element_by_css_selector("#proxyLi > div.ui-btn-inner.ui-li > div.ui-btn-text > a.ui-jf-config-link.ui-link-inherit > h3.ui-li-heading").click()
        browser.find_element_by_css_selector("#proxyEnable > span.ui-btn-inner").click()
        browser.find_element_by_id("proxyServer").clear()
        browser.find_element_by_id("proxyServer").send_keys(server)
        browser.find_element_by_id("proxyPort").clear()
        browser.find_element_by_id("proxyPort").send_keys(port)
        browser.find_element_by_id("proxyUsrName").clear()
        browser.find_element_by_id("proxyUsrName").send_keys(username)
        browser.find_element_by_id("proxyPwd").clear()
        browser.find_element_by_id("proxyPwd").send_keys(password)
        browser.find_element_by_css_selector("#proxySubmit > span.ui-btn-inner").click()
    def proxy_off_config(self):
        browser = self.driver
        browser.get(self.base_url + "index.html")
        browser.find_element_by_xpath("//img[@alt='setup']").click()
        browser.find_element_by_id("proxyCurSetting").click()
        browser.find_element_by_css_selector("#proxyDisable > span.ui-btn-inner > span.ui-btn-text > span.btnText").click()
        browser.find_element_by_css_selector("#proxySubmit > span.ui-btn-inner > span.ui-btn-text > span.btnText").click()





