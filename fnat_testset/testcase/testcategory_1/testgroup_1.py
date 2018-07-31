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
    print "Method setUp in class testclass_1"
    print('These are led events testset')

def tearDown():
    print "Method tearDown in class testclass_1"
    print('These are led events testset')

def testmethod_1():
    '''<case_id>10</case_id>'''
    print "Method testmethod_1 in class testclass_1"
    #d = FnatDevice("0c05b1d4dbc84ce8")
    #d.press.home()
    #assert True
    pass
def testmethod_2():
    '''<case_id>11</case_id>'''
    print "Method testmethod_1 in class testclass_1"
    #d = FnatDevice("0c05b1d4dbc84ce8")
    #d.press.home()
    #assert True
    pass
def testmethod_3():
    '''<case_id>12</case_id>'''
    print "Method testmethod_1 in class testclass_1"
    #d = FnatDevice("0c05b1d4dbc84ce8")
    #d.press.home()
    #assert True
    pass

def testmethod_4():
    '''<case_id>1</case_id>'''
    print "Method testmethod_4 in class testclass_1"
    print "Method GW empty, DNS empty, WWW hostname in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.ping_config('www.baidu.com')
    time.sleep(3)
    #ui_operation.proxy_on_config('129.196.210.231','80','administrator','1qaz@WSX')
    time.sleep(5)
    ui_operation.static_config_retest('192.168.100.33','255.255.255.0','0.0.0.0','0.0.0.0')
    scheme.activate()
    browser = webdriver.Firefox()
    browser.get('http://172.16.9.9')
    time.sleep(10)
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
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tNONE'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
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

def testmethod_5():
    '''<case_id>2</case_id>'''
    print "Method testmethod_5 in class testclass_1"
    print "Method GW empty, DNS empty, WWW IP, same subnet, reachable in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','0.0.0.0','0.0.0.0')
    time.sleep(5)
    ui_operation.ping_config_retest('192.168.100.1')
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
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tNONE'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
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
def testmethod_6():
    '''<case_id>3</case_id>'''
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
def testmethod_7():
    '''<case_id>4</case_id>'''
    print "Method testmethod_7 in class testclass_1"
    print "Method GW emtpy, DNS empty, WWW IP, same subnet, arp failed in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','0.0.0.0','0.0.0.0')
    time.sleep(5)
    ui_operation.ping_config_retest('192.168.100.2')
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
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tNONE'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
    dhcp_test = UITest()
    dhcp_test.dhcp_config_retest()
    time.sleep(15)
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
def testmethod_8():
    '''<case_id>4</case_id>'''
    print "Method testmethod_8 in class testclass_1"
    print "Method GW empty, DNS empty, WWW IP, diffirent subent in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','0.0.0.0','0.0.0.0')
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
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tNONE'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
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
def testmethod_9():
    '''<case_id>5</case_id>'''
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
def testmethod_10():
    '''<case_id>6</case_id>'''
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
def testmethod_11():
    '''<case_id>7</case_id>'''
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
def testmethod_12():
    '''<case_id>8</case_id>'''
    print "Method testmethod_12 in class testclass_1"
    print "Method GW empty, DNS same subnet set, WWW hostname, diffirent subnet in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','0.0.0.0','192.168.100.1')
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
    known_GW_value = 'http://172.16.9.9/images/gatewayblack.png'
    known_cloud_value = 'http://172.16.9.9/images/cloudred.png'
    assert ipConfig_value == known_ipConfig_value
    assert GW_value == known_GW_value
    assert cloud_value == known_cloud_value
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tNONE'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
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
    print("dhcp_color")
    assert www_color == u'red'
def testmethod_13():
    '''<case_id>9</case_id>'''
    print "Method testmethod_13 in class testclass_1"
    print "Method GW empty, DNS same subnet, DNS service down, WWW hostname in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    down_dns = DNS()
    down_dns.set_dns_stop()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','0.0.0.0','192.168.100.1')
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
def testmethod_14():
    '''<case_id>13</case_id>'''
    print "Method testmethod_14 in class testclass_1"
    print "Method GW empty, DNS different subnet, WWW hostname in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','0.0.0.0','192.168.1.100')
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
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tNONE'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
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
def testmethod_15():
    '''<case_id>14</case_id>'''
    print "Method testmethod_15 in class testclass_1"
    print "Method GW set, DNS empty, WWW hostname in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','192.168.100.1','0.0.0.0')
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
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tGREEN'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
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
def testmethod_16():
    '''<case_id>15</case_id>'''
    print "Method testmethod_16 in class testclass_1"
    print "Method GW set incorrect, WWW different subnet in class testclass_1"
    __author__ = 'bzhang4'
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    ui_operation = UITest()
    ui_operation.static_config('192.168.100.33','255.255.255.0','192.168.100.210','192.168.100.1')
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
    #ser = serial.Serial()
    #ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'
    #ser.open()
    #assert ser.isOpen()
    #ser.write('leds\n')
    #ser.inWaiting()
    #b = ser.read(110)
    #str1 = bytes.decode(b)
    #print(str1)
    #dhcp_led = 'DHCP:\tGREEN'
    #GW_led = 'GW:\tRED'
    #www_led = 'WWW:\tRED'
    #assert str1.find(dhcp_led) != -1
    #assert str1.find(GW_led) != -1
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
    print('GW_color is %s' % GW_color)
    print('The ipConfigColor is %s' % dhcp_color)
    print('The wwwColor is %s' % www_color)
    assert dhcp_color == u'green'
    assert www_color == u'red'
    assert GW_color == u'red'






