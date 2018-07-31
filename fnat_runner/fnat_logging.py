#!/usr/bin/env python

import ConfigParser
import os
import subprocess
import gl_var

class fnat_logging:

    def __init__(self, cfg_file, fnat_logfolder=None):
        config = ConfigParser.ConfigParser()
        config.read(cfg_file)
        if None != fnat_logfolder:
            self.log_folder = fnat_logfolder
        if 0 == cmp(gl_var.dev_serial.upper(), "FAKE"):
            self.log_in_one = "off"
            self.logcat_status = "off"
            self.dmesg_status = "off"
            self.serial_status = "off"
        else:
            self.log_in_one = config.get("logging", "log_as_one")
            self.logcat_status = config.get("logging", "logcat")
            self.dmesg_status = config.get("logging", "dmesg")
            self.serial_status = config.get("logging", "serial")
            self.serial_port = config.get("serial", "port")
            self.serial_br = config.get("serial", "baudrate")
            self.logcat_proc = None
            self.serial_proc = None
            self.dmesg_handle = None

    def if_logging_in_one(self):
        if 0 == cmp(self.log_in_one.upper(), "ON"):
            return True
        else:
            return False
        
    def start_logging(self, case_name = ""):
        self.logcat_enable(case_name)
        self.serial_enable(case_name)
        self.dmesg_start(case_name)

    def stop_logging(self):
        self.logcat_disable()
        self.serial_disable()
        self.dmesg_stop()

    def logcat_enable(self, case_name):
        if 0 == cmp(self.log_in_one.upper(), "ON"):
            log_file = self.log_folder + "/fnat_logcat.log"
        else:
            log_file = self.log_folder + "/fnat_logcat_" + case_name + ".log"
            
        if 0 == cmp(self.logcat_status.upper(), "ON"):
            self.logcat_handle = open(log_file, "wt")
            str_cmd  = [ "adb", "logcat" ]
            self.logcat_proc = subprocess.Popen(str_cmd, stdout = self.logcat_handle)

    def logcat_disable(self):
        if (0 == cmp(self.logcat_status.upper(), "ON")) and (None != self.logcat_proc):
            self.logcat_proc.terminate()
            self.logcat_handle.close()
    
    def serial_enable(self, case_name):
        if 0 == cmp(self.log_in_one.upper(), "ON"):
            log_file = self.log_folder + "/fnat_serial.log"
        else:
            log_file = self.log_folder + "/fnat_serial_" + case_name + ".log"

        if 0 == cmp(self.serial_status.upper(), "ON"): 
            str_cmd  = [ "/var/fnat/fnat_rdser" ]
            str_cmd += [ self.serial_port ]
            str_cmd += [ log_file ]
            self.serial_proc = subprocess.Popen(str_cmd)

    def serial_disable(self):
        if (0 == cmp(self.serial_status.upper(), "ON")) and (None != self.serial_proc): 
            self.serial_proc.terminate()

    def dmesg_start(self, case_name):
        if 0 == cmp(self.log_in_one.upper(), "ON"):
            log_file = self.log_folder + "/fnat_dmesg.log"
        else:
            log_file = self.log_folder + "/fnat_dmesg_" + case_name + ".log"

        if 0 == cmp(self.dmesg_status.upper(), "ON"):
            self.dmesg_handle = open(log_file, "wt")

    def dmesg_poll(self):
        if (0 == cmp(self.dmesg_status.upper(), "ON")) and (None != self.dmesg_handle) and (False == self.dmesg_handle.closed):
            str_cmd = [ "adb", "shell", "dmesg", "-c" ]
            subprocess.Popen(str_cmd, stdout = self.dmesg_handle)

    def dmesg_stop(self):
        if (0 == cmp(self.dmesg_status.upper(), "ON")) and (None != self.dmesg_handle):
            self.dmesg_handle.close()
