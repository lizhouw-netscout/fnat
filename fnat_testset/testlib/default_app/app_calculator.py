from fnat_app import FnatApp
from fnat_dev import FnatDevice
from testconfig import config

class app_calculator(FnatApp):
    def __init__(self):
        self.def_package = "com.android.calculator2"
        self.def_activity = ".Calculator"
        FnatApp.__init__(self)

    def btn_0(self):
        return self.d(resourceId="com.android.calculator2:id/digit_0")

    def btn_1(self):
        return self.d(resourceId="com.android.calculator2:id/digit_1")

    def btn_2(self):
        return self.d(resourceId="com.android.calculator2:id/digit_2")

    def btn_3(self):
        return self.d(resourceId="com.android.calculator2:id/digit_3")

    def btn_4(self):
        return self.d(resourceId="com.android.calculator2:id/digit_4")

    def btn_5(self):
        return self.d(resourceId="com.android.calculator2:id/digit_5")

    def btn_6(self):
        return self.d(resourceId="com.android.calculator2:id/digit_6")

    def btn_7(self):
        return self.d(resourceId="com.android.calculator2:id/digit_7")

    def btn_8(self):
        return self.d(resourceId="com.android.calculator2:id/digit_8")

    def btn_9(self):
        return self.d(resourceId="com.android.calculator2:id/digit_9")

    def btn_point(self):
        return self.d(resourceId="com.android.calculator2:id/dec_point")

    def btn_add(self):
        return self.d(resourceId="com.android.calculator2:id/op_add")

    def btn_sub(self):
        return self.d(resourceId="com.android.calculator2:id/op_sub")

    def btn_mul(self):
        return self.d(resourceId="com.android.calculator2:id/op_mul")

    def btn_div(self):
        return self.d(resourceId="com.android.calculator2:id/op_div")

    def btn_eq(self):
        return self.d(resourceId="com.android.calculator2:id/eq")

    def btn_del(self):
        return self.d(resourceId="com.android.calculator2:id/del")

    def btn_clr(self):
        return self.d(resourceId="com.android.calculator2:id/clr")
                      
    def edit_formula(self):
        return self.d(resourceId="com.android.calculator2:id/formula")

    def edit_result(self):
        return self.d(resourceId="com.android.calculator2:id/result")

    def control_mapper(self, input_char):
        map_table = { "1" : self.btn_1(),
                      "2" : self.btn_2(),
                      "3" : self.btn_3(),
                      "4" : self.btn_4(),
                      "5" : self.btn_5(),
                      "6" : self.btn_6(),
                      "7" : self.btn_7(),
                      "8" : self.btn_8(),
                      "9" : self.btn_9(),
                      "0" : self.btn_0(),
                      "+" : self.btn_add(),
                      "-" : self.btn_sub(),
                      "*" : self.btn_mul(),
                      "/" : self.btn_div(),
                      "=" : self.btn_eq(),
                      "." : self.btn_point()
                    }
        if map_table.has_key(input_char):
            return map_table[input_char]
        else:
            return None

    def clear(self):
        if self.btn_clr().exists:
            self.btn_clr().click()
        else:
            curr_text = self.edit_formula().text
            for i in range(0, len(curr_text)):
                self.btn_del().click()
        return (0 == len(self.edit_formula().text)) and (0 == len(self.edit_result().text))
        
    def verify(self, formula, exp_result):
        for i in range(0, len(formula)):
            this_ctrl = self.control_mapper(formula[i:i + 1])
            if None != this_ctrl:
                this_ctrl.click()
        if(0 != cmp(self.edit_result().text, exp_result)):
            return False

        self.btn_eq().click()
        return (0 == cmp(self.edit_formula().text, exp_result)) and self.btn_clr().exists
