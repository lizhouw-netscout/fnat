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
from uiautomator import device as d

def setUp():
    #print "Method setUp in class testclass_5"
    print('These are ARP&PING function test testset')

def tearDown():
    #print "Method tearDown in class testclass_5"
    print('These are ARP&PING function test testset')

def testmethod_1():
    '''<case_id>77</case_id>'''
    print "Method testmethod_1 in class ARP&PING function test suite"
    print "Method The target is within the same subnet: ARP response not received in ARP&PING function test suite"
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        #d.drag(6,594,6,138)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        time.sleep(2)
        d.drag(6,720,6,197)
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_ip_config').click()
        time.sleep(0.5)
        d(text='Static').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/ip_address_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.63")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/subnet_mask_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("255.255.255.0")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns1_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns2_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d.drag(6,724,6,90)
        d(resourceId='com.flukenetworks.yilian.prototype:id/add_target').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_address').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.80")
        d(resourceId='android:id/button1').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/test_type_switch').click()###disable tcp###
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(50)
        static_results = d(resourceId='com.flukenetworks.yilian.prototype:id/static_image').description
        print(static_results)
        string_static = str(static_results)
        assert string_static == 'green'
        static_value = d(resourceId='com.flukenetworks.yilian.prototype:id/static_text').text
        static_str = str(static_value)
        assert static_str == "192.168.10.63"
        
        target_results = d(resourceId='com.flukenetworks.yilian.prototype:id/target_image').description
        print(target_results)
        string_target = str(target_results)
        assert string_target == 'red'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_text').click()
        target_address = d(resourceId='com.flukenetworks.yilian.prototype:id/target_address_desc').text
        print(target_address)
        string_target_address = str(target_address)
        assert string_target_address == '192.168.10.80'
        
        target_type = d(resourceId='com.flukenetworks.yilian.prototype:id/target_type_desc').text
        print(target_type)
        string_target_type = str(target_type)
        assert string_target_type == 'PING'

        tcp_ping_time = d(resourceId='com.flukenetworks.yilian.prototype:id/targets_fail_reason').text
        print(tcp_ping_time)
        string_tcp_ping_time = str(tcp_ping_time)
        assert string_tcp_ping_time == 'Can not find the target (ARP Failed)'

        
        cloud_status = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status)
        string_cloud_status = str(cloud_status)
        assert string_cloud_status == 'green'
        
        cloud_value = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str = str(cloud_value)
        assert cloud_str == "Link-Live.com"
        d.press.back()
        time.sleep(1)
        d.press.back()
        
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
    '''<case_id>79</case_id>'''
    print "Method testmethod_2 in class ARP&PING function test suite"
    print "Method The target is within the same subnet: icmp received in ARP&PING function test suite"
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        #d.drag(6,594,6,138)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        time.sleep(2)
        d.drag(6,720,6,197)
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_ip_config').click()
        time.sleep(0.5)
        d(text='Static').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/ip_address_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.63")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/subnet_mask_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("255.255.255.0")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns1_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns2_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d.drag(6,724,6,90)
        d(resourceId='com.flukenetworks.yilian.prototype:id/add_target').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_address').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/test_type_switch').click()###disable tcp###
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(50)
        static_results = d(resourceId='com.flukenetworks.yilian.prototype:id/static_image').description
        print(static_results)
        string_static = str(static_results)
        assert string_static == 'green'
        
        static_value = d(resourceId='com.flukenetworks.yilian.prototype:id/static_text').text
        static_str = str(static_value)
        assert static_str == "192.168.10.63"
        
        target_results = d(resourceId='com.flukenetworks.yilian.prototype:id/target_image').description
        print(target_results)
        string_target = str(target_results)
        assert string_target == 'green'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_text').click()
        target_address = d(resourceId='com.flukenetworks.yilian.prototype:id/target_address_desc').text
        print(target_address)
        string_target_address = str(target_address)
        assert string_target_address == '192.168.10.1'
        
        target_type = d(resourceId='com.flukenetworks.yilian.prototype:id/target_type_desc').text
        print(target_type)
        string_target_type = str(target_type)
        assert string_target_type == 'PING'

        tcp_ping_time = d(resourceId='com.flukenetworks.yilian.prototype:id/ping_time').text
        print(tcp_ping_time)
        string_tcp_ping_time = str(tcp_ping_time)
        assert string_tcp_ping_time != ' --, --, --'

        
        cloud_status = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status)
        string_cloud_status = str(cloud_status)
        assert string_cloud_status == 'green'
        
        cloud_value = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str = str(cloud_value)
        assert cloud_str == "Link-Live.com"
        d.press.back()
        time.sleep(1)
        d.press.back()
        
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
    '''<case_id>80</case_id>'''
    print "Method testmethod_3 in class ARP&PING function test suite"
    print "Method The target is out of the same subnet: ARP response not received in ARP&PING function test suite"
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        #d.drag(6,594,6,138)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        time.sleep(2)
        d.drag(6,720,6,197)
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_ip_config').click()
        time.sleep(0.5)
        d(text='Static').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/ip_address_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.63")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/subnet_mask_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("255.255.255.0")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns1_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns2_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d.drag(6,724,6,90)
        d(resourceId='com.flukenetworks.yilian.prototype:id/add_target').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_address').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.20.10")
        d(resourceId='android:id/button1').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/test_type_switch').click()###disable tcp###
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(50)
        static_results = d(resourceId='com.flukenetworks.yilian.prototype:id/static_image').description
        print(static_results)
        string_static = str(static_results)
        assert string_static == 'green'
        static_value = d(resourceId='com.flukenetworks.yilian.prototype:id/static_text').text
        static_str = str(static_value)
        assert static_str == "192.168.10.63"
        
        target_results = d(resourceId='com.flukenetworks.yilian.prototype:id/target_image').description
        print(target_results)
        string_target = str(target_results)
        assert string_target == 'red'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_text').click()
        target_address = d(resourceId='com.flukenetworks.yilian.prototype:id/target_address_desc').text
        print(target_address)
        string_target_address = str(target_address)
        assert string_target_address == '192.168.20.10'
        
        target_type = d(resourceId='com.flukenetworks.yilian.prototype:id/target_type_desc').text
        print(target_type)
        string_target_type = str(target_type)
        assert string_target_type == 'PING'

        tcp_ping_time = d(resourceId='com.flukenetworks.yilian.prototype:id/ping_time').text
        print(tcp_ping_time)
        string_tcp_ping_time = str(tcp_ping_time)
        assert string_tcp_ping_time == ' --, --, --'

        
        cloud_status = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status)
        string_cloud_status = str(cloud_status)
        assert string_cloud_status == 'green'
        
        cloud_value = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str = str(cloud_value)
        assert cloud_str == "Link-Live.com"
        d.press.back()
        time.sleep(1)
        d.press.back()
        
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
    '''<case_id>82</case_id>'''
    print "Method testmethod_3 in class ARP&PING function test suite"
    print "Method The target is out of the same subnet: ARP response not received in ARP&PING function test suite"
    try:
        d(description='Apps').click()
        d(text='LinkRunner G2').click()
        time.sleep(5)
        d.click(0,28)
        time.sleep(2)
        #d.drag(6,594,6,138)
        d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        time.sleep(2)
        d.drag(6,720,6,197)
        d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_ip_config').click()
        time.sleep(0.5)
        d(text='Static').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/ip_address_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.63")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/subnet_mask_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("255.255.255.0")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns1_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d(resourceId='com.flukenetworks.yilian.prototype:id/dns2_edit').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.10.1")
        d(resourceId='android:id/button1').click()
        time.sleep(1)
        d.drag(6,724,6,90)
        d(resourceId='com.flukenetworks.yilian.prototype:id/add_target').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_address').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text("192.168.20.1")
        d(resourceId='android:id/button1').click()
        d(resourceId='com.flukenetworks.yilian.prototype:id/test_type_switch').click()###disable tcp###
        d.press.back()
        time.sleep(1)
        d.press.back()
        time.sleep(50)
        static_results = d(resourceId='com.flukenetworks.yilian.prototype:id/static_image').description
        print(static_results)
        string_static = str(static_results)
        assert string_static == 'green'
        static_value = d(resourceId='com.flukenetworks.yilian.prototype:id/static_text').text
        static_str = str(static_value)
        assert static_str == "192.168.10.63"
        
        target_results = d(resourceId='com.flukenetworks.yilian.prototype:id/target_image').description
        print(target_results)
        string_target = str(target_results)
        assert string_target != 'red'
        
        d(resourceId='com.flukenetworks.yilian.prototype:id/target_text').click()
        target_address = d(resourceId='com.flukenetworks.yilian.prototype:id/target_address_desc').text
        print(target_address)
        string_target_address = str(target_address)
        assert string_target_address == '192.168.20.1'
        
        target_type = d(resourceId='com.flukenetworks.yilian.prototype:id/target_type_desc').text
        print(target_type)
        string_target_type = str(target_type)
        assert string_target_type == 'PING'

        tcp_ping_time = d(resourceId='com.flukenetworks.yilian.prototype:id/ping_time').text
        print(tcp_ping_time)
        string_tcp_ping_time = str(tcp_ping_time)
        assert string_tcp_ping_time != ' --, --, --'

        
        cloud_status = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image').description
        print(cloud_status)
        string_cloud_status = str(cloud_status)
        assert string_cloud_status == 'green'
        
        cloud_value = d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text').text
        cloud_str = str(cloud_value)
        assert cloud_str == "Link-Live.com"
        d.press.back()
        time.sleep(1)
        d.press.back()
        
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
        
