#!/usr/bin/env python

import ConfigParser
import os
import sys
import getopt
import plan_reader
import gl_var
import subprocess
import time
import adb_obj

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'p:r:s:c:w:', ['plan=', 'root=', 'serial=', 'config=', 'switch='])
    except getopt.GetoptError, err:
        print(str(err))
        exit(1)

    gl_var.cfg_fname = "environ.cfg"
    for o, a in opts:
        if o in ('-r', '--root'):
            os.chdir(a)
            gl_var.testset_root = os.getcwd()
            os.environ['FNAT_TESTSET_ROOT'] = gl_var.testset_root;
        elif o in ('-p', '--plan'):
            plan_testset = a
        elif o in ('-s', '--serial'):
            gl_var.dev_serial = a
        elif o in ('-c', '--config'):
            gl_var.cfg_fname = a
        elif o in ('-w', '--switch'):
            os.environ['FNAT_SWITCH'] = a
        else:
            print('unknown option')
            exit(2)

    gl_var.cfg_fname = gl_var.testset_root + "/config/" + gl_var.cfg_fname

    config = ConfigParser.ConfigParser()
    config.read(gl_var.cfg_fname)
    gl_var.run_id = config.get("testrail", "run_id")

    print("[FNAT] root = " + gl_var.testset_root + ", plan = " + plan_testset + ", run_id = " + gl_var.run_id)

    gl_var.adb_mgr = adb_obj.adb_obj()
    if 0 == len(gl_var.dev_serial) or gl_var.dev_serial == "fake":
        gl_var.adb_mgr.restart_adb_server()
    else:
        gl_var.adb_mgr.start_adb_server()

    if len(gl_var.dev_serial) == 0:
        gl_var.adb_mgr.get_adb_serial()

    str_now_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    local_log = "/var/fnat/fnat_log/Exec_" + gl_var.dev_serial + "_" + str_now_time
    print("Log files and Screen shots will be saved at " + local_log)
    log_folder = local_log

    if not os.path.exists(local_log):
        os.makedirs(local_log)

    p_reader = plan_reader.plan_reader(plan_testset)
    p_reader.read_cases()
    p_reader.run_case(log_folder, local_log)
