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
#from wifi import Cell,Scheme
from hp2910 import HP2910
from uiautomator import device as d

def setUp():
    print "Method setUp in class testclass_5"
    print('These are Speed_duplex testset')

def tearDown():
    print "Method tearDown in class testclass_5"
    print('These are Speed_duplex testset')

def testmethod_1():
    '''<case_id>1</case_id>'''
    print "Method testmethod_1 in class Speed_duplex_test suite"
    print "Method speed-duplex 10-half test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','10-half',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '10'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '10'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '10'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False
def testmethod_2():
    '''<case_id>2</case_id>'''
    print "Method testmethod_2 in class Speed_duplex_test suite"
    print "Method speed-duplex 100-half test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','100-half',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '100'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '100'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '100'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False


def testmethod_3():
    '''<case_id>3</case_id>'''
    print "Method testmethod_3 in class Speed_duplex_test suite"
    print "Method speed-duplex 10-full test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','10-full',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '10'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '10'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '10'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False


def testmethod_4():
    '''<case_id>4</case_id>'''
    print "Method testmethod_4 in class Speed_duplex_test suite"
    print "Method speed-duplex 100-full test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','100-full',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '100'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '100'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '100'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False

def testmethod_5():
    '''<case_id>5</case_id>'''
    print "Method testmethod_5 in class Speed_duplex_test suite"
    print "Method speed-duplex 1000-full test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','1000-full',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '100'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '100'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '100'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False
def testmethod_6():
    '''<case_id>6</case_id>'''
    print "Method testmethod_6 in class Speed_duplex_test suite"
    print "Method speed-duplex auto test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','auto',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        advertised_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_speed_desc').text
        print(advertised_speed_1)
        string_advertised_speed_1 = str(advertised_speed_1)
        assert string_advertised_speed_1 == '10/100/1000'
        
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '1000'

        advertised_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_duplex_desc').text
        print(advertised_duplex_1)
        string_advertised_duplex_1 = str(advertised_duplex_1)
        assert string_advertised_duplex_1 == 'HDx/FDx'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'FDx'

        rx_pair_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/rx_pair_desc').text
        print(rx_pair_1)
        string_rx_pair_1 = str(rx_pair_1)
        assert string_rx_pair_1 == 'All'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '10'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '10'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_4)
        string_link_4 = str(link_results_4)
        assert string_link_4 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_4)
        string_actual_speed_4 = str(actual_speed_4)
        assert string_actual_speed_4 == '100'

        actual_duplex_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_4)
        string_actual_duplex_4 = str(actual_duplex_4)
        assert string_actual_duplex_4 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_4)
        string_cloud_status_4 = str(cloud_status_4)
        assert string_cloud_status_4 == 'green'
        
        cloud_value_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_4 = str(cloud_value_4)
        assert cloud_str_4 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_5)
        string_link_5 = str(link_results_5)
        assert string_link_5 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_5)
        string_actual_speed_5 = str(actual_speed_5)
        assert string_actual_speed_5 == '100'

        actual_duplex_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_5)
        string_actual_duplex_5 = str(actual_duplex_5)
        assert string_actual_duplex_5 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_5)
        string_cloud_status_5 = str(cloud_status_5)
        assert string_cloud_status_5 == 'green'
        
        cloud_value_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_5 = str(cloud_value_5)
        assert cloud_str_5 == "Link-Live.com"


        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='1000/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_6)
        string_link_6 = str(link_results_6)
        assert string_link_6 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        advertised_speed_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_speed_desc').text
        print(advertised_speed_6)
        string_advertised_speed_6 = str(advertised_speed_6)
        assert string_advertised_speed_6 == '10/100/1000'
        
        actual_speed_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_6)
        string_actual_speed_6 = str(actual_speed_6)
        assert string_actual_speed_6 == '1000'

        advertised_duplex_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_duplex_desc').text
        print(advertised_duplex_6)
        string_advertised_duplex_6 = str(advertised_duplex_6)
        assert string_advertised_duplex_6 == 'HDx/FDx'

        actual_duplex_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_6)
        string_actual_duplex_6 = str(actual_duplex_6)
        assert string_actual_duplex_6 == 'FDx'

        rx_pair_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/rx_pair_desc').text
        print(rx_pair_6)
        string_rx_pair_6 = str(rx_pair_6)
        assert string_rx_pair_6 == 'All'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_6)
        string_cloud_status_6 = str(cloud_status_6)
        assert string_cloud_status_6 == 'green'
        
        cloud_value_6 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_6 = str(cloud_value_6)
        assert cloud_str_6 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False

def testmethod_7():
    '''<case_id>7</case_id>'''
    print "Method testmethod_7 in class Speed_duplex_test suite"
    print "Method speed-duplex auto-10 test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','auto-10',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        advertised_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_speed_desc').text
        print(advertised_speed_1)
        string_advertised_speed_1 = str(advertised_speed_1)
        assert string_advertised_speed_1 == '10'
        
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '10'

        advertised_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_duplex_desc').text
        print(advertised_duplex_1)
        string_advertised_duplex_1 = str(advertised_duplex_1)
        assert string_advertised_duplex_1 == 'HDx/FDx'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'FDx'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '10'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '10'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"

        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False

def testmethod_8():
    '''<case_id>8</case_id>'''
    print "Method testmethod_8 in class Speed_duplex_test suite"
    print "Method speed-duplex auto-100 test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','auto-100',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        advertised_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_speed_desc').text
        print(advertised_speed_1)
        string_advertised_speed_1 = str(advertised_speed_1)
        assert string_advertised_speed_1 == '100'
        
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '100'

        advertised_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_duplex_desc').text
        print(advertised_duplex_1)
        string_advertised_duplex_1 = str(advertised_duplex_1)
        assert string_advertised_duplex_1 == 'HDx/FDx'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'FDx'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '100'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '100'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False
        
def testmethod_9():
    '''<case_id>9</case_id>'''
    print "Method testmethod_9 in class Speed_duplex_test suite"
    print "Method speed-duplex auto-10-100 test in Speed_duplex_test suite"
    b = Switch()
    b.set_speed_duplex_value('8','auto-10-100',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        advertised_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_speed_desc').text
        print(advertised_speed_1)
        string_advertised_speed_1 = str(advertised_speed_1)
        assert string_advertised_speed_1 == '10/100'
        
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '100'

        advertised_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_duplex_desc').text
        print(advertised_duplex_1)
        string_advertised_duplex_1 = str(advertised_duplex_1)
        assert string_advertised_duplex_1 == 'HDx/FDx'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'FDx'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '10'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='10/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_3)
        string_link_3 = str(link_results_3)
        assert string_link_3 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_3)
        string_actual_speed_3 = str(actual_speed_3)
        assert string_actual_speed_3 == '10'

        actual_duplex_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_3)
        string_actual_duplex_3 = str(actual_duplex_3)
        assert string_actual_duplex_3 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_3)
        string_cloud_status_3 = str(cloud_status_3)
        assert string_cloud_status_3 == 'green'
        
        cloud_value_3 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_3 = str(cloud_value_3)
        assert cloud_str_3 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Half').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_4)
        string_link_4 = str(link_results_4)
        assert string_link_4 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_4)
        string_actual_speed_4 = str(actual_speed_4)
        assert string_actual_speed_4 == '100'

        actual_duplex_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_4)
        string_actual_duplex_4 = str(actual_duplex_4)
        assert string_actual_duplex_4 == 'HDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_4)
        string_cloud_status_4 = str(cloud_status_4)
        assert string_cloud_status_4 == 'green'
        
        cloud_value_4 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_4 = str(cloud_value_4)
        assert cloud_str_4 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_5)
        string_link_5 = str(link_results_5)
        assert string_link_5 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        actual_speed_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_5)
        string_actual_speed_5 = str(actual_speed_5)
        assert string_actual_speed_5 == '100'

        actual_duplex_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_5)
        string_actual_duplex_5 = str(actual_duplex_5)
        assert string_actual_duplex_5 == 'FDx'
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_5)
        string_cloud_status_5 = str(cloud_status_5)
        assert string_cloud_status_5 == 'green'
        
        cloud_value_5 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_5 = str(cloud_value_5)
        assert cloud_str_5 == "Link-Live.com"
        
    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False
    

def testmethod_10():
    '''<case_id>10</case_id>'''
    print "Method testmethod_10 in class Speed_duplex_test suite"
    print "Method speed-duplex auto-1000 test in Speed_duplex_test suite"
    b = switch()
    b.set_speed_duplex_value('8','auto-1000',None)
    time.sleep(5)
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='Auto').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_1)
        string_link_1 = str(link_results_1)
        assert string_link_1 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        advertised_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_speed_desc').text
        print(advertised_speed_1)
        string_advertised_speed_1 = str(advertised_speed_1)
        assert string_advertised_speed_1 == '1000'
        
        actual_speed_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_1)
        string_actual_speed_1 = str(actual_speed_1)
        assert string_actual_speed_1 == '1000'

        advertised_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_duplex_desc').text
        print(advertised_duplex_1)
        string_advertised_duplex_1 = str(advertised_duplex_1)
        assert string_advertised_duplex_1 == 'FDx'

        actual_duplex_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_1)
        string_actual_duplex_1 = str(actual_duplex_1)
        assert string_actual_duplex_1 == 'FDx'
        
        rx_pair_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/rx_pair_desc').text
        print(rx_pair_1)
        string_rx_pair_1 = str(rx_pair_1)
        assert string_rx_pair_1 == 'All'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_1)
        string_cloud_status_1 = str(cloud_status_1)
        assert string_cloud_status_1 == 'green'
        
        cloud_value_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_1 = str(cloud_value_1)
        assert cloud_str_1 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='1000/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

        link_results_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/link_image').description
        print(link_results_2)
        string_link_2 = str(link_results_2)
        assert string_link_2 == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()
        time.sleep(1)
        advertised_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_speed_desc').text
        print(advertised_speed_2)
        string_advertised_speed_2 = str(advertised_speed_2)
        assert string_advertised_speed_2 == '1000'
        
        actual_speed_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_speed_desc').text
        print(actual_speed_2)
        string_actual_speed_2 = str(actual_speed_2)
        assert string_actual_speed_2 == '1000'
        
        advertised_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/advertised_duplex_desc').text
        print(advertised_duplex_2)
        string_advertised_duplex_2 = str(advertised_duplex_1)
        assert string_advertised_duplex_2 == 'FDx'

        actual_duplex_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/actual_duplex_desc').text
        print(actual_duplex_2)
        string_actual_duplex_2 = str(actual_duplex_2)
        assert string_actual_duplex_2 == 'FDx'

        rx_pair_1 = d(resourceId='com.flukenetworks.yilian.prototype:id/rx_pair_desc').text
        print(rx_pair_1)
        string_rx_pair_1 = str(rx_pair_1)
        assert string_rx_pair_1 == 'All'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/link_text').click()

        cloud_status_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status_2)
        string_cloud_status_2 = str(cloud_status_2)
        assert string_cloud_status_2 == 'green'
        
        cloud_value_2 = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str_2 = str(cloud_value_2)
        assert cloud_str_2 == "Link-Live.com"

        d.click(0,28)
        time.sleep(2)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_speed').click()
        d(text='100/Full').click()
        time.sleep(1)
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(30)

    except Exception as e:
        print(e)
        #return False
        a = os.popen('adb shell ps | grep com.flukenetworks.yilian.prototype').readlines()[0]
        lis = a.split()
        lis1 = int(lis[1])
        os.system('adb shell kill -9 %d' % lis1)
        d.press.back()
        time.sleep(6)
        #return False
        assert False
    
