from fnat_dev import FnatDevice
from lrg2_app import app_lrg2
import time

def setUp():
    print('These are Static_ip_address testset')

def tearDown():
    print('These are Static_ip_address testset')

def testmethod_1():
    '''<case_id>63</case_id>'''
    print "Method testmethod_1 in class Static_ip_address_test suite"
    print "Method set the full static IP address and subnet, which is not duplicated in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "192.168.0.0", "192.168.10.1")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "red", 6)

    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 3)

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 15)

def testmethod_2():
    '''<case_id>61</case_id>'''
    print "Method testmethod_2 in class Static_ip_address_test suite"
    print "Method set the static IP address and subnet, which is not duplicated in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "", "", "")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)    

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 40, True)

    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "red", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "DNS Lookup Failed"

def testmethod_3():
    '''<case_id>65</case_id>'''
    print "Method testmethod_3 in class Static_ip_address_test suite"
    print "Method set the full static IP address and subnet, which is duplicated in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.1", "255.255.255.0", "192.168.10.1", "192.168.10.1", "192.168.10.2")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "red", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "Duplicate IP Address"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 40, True)

    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "red", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Duplicate IP Address"
        
def testmethod_4():
    '''<case_id>64</case_id>'''
    print "Method testmethod_4 in class Static_ip_address_test suite"
    print "Method set the static IP address and subnet, which is duplicated in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.1", "255.255.255.0", "", "", "")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "red", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "Duplicate IP Address"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 40, True)

    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "red", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Duplicate IP Address"
 
def testmethod_5():
    '''<case_id>66</case_id>'''
    print "Method testmethod_5 in class Static_ip_address_test suite"
    print "Method set the default gateway, which is in the subnet in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "192.168.10.1", "")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "green", 6)

    dns_value = lrg2.autotest_text_dns().text
    assert dns_value.rstrip() == "192.168.10.1"

    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 6)

    gate_value = lrg2.autotest_text_gateway().text
    assert str(gate_value) == "192.168.10.1"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "green", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Link-Live.com"
        
def testmethod_6():
    '''<case_id>67</case_id>'''
    print "Method testmethod_6 in class Static_ip_address_test suite"
    print "Method set the default gateway, which is out of the subnet in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.2.100", "192.168.10.1", "")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "green", 6)

    dns_value = lrg2.autotest_text_dns().text
    assert dns_value.rstrip() == "192.168.10.1"

    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "red", 6)

    lrg2.autotest_text_gateway().click()
    gate_value = lrg2.autotest_text_gateway_pingtime().text
    assert str(gate_value) == " --, --, --"

    lrg2.autotest_text_gateway().click()

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "red", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Can not connect to server."

def testmethod_7():
    '''<case_id>68</case_id>'''
    print "Method testmethod_7 in class Static_ip_address_test suite"
    print "Method set DNS1,not set DNS2 in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "192.168.10.1", "")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "green", 6)

    dns_value = lrg2.autotest_text_dns().text
    assert dns_value.strip() == "192.168.10.1"

    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 6)

    gate_value = lrg2.autotest_text_gateway().text
    assert str(gate_value) == "192.168.10.1"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "green", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Link-Live.com"
        
def testmethod_8():
    '''<case_id>69</case_id>'''
    print "Method testmethod_8 in class Static_ip_address_test suite"
    print "Method set DNS2,not set DNS1 in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "", "192.168.10.1")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "green", 6)

    lrg2.autotest_text_dns().click()
        
    dns_value = lrg2.autotest_detail_dns_title().text
    assert dns_value == "DNS2"

    dns_value = lrg2.autotest_text_dns().text
    assert dns_value.strip() == "192.168.10.1"

    lrg2.autotest_text_dns().click()

    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 6)

    gate_value = lrg2.autotest_text_gateway().text
    assert str(gate_value) == "192.168.10.1"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "green", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Link-Live.com"
        
def testmethod_9():
    '''<case_id>70</case_id>'''
    print "Method testmethod_9 in class Static_ip_address_test suite"
    print "Method set DNS2,set DNS1 in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "192.168.1.1", "192.168.10.1")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "red", 6)

    lrg2.autotest_text_dns().click()
 
    dns_value = lrg2.autotest_detail_dns_title().text
    assert dns_value == "DNS1"

    dns_value = lrg2.autotest_detail_dns_pingtime().text
    assert dns_value == " --, --, --"

    lrg2.autotest_text_dns().click()

    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 6)        

    gate_value = lrg2.autotest_text_gateway().text
    assert str(gate_value) == "192.168.10.1"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "green", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Link-Live.com"

def testmethod_10():
    '''<case_id>71</case_id>'''
    print "Method testmethod_10 in class Static_ip_address_test suite"
    print "Method DNS server is in the different subnet, while GW is set in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "192.168.1.1", "192.168.10.1")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "green", 6)

    lrg2.autotest_text_dns().click()
 
    dns_value_1 = lrg2.autotest_detail_dns_title()[0].text
    assert dns_value_1 == "DNS1"
  
    time.sleep(3) 
    dns_ping_1 = lrg2.autotest_detail_dns_pingtime()[0].text
    assert dns_ping_1 == " --, --, --"
       
    lrg2.autotest_text_dns().click()
 
    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 6)

    gate_value = lrg2.autotest_text_gateway().text
    assert str(gate_value) == "192.168.10.1"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "green", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Link-Live.com"

def testmethod_11():
    '''<case_id>72</case_id>'''
    print "Method testmethod_11 in class Static_ip_address_test suite"
    print "Method DNS server is in the different subnet, while GW is not set in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "192.168.1.1", "192.168.10.1")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "red", 6)

    lrg2.autotest_text_dns().click()
     
    dns_value_1 = lrg2.autotest_detail_dns_title()[0].text
    assert dns_value_1 == "DNS1"

    time.sleep(3)
    dns_value_1 = lrg2.autotest_detail_dns_pingtime()[0].text
    assert dns_value_1 != "ARP Failed"

    lrg2.autotest_text_dns().click()
        
    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "red", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "DNS Lookup Failed"

def testmethod_12():
    '''<case_id>84</case_id>'''
    print "Method testmethod_12 in class Static_ip_address_test suite"
    print "Method confirm LLT can identify the address in the subnet based on netmask is set in Static_ip_address_test suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_static_address("192.168.10.63", "255.255.255.0", "192.168.10.1", "192.168.1.1", "192.168.10.1")

    lrg2.wait_for_object_v(lrg2.autotest_icon_static_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_static_card(), "green", 6)

    static_value = lrg2.autotest_text_static_address().text
    assert str(static_value) == "192.168.10.63"

    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "green", 6)

    lrg2.autotest_text_dns().click()
 
    dns_value_1 = lrg2.autotest_detail_dns_title()[0].text
    assert dns_value_1 == "DNS1"

    lrg2.autotest_text_dns().click()
 
    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 6)

    gate_value = lrg2.autotest_text_gateway().text
    assert str(gate_value) == "192.168.10.1"

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_cloud_card(), "green", 15)

    cloud_value = lrg2.autotest_text_cloud().text
    assert str(cloud_value) == "Link-Live.com"
