from fnat_app import FnatApp
from fnat_dev import FnatDevice
from testconfig import config
import time

class app_lrg2(FnatApp):
    def __init__(self):
        self.def_package = "com.flukenetworks.yilian.prototype"
        self.def_activity = ".activity.MainActivity"
        FnatApp.__init__(self)

    def btn_refresh(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/refresh')

    def btn_menu(self):
        return self.d(description='Open navigation drawer')

    def menu_setting_item_profile(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/profile')

    def menu_setting_item_ip_config(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/spinner_ip_config')

    def menu_setting_item_edit_ip_address(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/ip_address_edit')

    def menu_setting_item_edit_subnet_mask(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/subnet_mask_edit')

    def menu_setting_item_edit_gateway(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_edit')

    def menu_setting_item_edit_dns1(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/dns1_edit')

    def menu_setting_item_edit_dns2(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/dns2_edit')

    def menu_setting_item_add_target(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/add_target')

    def menu_setting_item_target_address(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/target_address')

    def menu_setting_item_target_ping(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/test_type_switch')

    def menu_setting_item_default_settings(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/factory_view')

    def autotest_icon_static_card(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/static_image')

    def autotest_text_static_address(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/static_text')

    def autotest_icon_dhcp_card(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/dhcp_image')

    def autotest_icon_dns_card(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/dns_image')

    def autotest_text_dns(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/dns_text')

    def autotest_detail_dns_title(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/dns')

    def autotest_detail_dns_pingtime(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/dns_ping_time')

    def autotest_icon_gateway_card(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_image')

    def autotest_text_gateway(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_text')

    def autotest_text_gateway_pingtime(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/gateway_ping_time')

    def autotest_icon_cloud_card(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_image')

    def autotest_text_cloud(self):
        return self.d(resourceId='com.flukenetworks.yilian.prototype:id/cloud_text')

    def launch_from_icon(self):
        if not self.btn_refresh().exists:
            self.d(description='Apps').click()
            self.wait_for_object_v(self.d(text='LinkRunner G2'), 5, True)
            self.d(text='LinkRunner G2').click()
            self.wait_for_object_v(self.btn_refresh(), 5, True)

    # functions for menu "setting"
    def to_menu_setting(self):
        self.btn_menu().click()
        self.wait_for_object_v(self.d(resourceId='com.flukenetworks.yilian.prototype:id/set_text'), 3, True)
        time.sleep(0.5)
        self.d(resourceId='com.flukenetworks.yilian.prototype:id/set_text').click()
        self.wait_for_object_v(self.d(resourceId='com.flukenetworks.yilian.prototype:id/edit_profile_view'), 3, True)
        time.sleep(0.5)

    def quit_menu_setting(self):
        self.d.press.back()
        self.wait_for_object_v(self.d(resourceId='com.flukenetworks.yilian.prototype:id/set_text'), 1, True)
        time.sleep(0.5)
        self.d.press.back()
        self.wait_for_object_x(self.d(resourceId='com.flukenetworks.yilian.prototype:id/set_text'), 1, True)
        time.sleep(0.5)

    def menu_setting_scroll_down(self):
        self.d.drag(6, 350, 6, 100)

    def menu_setting_scroll_up(self):
        self.d.drag(6, 100, 6, 350)

    def navigate_menu_setting(self, object_selector, direction):
        if not object_selector.exists:
            while(True):
                if direction > 0:
                    self.menu_setting_scroll_down()
                else:
                    self.menu_setting_scroll_up()

                if object_selector.exists:
                    return True
                else:
                    if (direction > 0) and (self.menu_setting_item_default_settings().exists):
                        assert False

                    if (direction < 0) and (self.menu_setting_item_profile().exists):
                        assert False

    def menu_setting_edit_input(self, edit_selector, content):
        edit_selector.click()
        self.wait_for_object_v(self.d(resourceId='com.flukenetworks.yilian.prototype:id/edit'), 3, True)
        self.wait_for_object_v(self.d(resourceId='android:id/button1'), 1, True)
        self.d(resourceId='com.flukenetworks.yilian.prototype:id/edit').set_text(content)
        self.d(resourceId='android:id/button1').click()
        self.wait_for_object_x(self.d(resourceId='com.flukenetworks.yilian.prototype:id/edit'), 1, True)
        if len(content) == 0:
            assert edit_selector.text is None
        else:
            assert edit_selector.text == content

    def set_static_address(self, ip_address, subnet_mask, gateway, dns1, dns2, stay_menu = False):
        self.to_menu_setting()

        self.navigate_menu_setting(self.menu_setting_item_ip_config(), 1)
        self.menu_setting_item_ip_config().click()
        time.sleep(0.5)
        self.d(text='Static').click()

        self.navigate_menu_setting(self.menu_setting_item_edit_ip_address(), 1)
        self.menu_setting_edit_input(self.menu_setting_item_edit_ip_address(), ip_address)

        self.navigate_menu_setting(self.menu_setting_item_edit_subnet_mask(), 1)
        self.menu_setting_edit_input(self.menu_setting_item_edit_subnet_mask(), subnet_mask)

        self.navigate_menu_setting(self.menu_setting_item_edit_gateway(), 1);
        self.menu_setting_edit_input(self.menu_setting_item_edit_gateway(), gateway)

        self.navigate_menu_setting(self.menu_setting_item_edit_dns1(), 1)
        self.menu_setting_edit_input(self.menu_setting_item_edit_dns1(), dns1)

        self.navigate_menu_setting(self.menu_setting_item_edit_dns2(), 1)
        self.menu_setting_edit_input(self.menu_setting_item_edit_dns2(), dns2)

        if True != stay_menu:
            self.quit_menu_setting()

    def set_dhcp(self, stay_menu = False):
        self.to_menu_setting()

        self.navigate_menu_setting(self.menu_setting_item_ip_config(), 1)
        self.menu_setting_item_ip_config().click()
        time.sleep(0.5)
        self.d(text='DHCP').click()

        if True != stay_menu:
            self.quit_menu_setting()

    def add_target(self, is_scroll_down, target_address, is_ping):
        if True == is_scroll_down:
            self.navigate_menu_setting(self.menu_setting_item_add_target(), 1)
        else:
            self.navigate_menu_setting(self.menu_setting_item_add_target(), 0)
        self.menu_setting_item_add_target().click
        self.wait_for_object_v(self.menu_setting_item_target_address(), 1, True)

        self.menu_setting_edit_input(self.menu_setting_item_target_address(), target_address)

        if True == is_ping:
            self.menu_setting_item_target_ping().click
