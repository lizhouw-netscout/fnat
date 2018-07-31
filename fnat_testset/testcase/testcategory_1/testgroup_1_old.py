from fnat_dev import FnatDevice
from switch import Switch
import time
import sys
import os
from gateway import Gateway
from dhcp import DHCP
from dns import DNS
from nistnet import Nistnet
from demo import UITest
import serial
import pymongo
from pymongo import MongoClient
from selenium import webdriver
from wifi import Cell,Scheme
from hp2910 import HP2910


class testclass_1:
    def setUp(self):
        print "Method setUp in class testclass_1"
        print('These are led events testset')

    def tearDown(self):
        print "Method tearDown in class testclass_1"
        print('These are led events testset')

    def testmethod_1(self):
        print "Method testmethod_1 in class testclass_1"
        d = FnatDevice("0c05b1d4dbc84ce8")
        d.press.home()
        assert True

    def testmethod_2(self):
        print('GW empty,DNS empty,WWW hostname')
        __author__ = 'bzhang4'
        class UITest():
            def __init__(self):
                self.driver = webdriver.Firefox()
                self.driver.implicitly_wait(90)
                self.base_url = "http://172.16.9.9/"
            def dhcp_config(self):
                browser = self.driver
                browser.get(self.base_url)
                time.sleep(5)
                browser.find_element_by_xpath("//img[@alt='setup']").click()
                time.sleep(1)
                browser.find_element_by_css_selector("span.ui-jf-icon.ui-jf-arrow-next").click()
                browser.find_element_by_css_selector("#dhcpIp > span.ui-btn-inner > span.ui-btn-text").click()
                browser.find_element_by_css_selector("#ipConfigSubmit > span.ui-btn-inner").click()
                browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
                browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
                time.sleep(20)
                exp_value = 'http://172.16.9.9/images/poeblack.png'
                real_value = browser.find_element_by_id("poeHeadIcon").get_attribute('src')
                browser.quit()
                if exp_value != real_value:
                    assert True        
                else:
                    assert False
                #browser.quit()
        class serial_re():
            def serial_test(self):
                ser=serial.Serial()
                ser.baudrate = 115200
                ser.port = '/dev/ttyUSB0'
                ser.open()
                ser.isOpen()
                assert True
                ser.write(b'leds')
                b = ser.read(140)
                time.sleep(5)
                str1 = bytes.decode(b)
                str2 = "PoE:\tNONE"
                value = str1.find(str2)
                print(value)
                assert value != -1
                ser.close()


        #b = Switch()
        #b.set_poe_disable('7')
        #time.sleep(20)
        #######################################
        #wifi_test = WiFi()
        #wifi_test.wifi_conn('wlan0','1234')
        #time.sleep(5)
        #cell = Cell.all('wlan0')[0]
        #time.sleep(10)
        #scheme = Scheme.for_cell('wlan0','1234',cell,passkey=None)
        #scheme.save()
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ########################################
        ui_operation = UITest()
        ui_operation.dhcp_config()
        #######################################
        #s = serial_re()
        #s.serial_test()
        #########################################
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": False}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        c = aa['poeColor']
        print('The poeColor is %s' % c)
        assert c == u'green'
    def testmethod_3(self):
        print "Method GW empty, DNS empty, WWW IP, same subnet, reachable in class Led_events"
        __author__ = 'bzhang4'
        class UITest():
            def __init__(self):
                self.driver = webdriver.Firefox()
                self.driver.implicitly_wait(90)
                self.base_url = "http://172.16.9.9/"
            def dhcp_config(self):
                browser = self.driver
                browser.get(self.base_url)
                time.sleep(5)
                browser.find_element_by_xpath("//img[@alt='setup']").click()
                time.sleep(1)
                browser.find_element_by_css_selector("span.ui-jf-icon.ui-jf-arrow-next").click()
                browser.find_element_by_css_selector("#dhcpIp > span.ui-btn-inner > span.ui-btn-text").click()
                browser.find_element_by_css_selector("#ipConfigSubmit > span.ui-btn-inner").click()
                browser.find_element_by_css_selector("img.ui-jf-icon-nav-bar").click()
                browser.find_element_by_xpath("//a[@id='btnResPageRetest']/span/span/div").click()
                time.sleep(20)
                exp_value = 'http://172.16.9.9/images/poeblack.png'
                real_value = browser.find_element_by_id("poeHeadIcon").get_attribute('src')
                browser.quit()
                if exp_value != real_value:
                    assert True        
                else:
                    assert False
        #######################################
        #wifi_test = WiFi()
        #wifi_test.wifi_conn('wlan0','1234')
        #time.sleep(5)
        #cell = Cell.all('wlan0')[0]
        #time.sleep(10)
        #scheme = Scheme.for_cell('wlan0','1234',cell,passkey=None)
        #scheme.save()
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ########################################
        ui_operation = UITest()
        ui_operation.dhcp_config()
        #######################################
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": False}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        c = aa['poeColor']
        print('The poeColor is %s' % c)
        assert c != u'green'

    def testmethod_4(self):
        print "Method testmethod_4 in class testclass_1"
        print "Method GW empty, DNS empty, WWW hostname in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.ping_config('www.baidu.com')
        time.sleep(3)
        ui_operation.proxy_on_config('129.196.210.231','80','administrator','1qaz@WSX')
        time.sleep(5)
        ui_operation.static_config_retest('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_5(self):
        print "Method testmethod_5 in class testclass_1"
        print "Method GW empty, DNS empty, WWW IP, same subnet, reachable in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.2.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudgreen.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'green'
    def testmethod_6(self):
        print "Method testmethod_6 in class testclass_1"
        print "GW empty, DNS empty, WWW IP, same subnet, fw enable in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        firewall = Gateway()
        firewall.set_firewall_enable()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.2.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        firewall1 = Gateway()
        firewall1.set_firewall_disable()
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_7(self):
        print "Method testmethod_7 in class testclass_1"
        print "Method GW emtpy, DNS empty, WWW IP, same subnet, arp failed in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.2.2')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_8(self):
        print "Method testmethod_8 in class testclass_1"
        print "Method GW empty, DNS empty, WWW IP, diffirent subent in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.1.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_9(self):
        print "Method testmethod_9 in class testclass_1"
        print "Method GW empty, DNS same subnet set, WWW hostname, same subnet, reachable in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudgreen.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'green'
    def testmethod_10(self):
        print "Method testmethod_10 in class testclass_1"
        print "Method GW empty, DNS same subnet set, WWW hostname, same subnet, fw enable in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        firewall = Gateway()
        firewall.set_firewall_enable()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        firewall1 = Gateway()
        firewall1.set_firewall_disable()
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False

        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_11(self):
        print "Method testmethod_11 in class testclass_1"
        print "Method GW empty, DNS same subnet set, WWW hostname,same subnet, arp failed in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('c.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_12(self):
        print "Method testmethod_12 in class testclass_1"
        print "Method GW empty, DNS same subnet set, WWW hostname, diffirent subnet in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.1.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_13(self):
        print "Method testmethod_13 in class testclass_1"
        print "Method GW empty, DNS same subnet, DNS service down, WWW hostname in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        down_dns = DNS()
        down_dns.set_dns_stop()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        up_dns = DNS()
        up_dns.set_dns_start()
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_14(self):
        print "Method testmethod_14 in class testclass_1"
        print "Method GW empty, DNS different subnet, WWW hostname in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.1.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_15(self):
        print "Method testmethod_15 in class testclass_1"
        print "Method GW set, DNS empty, WWW hostname in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','192.168.2.200','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewaygreen.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tGREEN'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        GW_color = aa['routerColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
        assert GW_color == u'green'
    def testmethod_16(self):
        print "Method testmethod_16 in class testclass_1"
        print "Method GW set incorrect, WWW different subnet in class testclass_1"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','192.168.2.210','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('www.baidu.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayred.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tRED'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False

        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        GW_color = aa['routerColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
        assert GW_color == u'red'


class testclass_2:
    def setUp(self):
        print "Method setUp in class testclass_2"
        print('These are Static IP Test testset')

    def tearDown(self):
        print "Method tearDown in class testclass_2"
        print('These are Static IP Test testset')

    def testmethod_1(self):
        print "Method testmethod_1 in class testclass_2"
        print "Method Assign IP address by static in class testclass_2"
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        static_test = UITest()
        static_test.static_config_retest('192.168.2.243','255.255.255.0','0.0.0.0','0.0.0.0')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfigHeadIcon_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        known_ipConfigHeadIcon_value = 'http://172.16.9.9/images/dhcpgreen.png'
        assert known_ipConfigHeadIcon_value == ipConfigHeadIcon_value
        ipConfigTitle_value = browser.find_element_by_id("ipConfigTitle").text
        assert ipConfigTitle_value == '192.168.2.243'
        print("ipConfigTitle = %s" % ipConfigTitle_value)
        browser.find_element_by_id("ipConfigHeadIcon").click()
        dhcp_name = browser.find_element_by_id("dhcpName").text
        dhcp_subnet = browser.find_element_by_id("dhcpSubnet").text
        dhcp_dns1 = browser.find_element_by_id("dhcpDns1").text
        assert dhcp_name == 'Server:'
        assert dhcp_subnet == '255.255.255.0'
        assert dhcp_dns1 == 'DNS:'
        browser.quit()

    def testmethod_2(self):
        print "Method testmethod_2 in class testclass_2"
        print "Method Dupicate IP address detection in class testclass_2"
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        static_test = UITest()
        static_test.static_config_retest('192.168.2.200','255.255.255.0','0.0.0.0','0.0.0.0')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfigHeadIcon_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        gateHeadIcon_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        wwwHeadIcon_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        assert ipConfigHeadIcon_value == 'http://172.16.9.9/images/dhcpred.png'
        assert gateHeadIcon_value == 'http://172.16.9.9/images/gatewayblack.png'
        assert wwwHeadIcon_value == 'http://172.16.9.9/images/cloudblack.png'
        ipConfigTitle_value = browser.find_element_by_id("ipConfigTitle").text
        assert ipConfigTitle_value == '192.168.2.200'
        print("ipConfigTitle = %s" % ipConfigTitle_value)
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False

        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        ipconfig_value = aa['ipConfigIp']
        assert dhcp_color == u'red'
        assert ipconfig_value == u'192.168.2.200'


    def testmethod_3(self):
        print "Method testmethod_3 in class testclass_2"
        print "Method set ip addr, subnet, and dns which is out of subnet in class testclass_2"
        static_test = UITest()
        static_test.static_config('192.168.2.243','255.255.255.0','0.0.0.0','192.168.1.100')
        static_test.ping_config_retest('www.baidu.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfigHeadIcon_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        gateHeadIcon_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        wwwHeadIcon_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        assert ipConfigHeadIcon_value == 'http://172.16.9.9/images/dhcpgreen.png'
        assert gateHeadIcon_value == 'http://172.16.9.9/images/gatewayblack.png'
        assert wwwHeadIcon_value == 'http://172.16.9.9/images/cloudred.png'
        ipConfigTitle_value = browser.find_element_by_id("ipConfigTitle").text
        assert ipConfigTitle_value == '192.168.2.243'
        print("ipConfigTitle = %s" % ipConfigTitle_value)
        browser.find_element_by_id("ipConfigHeadIcon").click()
        dhcp_dns1 = browser.find_element_by_id("dhcpDns1").text
        assert dhcp_dns1 == 'DNS:192.168.1.100'
        browser.find_element_by_id("wwwHeadIcon").click()
        www_ip = browser.find_element_by_id("wwwIp").text
        assert www_ip == "IP:"
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        dns_value = aa['dns']
        www_value = aa['www']
        dns_value_1 = dns_value[0]
        dns_value_2 = dns_value_1['dnsIp']
        www_value_1 = www_value[0]
        www_value_2 = www_value_1['wwwIp']
        assert dhcp_color == u'green'
        assert www_color == u'red'
        assert dns_value_2 == u'192.168.1.100'
        assert www_value_2 == u''
class testclass_3:
    def setUp(self):
        print "Method setUp in class testclass_3"
        print('These are TCP SYN test testset')

    def tearDown(self):
        print "Method tearDown in class testclass_3"
        print('These are TCP SYN test testset')

    def testmethod_1(self):
        print "Method testmethod_1 in class testclass_3"
        print "Method tcp port reachable in class testclass_3"
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        dhcp_test = UITest()
        dhcp_test.tcp_config('192.168.2.100','80')
        time.sleep(3)
        dhcp_test.dhcp_config_retest()
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        wwwHeadIcon_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        assert wwwHeadIcon_value == 'http://172.16.9.9/images/cloudgreen.png'
        browser.find_element_by_id('wwwHeadIcon').click()
        type_value = browser.find_element_by_id('wwwType').text
        port_value = browser.find_element_by_id("wwwPort").text
        ip_value = browser.find_element_by_id("wwwIp").text
        pingres_value = browser.find_element_by_id("wwwPingRes").text
        list1 = list(pingres_value)
        c = type(list1)
        print(c)
        #print('type_value')
        #print(type_value)
        #print('port_value')
        #print(port_value)
        #print('ip_value')
        #print(ip_value)
        print('pingres_value')
        print(pingres_value)
        assert type_value == u'Type:TCP'
        assert port_value == u'Port:80(HTTP)'
        assert ip_value == u'IP:192.168.2.100'
        #cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').get_attribute('src')
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": False}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        www_color = aa['wwwColor']
        www_value = aa['www']
        www_value_1 = www_value[0]
        wwwtype_value = www_value_1['wwwType']
        wwwip_value = www_value_1['wwwIp']
        wwwport_value = www_value_1['wwwPort']
        list2 = www_value_1['wwwConnect']
        a = type(list2)
        print(list2)

        #print('www_color')
        #print(www_color)
        #print('wwwtype_value')
        #print(wwwtype_value)
        #print('wwwip_value')
        #print(wwwip_value)
        #print('wwwport_value')
        #print(wwwport_value)
        #b = type(wwwport_value)
        #print(b)

        assert www_color == u'green'
        assert wwwtype_value == u'TCP'
        assert wwwip_value == u'192.168.2.100'
        assert wwwport_value == 80
        #for i in list1:
            #if i in list2:
                #assert True
            #else:
                #assert False
        #assert list1[0] == list2[0]
        #assert list1[1] == list2[1]
        #assert list1[2] == list2[2]


class testclass_4:
    def setUp(self):
        print "Method setUp in class testclass_4"
        print('These are led events testset')

    def tearDown(self):
        print "Method tearDown in class testclass_4"
        print('These are led events testset')

    def testmethod_1(self):
        print "Method testmethod_1 in class testclass_4"
        print "Method GW empty, DNS empty, WWW hostname in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.ping_config('www.baidu.com')
        time.sleep(3)
        ui_operation.proxy_off_config()
        time.sleep(5)
        ui_operation.static_config_retest('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_2(self):
        print "Method testmethod_2 in class testclass_4"
        print "Method GW empty, DNS empty, WWW IP, same subnet, reachable in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.2.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudgreen.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'green'
    def testmethod_3(self):
        print "Method testmethod_3 in class testclass_4"
        print "GW empty, DNS empty, WWW IP, same subnet, fw enable in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        firewall = Gateway()
        firewall.set_firewall_enable()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.2.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        firewall1 = Gateway()
        firewall1.set_firewall_disable()
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_4(self):
        print "Method testmethod_4 in class testclass_4"
        print "Method GW emtpy, DNS empty, WWW IP, same subnet, arp failed in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.2.2')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_5(self):
        print "Method testmethod_5 in class testclass_4"
        print "Method GW empty, DNS empty, WWW IP, diffirent subent in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.1.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_6(self):
        print "Method testmethod_6 in class testclass_4"
        print "Method GW empty, DNS same subnet set, WWW hostname, same subnet, reachable in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudgreen.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'green'
    def testmethod_7(self):
        print "Method testmethod_7 in class testclass_4"
        print "Method GW empty, DNS same subnet set, WWW hostname, same subnet, fw enable in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        firewall = Gateway()
        firewall.set_firewall_enable()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        firewall1 = Gateway()
        firewall1.set_firewall_disable()
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False

        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_8(self):
        print "Method testmethod_8 in class testclass_4"
        print "Method GW empty, DNS same subnet set, WWW hostname,same subnet, arp failed in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('c.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_9(self):
        print "Method testmethod_9 in class testclass_4"
        print "Method GW empty, DNS same subnet set, WWW hostname, diffirent subnet in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('192.168.1.200')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        time.sleep(5)
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_10(self):
        print "Method testmethod_10 in class testclass_4"
        print "Method GW empty, DNS same subnet, DNS service down, WWW hostname in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        down_dns = DNS()
        down_dns.set_dns_stop()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        up_dns = DNS()
        up_dns.set_dns_start()
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_11(self):
        print "Method testmethod_11 in class testclass_4"
        print "Method GW empty, DNS different subnet, WWW hostname in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','0.0.0.0','192.168.1.100')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tNONE'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
    def testmethod_12(self):
        print "Method testmethod_12 in class testclass_4"
        print "Method GW set, DNS empty, WWW hostname in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','192.168.2.200','0.0.0.0')
        time.sleep(5)
        ui_operation.ping_config_retest('a.fnet.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewaygreen.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tGREEN'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        GW_color = aa['routerColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
        assert GW_color == u'green'
    def testmethod_13(self):
        print "Method testmethod_13 in class testclass_4"
        print "Method GW set incorrect, WWW different subnet in class testclass_4"
        __author__ = 'bzhang4'
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        ui_operation = UITest()
        ui_operation.static_config('192.168.2.33','255.255.255.0','192.168.2.210','192.168.2.100')
        time.sleep(5)
        ui_operation.ping_config_retest('www.baidu.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfig_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        GW_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        cloud_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        print(cloud_value)
        known_ipConfig_value = 'http://172.16.9.9/images/dhcpgreen.png'
        known_GW_value = 'http://172.16.9.9/images/gatewayred.png'
        known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
        assert ipConfig_value == known_ipConfig_value
        assert GW_value == known_GW_value
        assert cloud_value == known_cloud_value
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = '/dev/ttyUSB0'
        ser.open()
        assert ser.isOpen()
        ser.write('leds\n')
        ser.inWaiting()
        b = ser.read(110)
        str1 = bytes.decode(b)
        print(str1)
        dhcp_led = 'DHCP:\tGREEN'
        GW_led = 'GW:\tRED'
        #www_led = 'WWW:\tRED'
        assert str1.find(dhcp_led) != -1
        assert str1.find(GW_led) != -1
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False

        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        GW_color = aa['routerColor']
        print('The ipConfigColor is %s' % dhcp_color)
        print('The wwwColor is %s' % www_color)
        assert dhcp_color == u'green'
        assert www_color == u'red'
        assert GW_color == u'red'


class testclass_5:
    def setUp(self):
        print "Method setUp in class testclass_5"
        print('These are Static IP Test testset')

    def tearDown(self):
        print "Method tearDown in class testclass_5"
        print('These are Static IP Test testset')

    def testmethod_1(self):
        print "Method testmethod_1 in class testclass_5"
        print "Method Assign IP address by static in class testclass_5"
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        static_test = UITest()
        static_test.static_config_retest('192.168.2.243','255.255.255.0','0.0.0.0','0.0.0.0')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfigHeadIcon_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        known_ipConfigHeadIcon_value = 'http://172.16.9.9/images/dhcpgreen.png'
        assert known_ipConfigHeadIcon_value == known_ipConfigHeadIcon_value
        ipConfigTitle_value = browser.find_element_by_id("ipConfigTitle").text
        assert ipConfigTitle_value == '192.168.2.243'
        print("ipConfigTitle = %s" % ipConfigTitle_value)
        browser.find_element_by_id("ipConfigHeadIcon").click()
        dhcp_name = browser.find_element_by_id("dhcpName").text
        dhcp_subnet = browser.find_element_by_id("dhcpSubnet").text
        dhcp_dns1 = browser.find_element_by_id("dhcpDns1").text
        assert dhcp_name == 'Server:'
        assert dhcp_subnet == '255.255.255.0'
        assert dhcp_dns1 == 'DNS:'
        browser.quit()

    def testmethod_2(self):
        print "Method testmethod_2 in class testclass_5"
        print "Method Dupicate IP address detection in class testclass_5"
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        static_test = UITest()
        static_test.static_config_retest('192.168.2.200','255.255.255.0','0.0.0.0','0.0.0.0')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfigHeadIcon_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        gateHeadIcon_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        wwwHeadIcon_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        assert ipConfigHeadIcon_value == 'http://172.16.9.9/images/dhcpred.png'
        assert gateHeadIcon_value == 'http://172.16.9.9/images/gatewayblack.png'
        assert wwwHeadIcon_value == 'http://172.16.9.9/images/cloudblack.png'
        ipConfigTitle_value = browser.find_element_by_id("ipConfigTitle").text
        assert ipConfigTitle_value == '192.168.2.200'
        print("ipConfigTitle = %s" % ipConfigTitle_value)
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False

        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        ipconfig_value = aa['ipConfigIp']
        assert dhcp_color == u'red'
        assert ipconfig_value == u'192.168.2.200'


    def testmethod_3(self):
        print "Method testmethod_3 in class testclass_5"
        print "Method set ip addr, subnet, and dns which is out of subnet in class testclass_5"
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        static_test = UITest()
        static_test.static_config('192.168.2.243','255.255.255.0','0.0.0.0','192.168.1.100')
        static_test.ping_config_retest('www.baidu.com')
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        ipConfigHeadIcon_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
        gateHeadIcon_value = browser.find_element_by_id("gateHeadIcon").get_attribute('src')
        wwwHeadIcon_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        assert ipConfigHeadIcon_value == 'http://172.16.9.9/images/dhcpgreen.png'
        assert gateHeadIcon_value == 'http://172.16.9.9/images/gatewayblack.png'
        assert wwwHeadIcon_value == 'http://172.16.9.9/images/cloudred.png'
        ipConfigTitle_value = browser.find_element_by_id("ipConfigTitle").text
        assert ipConfigTitle_value == '192.168.2.243'
        print("ipConfigTitle = %s" % ipConfigTitle_value)
        browser.find_element_by_id("ipConfigHeadIcon").click()
        dhcp_dns1 = browser.find_element_by_id("dhcpDns1").text
        assert dhcp_dns1 == 'DNS:192.168.1.100'
        browser.find_element_by_id("wwwHeadIcon").click()
        www_ip = browser.find_element_by_id("wwwIp").text
        assert www_ip == "IP:"
        dhcp_test = UITest()
        dhcp_test.dhcp_config_retest()
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": True}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        dhcp_color = aa['ipConfigColor']
        www_color = aa['wwwColor']
        dns_value = aa['dns']
        www_value = aa['www']
        dns_value_1 = dns_value[0]
        dns_value_2 = dns_value_1['dnsIp']
        www_value_1 = www_value[0]
        www_value_2 = www_value_1['wwwIp']
        assert dhcp_color == u'green'
        assert www_color == u'red'
        assert dns_value_2 == u'192.168.1.100'
        assert www_value_2 == u''
class testclass_6:
    def setUp(self):
        print "Method setUp in class testclass_6"
        print('These are TCP SYN test testset')

    def tearDown(self):
        print "Method tearDown in class testclass_6"
        print('These are TCP SYN test testset')

    def testmethod_1(self):
        print "Method testmethod_1 in class testclass_6"
        print "Method tcp port reachable in class testclass_6"
        scheme = Scheme.find('wlan0','1234')
        time.sleep(5)
        scheme.activate()
        dhcp_test = UITest()
        dhcp_test.tcp_config('192.168.2.100','80')
        time.sleep(3)
        dhcp_test.dhcp_config_retest()
        browser = webdriver.Firefox()
        browser.get('http://172.16.9.9')
        time.sleep(3)
        wwwHeadIcon_value = browser.find_element_by_id("wwwHeadIcon").get_attribute('src')
        assert wwwHeadIcon_value == 'http://172.16.9.9/images/cloudgreen.png'
        browser.find_element_by_id('wwwHeadIcon').click()
        type_value = browser.find_element_by_id('wwwType').text
        port_value = browser.find_element_by_id("wwwPort").text
        ip_value = browser.find_element_by_id("wwwIp").text
        pingres_value = browser.find_element_by_id("wwwPingRes").text
        list1 = list(pingres_value)
        c = type(list1)
        print(c)
        #print('type_value')
        #print(type_value)
        #print('port_value')
        #print(port_value)
        #print('ip_value')
        #print(ip_value)
        print('pingres_value')
        print(pingres_value)
        assert type_value == u'Type:TCP'
        assert port_value == u'Port:80(HTTP)'
        assert ip_value == u'IP:192.168.2.100'
        #cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').get_attribute('src')
        cloudHeadIcon_value = browser.find_element_by_id('cloudHeadIcon').is_displayed()
        print(cloudHeadIcon_value)
        browser.quit()
        if cloudHeadIcon_value == False:
            assert True
        else:
            assert False
        MONGOHQ_URL='mongodb://linksprinterzbc:1qaz2WSX12@c494.candidate.42.mongolayer.com:10494/linksprinter-new-test'
        DATABASE = 'linksprinter-new-test'
        mongoClient = MongoClient(MONGOHQ_URL)
        linksprinter = mongoClient[DATABASE]
        collection=linksprinter.results
        print(collection)
        a = collection.find({"unit_mac": "00C017-090909","cached": False}).sort([("created_at",pymongo.DESCENDING)]).limit(1)
        aa = dict(a[0])
        www_color = aa['wwwColor']
        www_value = aa['www']
        www_value_1 = www_value[0]
        wwwtype_value = www_value_1['wwwType']
        wwwip_value = www_value_1['wwwIp']
        wwwport_value = www_value_1['wwwPort']
        list2 = www_value_1['wwwConnect']
        a = type(list2)
        print(list2)

        #print('www_color')
        #print(www_color)
        #print('wwwtype_value')
        #print(wwwtype_value)
        #print('wwwip_value')
        #print(wwwip_value)
        #print('wwwport_value')
        #print(wwwport_value)
        #b = type(wwwport_value)
        #print(b)

        assert www_color == u'green'
        assert wwwtype_value == u'TCP'
        assert wwwip_value == u'192.168.2.100'
        assert wwwport_value == 80
        #for i in list1:
            #if i in list2:
                #assert True
            #else:
                #assert False
        #assert list1[0] == list2[0]
        #assert list1[1] == list2[1]
        #assert list1[2] == list2[2]








