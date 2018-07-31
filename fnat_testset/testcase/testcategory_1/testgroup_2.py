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

def setUp():
    print "Method setUp in class testclass_2"
    print('These are Static IP Test testset')

def tearDown():
    print "Method tearDown in class testclass_2"
    print('These are Static IP Test testset')

def testmethod_1():
    '''<case_id>6</case_id>'''

    print "Method testmethod_1 in class testclass_2"
    print "Method Assign IP address by static in class testclass_2"
    scheme = Scheme.find('wlan0','43211234')
    time.sleep(5)
    scheme.activate()
    static_test = UITest()
    static_test.static_config_retest('192.168.100.243','255.255.255.0','0.0.0.0','0.0.0.0')
    browser = webdriver.Firefox()
    browser.get('http://172.16.9.9')
    time.sleep(3)
    ipConfigHeadIcon_value = browser.find_element_by_id("ipConfigHeadIcon").get_attribute('src')
    known_ipConfigHeadIcon_value = 'http://172.16.9.9/images/dhcpgreen.png'
    assert known_ipConfigHeadIcon_value == ipConfigHeadIcon_value
    ipConfigTitle_value = browser.find_element_by_id("ipConfigTitle").text
    assert ipConfigTitle_value == '192.168.100.243'
    print("ipConfigTitle = %s" % ipConfigTitle_value)
    browser.find_element_by_id("ipConfigHeadIcon").click()
    dhcp_name = browser.find_element_by_id("dhcpName").text
    dhcp_subnet = browser.find_element_by_id("dhcpSubnet").text
    dhcp_dns1 = browser.find_element_by_id("dhcpDns1").text
    assert dhcp_name == 'Server:'
    assert dhcp_subnet == '255.255.255.0'
    assert dhcp_dns1 == 'DNS:'
    browser.quit()

def testmethod_2():
    print "Method testmethod_2 in class testclass_2"
    print "Method Dupicate IP address detection in class testclass_2"
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    static_test = UITest()
    static_test.static_config_retest('192.168.100.1','255.255.255.0','0.0.0.0','0.0.0.0')
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
    assert ipConfigTitle_value == '192.168.100.1'
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


def testmethod_3():
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

