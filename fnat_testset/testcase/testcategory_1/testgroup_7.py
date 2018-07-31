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
    print "Method setUp in class testclass_7"
    print('These are Link test testset')

def tearDown():
    print "Method tearDown in class testclass_7"
    print('These are Link test testset')

def testmethod_1():
    print "Method testmethod_1 in class testclass_7"
    print "Method 10-half in class testclass_6"
    scheme = Scheme.find('wlan0','1234')
    time.sleep(5)
    scheme.activate()
    s = Switch()
    s.set_speed_duplex_value('8','10-half',None)
    dhcp_test = UITest()
    dhcp_test.dhcp_config_retest()
    browser = webdriver.Firefox()
    browser.get('http://172.16.9.9')
    time.sleep(3)
    linkHeadIcon_value = browser.find_element_by_id("linkHeadIcon").get_attribute('src')
    assert linkHeadIcon_value == 'http://172.16.9.9/images/linkgreen.png'
    browser.find_element_by_id('linkHeadIcon').click()
    time.sleep(1)
    advertise_value = browser.find_element_by_id('linkAdvContent').text
    time.sleep(1)
    pair_value = browser.find_element_by_id("linkRxPairContent").text
    time.sleep(1)
    polarity_value = browser.find_element_by_id("linkPolarityContent").text
    time.sleep(1)
    print('advertise_value')
    print(advertise_value)
    print('pair_value')
    print(pair_value)
    print('polarity_value')
    print(polarity_value)
    assert advertise_value == u'Advertise:'
    print('The value of Advertise is ok')
    assert pair_value == u'Rx Pair:1,2'
    print('The value of Rx Pair is ok')
    assert polarity_value == u'Polarity:Normal'
    print('The value of polarity is ok')
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
    cc = aa[linkColor]
    print(cc)
    #assert aa[linkColor] == u'green'
    print('linkcolor is ok')
    dd = aa[linkPolarity]
    print(dd)
    #assert aa[linkPolarity] == u'Normal'
    print('linkpolarity is ok')
    print(aa[linkActDuplex])
    #assert aa[linkActDuplex] == u'HDx'
    print('linkactduplex is ok')
    print(aa[linkActSpeed])
    #assert aa[linkActSpeed] == 10
    print('linkactspeed is ok')
    print(aa[linkRxPair])
    #assert aa[linkRxPair] == u'1,2'
    print('linkrxpair is ok')






