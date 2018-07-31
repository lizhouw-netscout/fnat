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
    print "Method setUp in class testclass_6"
    print('These are TCP SYN test testset')

def tearDown():
    print "Method tearDown in class testclass_6"
    print('These are TCP SYN test testset')

def testmethod_1():
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








