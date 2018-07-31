#!/usr/bin/python

import ConfigParser
from cisco3560 import Cisco3560
from hp2910 import HP2910
from Huawei3328 import Huawei3328
from Huawei5324 import Huawei5324
from juniper2200 import Juniper2200
from hp5406 import HP5406
import os


class Switch:
    def __init__(self):
        print "Function __init__ of class switch is called"
        env_cfg = os.environ['FNAT_TESTSET_ROOT'] + "/config/environ.cfg"
        config = ConfigParser.ConfigParser()
        config.read(env_cfg)

        dev_type = os.environ['FNAT_SWITCH'] 
        print "=============================" + env_cfg + "===============" + dev_type + "****************************"
        str_host = config.get(dev_type, "host")
        str_user = config.get(dev_type, "user")
        str_passwd = config.get(dev_type, "passwd")

        if("cisco3560" == dev_type):
            self.switch_dev = Cisco3560(str_host, str_user, str_passwd)
        elif("hp2910" == dev_type):
            self.switch_dev = HP2910(str_host, str_user, str_passwd)
        elif("Huawei3328" == dev_type):
            self.switch_dev = Huawei3328(str_host, str_user, str_passwd)
        elif("Huawei5324" == dev_type):
            self.switch_dev = Huawei5324(str_host, str_user, str_passwd)
        elif("juniper2200" == dev_type):
            self.switch_dev = Juniper2200(str_host, str_user, str_passwd)
        elif("hp5406" == dev_type):
            self.switch_dev = HP5406(str_host, str_user, str_passwd)
        else:
            assert False

    def set_speed_duplex_value(self,port,speed,duplex):
        print "Function set_speed of class switch is called"
        self.switch_dev.set_speed_duplex_value(port,speed,duplex)
    def set_poe_enable(self,port):
        print('Function Set_poe_enable of class switch is called')
        self.switch_dev.set_poe_enable(port)
    def set_poe_disable(self,port):
        print('Function Set_poe_disable of class switch is called')
        self.switch_dev.set_poe_disable(port)
    def set_lldp_enable(self,port):
        print('Function Set_lldp_enable of class switch is called')
        self.switch_dev.set_lldp_enable(port)
    def set_lldp_disable(self,port):
        print('Function Set_lldp_disable of class switch is called')
        self.switch_dev.set_lldp_disable(port)
    def set_cdp_enable(self,port):
        print('Function Set_cdp_enable of class switch is called')
        self.switch_dev.set_cdp_enable(port)
    def set_lldp_cdp_enable(self,port):
        print('Function Set_lldp_cdp_enable of class switch is called')
        self.switch_dev.set_lldp_cdp_enable(port)
