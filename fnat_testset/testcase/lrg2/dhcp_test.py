from fnat_dev import FnatDevice
from lrg2_app import app_lrg2
import time

def setUp():
    print('These are DHCP_FUNCTION_TEST testset')

def tearDown():
    print('These are DHCP_FUNCTION_TEST testset')

def testmethod_1():
    # Prerequisite:
    #     Run under VLAN 100 networking.

    print "Method testmethod_1 in class DHCP_FUNCTION_TEST suite"
    print "Method Using DHCP to get IP address in DHCP_FUNCTION_TEST suite"

    lrg2 = app_lrg2.app_lrg2()
    lrg2.launch_from_icon()

    lrg2.set_dhcp()
   
    lrg2.wait_for_object_description(lrg2.autotest_icon_dhcp_card(), "green", 40)
    
    lrg2.wait_for_object_v(lrg2.autotest_icon_dns_card(), 35, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_dns_card(), "green", 6) 
       
    dns_value = lrg2.autotest_text_dns().text
    assert dns_value.rstrip() == '192.168.10.1   10.203.1.19   10.203.1.18'

    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 3) 

    lrg2.wait_for_object_v(lrg2.autotest_text_cloud(), 15, True)
    lrg2.wait_for_object_description(lrg2.autotest_icon_gateway_card(), "green", 15)
        
