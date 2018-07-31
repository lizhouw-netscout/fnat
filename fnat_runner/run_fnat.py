#!/usr/bin/env python
#
#  File:      run_fnat.py
#  Project:   FNAT (Pyunit Automation Test for Android)
#
#  This script is the main entry of project FNAT.
#

import os
import sys
import getopt
import subprocess

def Usage():
    print("run_fnat.py")
    print("  -r, --root: identify root of test set url")
    print("  -p, --plan: identify url of test plan")
    print("  -s, --serial: identify the serial no of device which we want to test")
    print "  -w, --switch: identify the switch we are using, the possible value is in (cisco, hp, huawei)"
    print("  -c, --config: identify the config file we want to use")
    print("  -h, --help: print help information")

if __name__ == "__main__":
    if 0 != os.geteuid():
        print("This script can be executed with root priviledge only")
        exit(1)
        
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hp:r:s:c:w:', ['help', 'plan=',
            'root=', 'serial=', 'config=', 'switch='])
    except getopt.GetoptError, err:
        print(str(err))
        Usage()
        exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            Usage()
            exit(0)
        elif o in ('-r', '--root'):
            curr_dir = os.getcwd()
            os.chdir(a)
            testset_root = os.getcwd()
            os.chdir(curr_dir)
        elif o in ('-p', '--plan', '-s', '--serial', '-c', '--config', '-w', '--switch'):
            pass
        else:
            print('unknown option')
            exit(2)

    lib_path = testset_root + "/testlib:" + sys.path[0]
    case_path = testset_root + "/testcase"
    if os.environ.has_key('PYTHONPATH'):
        os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ":" + lib_path 
    else:
        os.environ['PYTHONPATH'] = lib_path
    os.environ["PYTHONPATH"] += ":" + case_path

    run_test = sys.path[0] + "/run_test.py"
    test_cmd = [ run_test ] + sys.argv[1:]
    p = subprocess.Popen(test_cmd, env=None)
    p.wait()
