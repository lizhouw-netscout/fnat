from uiautomator import Device
from testconfig import config
from find_obj import find_obj
import os
import time

class FnatDevice(Device):
    def __init__(self, serial_no):
        Device.__init__(self, serial_no)
        self.serial = serial_no
        if 0 != cmp(self.serial.upper(), "FAKE"):
            self.d = Device(self.serial)

    def wakeup(self):
        if 0 != cmp(self.serial.upper(), "FAKE"):
            self.d.wakeup()
        else:
            pass

    def launch_from_home(self, list_of_icons):
        self.d.press.home()
        app_icon = self.d(packageName="com.android.launcher", description="Apps")
        if 0 <= self.wait_for_object_v(app_icon, 3):
            app_icon.click()

            widget_tab = self.d(packageName="com.android.launcher", description="Widgets")
            if 0 > self.wait_for_object_v(widget_tab, 3):
                return False

            size_list = len(list_of_icons)
            center_point = (-1, -1)
            for i in range(0, size_list - 1):
                self.screenshot("pata_fullscreen.png")
                center_point = find_obj(config["__log_dir"] + "/pata_fullscreen.png", config["__testset_root"] + "/icons/" + list_of_icons[i])
                if center_point[0] < 0 or center_point[1] < 0:
                    return False
                else:
                    self.d.click(center_point[0], center_point[1])
            return True
        else:
            return False

    def wait_for_object_v(self, obj_selector, timeout, by_force = False):
        while(timeout >= 0):
            if obj_selector.exists:
                return timeout

            timeout = timeout - 1
            time.sleep(1)
        if True == by_force:
            assert False
        else:
            return -1

    def wait_for_object_x(self, obj_selector, timeout, by_force = False):
        while(timeout >= 0):
            if not obj_selector.exists:
                return timeout

            timeout = timeout - 1
            time.sleep(1)
        if True == by_force:
            assert False
        else:
            return -1

    def wait_for_object_description(self, obj_selector, expected_value, timeout, by_force = False):
        while(timeout >= 0):
            if obj_selector.exists:
                obj_description = obj_selector.description
                if str(obj_description) == expected_value:
                    return timeout

            timeout = timeout - 1
            time.sleep(1)
        if True == by_force:
            assert False
        else:
            return -1

    def unlock(self):
        if 0 != cmp(self.serial.upper(), "FAKE"):
            icon_lock = self.d(resourceId="com.android.systemui:id/lock_icon")
            if icon_lock.exists:
                icon_lock.drag.to(icon_lock.bounds["left"], 0)
                self.wait_for_object_x(icon_lock, 5, True)
        else:
            pass

    def screenshot(self, png_file):
        this_cmd = "adb -s " + self.serial + " shell /system/bin/screencap -p | sed 's/\r$//' > " + config["__log_dir"] + "/" + png_file
        os.system(this_cmd)

    def run_adb_cmd(self, adb_cmd):
        this_cmd = "adb -s " + self.serial + " shell " + adb_cmd
        return os.popen(this_cmd).readlines()

