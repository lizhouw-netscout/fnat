from testconfig import config
from fnat_dev import FnatDevice

class FnatApp:
    def __init__(self):
        self.d = FnatDevice(config["__dev_serial"])

    def launch(self):
        am_start_cmd = "am start -n " + self.def_package + "/" + self.def_activity;
        self.d.run_adb_cmd(am_start_cmd)

    def launch_from_home(self, list_of_icons):
        self.d.launch_from_home(list_of_icons)

    def term(self):
        pass

    def screenshot(self, png_file):
        self.d.screenshot(png_file)

    def run_adb_cmd(self, adb_cmd):
        self.d.run_adb_cmd(adb_cmd)

    def wait_for_object_v(self, obj_selector, timeout, by_force = False):
        self.d.wait_for_object_v(obj_selector, timeout, by_force)

    def wait_for_object_x(self, obj_selector, timeout, by_force = False):
        self.d.wait_for_object_x(obj_selector, timeout, by_force)

    def wait_for_object_description(self, obj_selector, expected_value, timeout, by_force = False):
        self.d.wait_for_object_description(obj_selector, expected_value, timeout, by_force)
