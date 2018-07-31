#!/usr/bin/env python

#
#  File:      plan_reader.py
#  Project:   FNAT (Pyunit Automation Test for Android)
#
#  This script is used in project FNAT to write/parse test plan.
#

import json
import ConfigParser
import os
import string
import subprocess
import sys
import adb_obj
import time
import gl_var
import fnat_logging
import fnat_callback
# from testrail import *

class plan_reader:
    '''
    This class is to read/process FNAT test plan
    '''
    def __init__(self, plan_url):
        self.plan = plan_url
        self.case_list = []
        
    def read_cases(self):
        '''
        Function read_cases() in class plan_reader:
        In class plan_reader, there is an instance variable called case_list which is used to keep
        the cases that will be executed according to the current test plan.
        
        Each item in case_list is a tuple that contains four fields
        - The first one is the entry of case
        - The second one is the loop the case will be executed for
        - The third one is a dictionary containing the input parameters
        - The forth one is the postfix of data driven cases, and it is left empty if it is not data driven
        '''
    
        # Read testplan and extract cases	
        plan_location = gl_var.testset_root + "/testplan/" + self.plan
        config = ConfigParser.ConfigParser()
        config.read(plan_location)
        all_cases = config.items("cases")

        # Parse all cases
        for case_entry in all_cases:
            left_bracket_pos = case_entry[1].find('(')
            right_bracket_pos = case_entry[1].find(')')
            equal_mark_pos = case_entry[1].rfind('=')

            case_name = case_entry[0].strip()
            case_loop = string.atoi(case_entry[1][equal_mark_pos + 1:].strip(), 10)
            if (right_bracket_pos > left_bracket_pos) and (left_bracket_pos >= 0) and (equal_mark_pos > right_bracket_pos):
                case_params = case_entry[1][left_bracket_pos + 1:right_bracket_pos].strip()
            else:
                case_params = ""

            if (case_loop > 0) and (len(case_name.split(".")) > 2):
                # If case iteration is less than or equal to 0, it means that
                # this case is disabled
                # Besides, there must be at least three items in case name, 
                # for, case file name and case method name
                if len(case_params) > 0:
                    # We have extra parameters in brackets
                    data_file = ""
                    dict_params = {}
                    list_params = case_params.split(",")
                    
                    for i in range(0, len(list_params)):
                        param_items = list_params[i].split("=")
                        param_name = param_items[0].strip()
                        if param_name == "data_file":
                            data_file = param_items[1].strip()
                        else:
                            dict_params[param_name] = param_items[1].strip()
                                
                    if len(data_file) > 0:
                        # It is data driven case
                        file_json = file(gl_var.testset_root + "/config/" + data_file)
                        data_dict = json.load(file_json)["data"]
                        for i in range(0, len(data_dict)):
                            self.case_list.append((case_name, case_loop, dict(dict_params, **data_dict[i]), data_dict[i]["name"]))
                    else:
                        self.case_list.append((case_name, case_loop, dict_params, ""))                    
                else:
                    self.case_list.append((case_name, case_loop, {}, ""))

    def get_exec_time (self):
        return time.strftime("%Y-%m-%d-%H-%M-%S")

    def create_logfolder (self, log_root_folder, str_exec_time):
        log_folder = log_root_folder + "/" + gl_var.dev_serial
        if os.path.exists(log_folder):
            if not os.path.isdir(log_folder):
                assert False
        else:
            os.makedirs(log_folder)

        time.localtime(time.time())
        log_folder += "/Exec-" + str_exec_time
        os.makedirs(log_folder)
        return log_folder
        
    def run_case(self, log_root_folder, local_log_folder):
        log_case = None
        p_logging = None
        try:
            str_exec_time = self.get_exec_time()
            log_folder = self.create_logfolder(log_root_folder, str_exec_time)
            log_file = log_folder + "/fnat_case.log"
            log_case = open(log_file, "w+")

            p_logging = fnat_logging.fnat_logging(gl_var.cfg_fname, log_folder)

            if True == p_logging.if_logging_in_one():
                p_logging.start_logging()
                
            fnat_callback.action_before_all_cases(gl_var.dev_serial)
            for case_entry in self.case_list:
                nose_input_params = [ "nosetests", "-s" ]

                for param_name in case_entry[2]:
                    case_params = "--tc=" + param_name + ":\'" + case_entry[2][param_name] + "\'"
                    nose_input_params.append(case_params)

                case_params = "--tc=__dev_serial:" + gl_var.dev_serial
                nose_input_params.append(case_params)

                case_params = "--tc=__log_dir:" + local_log_folder
                nose_input_params.append(case_params)
                
                case_params = "--tc=__testset_root:" + gl_var.testset_root
                nose_input_params.append(case_params)
                
                entry_items = case_entry[0].split(".")
                case_cmdline = "testcase/"                
                module_entry = gl_var.testset_root + "/testcase"

                for i in range(0, len(entry_items) - 2):
                    case_cmdline += entry_items[i] + "/"
                    module_entry += "/" + entry_items[i]
                    
                case_cmdline += entry_items[-2] + ".py:"
                case_cmdline += entry_items[-1]
                nose_input_params.append(case_cmdline)

                old_syspath = sys.path
                sys.path.append(module_entry)
                this_module = __import__(entry_items[-2])
                this_object = getattr(this_module, entry_items[-1])
                doc_section = this_object.__doc__

                section_caseid = ""
                if None != doc_section:
                    left_tag_pos = doc_section.find("<case_id>")
                    if left_tag_pos >= 0:
                        right_tag_pos = doc_section.find("</case_id>")
                        section_caseid = doc_section[left_tag_pos + 9:right_tag_pos]

                # section_steps = ""
                # if None != doc_section:
                #     left_step_pos = doc_section.find("<steps>")
                #     if left_step_pos >= 0:
                #         right_step_pos = doc_section.find("</steps>")
                #         section_steps = doc_section[left_step_pos + 7:right_step_pos]

                # section_expresult = ""
                # if None != doc_section:
                #     left_expresult_pos = doc_section.find("<exp_result>")
                #     if left_expresult_pos >= 0:
                #         right_expresult_pos = doc_section.find("</exp_result>")
                #         section_expresult = doc_section[left_expresult_pos + 12:right_expresult_pos]                
                    
                sys.path = old_syspath
                
                for i in range(0, case_entry[1]):
                    if len(case_entry[3]) > 0:
                        display_name = case_entry[0] + "_" + case_entry[3]
                    else:
                        display_name = case_entry[0]
                        
                    if 1 == case_entry[1]:
                        case_folder = log_folder + "/" + display_name
                    else:
                        case_folder = "%s/%s_%d" % (log_folder, display_name, i)
                    os.makedirs(case_folder)

                    p = None
                    r = -1
                    # client = APIClient()
                    try:
                        log_case.write("*" * 80 + "\n")
                        log_case.write(" " * 8 + "CASE : " + display_name + "\n\n\n")

                        if False == p_logging.if_logging_in_one():
                            if 1 == case_entry[1]:
                                p_logging.start_logging(display_name)
                            else:
                                p_logging.start_logging(display_name + "_" + str(i))

                        fnat_callback.action_before_case(gl_var.dev_serial, display_name)
                
                        p = subprocess.Popen(nose_input_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=None)
                        r = p.wait()

                        if 0 == r:
                        #    client.add_result_for_case(gl_var.run_id, section_caseid, "1")
                            log_case.write(" " * 8 + "Verdict : PASS\n")
                        else:
                        #    client.add_result_for_case(gl_var.run_id, section_caseid, "5")
                            log_case.write(" " * 8 + "Verdict : FAIL\n")                            
                    except Exception as e:
                        # client.add_result_for_case(gl_var.run_id, section_caseid, "5")
                        log_case.write(" " * 8 + "Verdict : FAIL (" + e.message + ")\n\n\n")
                        if e.message == "Device not attached.":
                            time.sleep(10)
                    finally:
                        if None != p:
                            log_buffer = p.stdout.readlines()
                            for log_line in log_buffer:
                                log_case.write(log_line)
                                sys.stdout.write(log_line)
                            log_case.flush()

                        fnat_callback.action_after_case(gl_var.dev_serial, display_name)
                        if gl_var.dev_serial != "fake":
                            this_cmd = "adb -s " + gl_var.dev_serial + " shell /system/bin/screencap -p | sed 's/\r$//' > " + case_folder + "/Case_FinalScreen.png"
                            os.system(this_cmd)
                        p_logging.dmesg_poll()

                        if False == p_logging.if_logging_in_one():
                            p_logging.stop_logging()
        finally:
            fnat_callback.action_after_all_cases(gl_var.dev_serial)
            if None != log_case:
                log_case.close()
            if (True == p_logging.if_logging_in_one()) and (None != p_logging):
                p_logging.stop_logging()
