#!/usr/bin/env python

#
#  File:      fnat_callback.py
#  Project:   FNAT (Pyunit Automation Test for Android)
#
#  This script is used in project FNAT to implement some predefined
#  action in test plan.
#

from fnat_dev import FnatDevice

def action_before_all_cases(serial_no):
    print "Function: action_before_all_cases() is called"

def action_before_case(serial_no,  case_id):
    print "Function: action_before_case(" + case_id + ") is called"
    thisDev = FnatDevice(serial_no)
    thisDev.wakeup()
    thisDev.unlock()

def action_after_case(serial_no,  case_id):
    print "Function: action_after_case(" + case_id + ") is called"

def action_after_all_cases(serial_no):
    print "Function: action_after_all_cases() is called"

