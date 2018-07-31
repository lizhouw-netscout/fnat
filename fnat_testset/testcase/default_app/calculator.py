from default_app import app_calculator
from util import cfg

def setUp():
    pass

def tearDown():
    pass

def test_calculator():
    '''
    This case is used to verify the primary functionality of calculator
    '''
    calculator = app_calculator.app_calculator()
    calculator.launch()

    print("Save a screen-shot at calculator_launch.png")
    calculator.screenshot("calculator_launch.png")

    calculator.clear()
    assert calculator.verify("1+2", "3")

    calculator.clear()
    assert calculator.verify("1*2", "2")

def test_calculator_loop ():
    '''
    This case is used to verify the primary functionality of calculator
    for loops
    '''
    calculator = app_calculator.app_calculator()
    calculator.launch()

    print("Save a screen-shot at calculator_launch.png")
    calculator.screenshot("calculator_launch.png")

    calculator.clear()
    assert calculator.verify("2+3", "5")

    calculator.clear()
    assert calculator.verify("2*3", "6")

def test_calculator_param ():
    '''
    This case is used to verify the primary functionality of calculator
    with input parameters
    '''
    calculator = app_calculator.app_calculator()
    calculator.launch()

    print("Save a screen-shot at calculator_launch.png")
    calculator.screenshot("calculator_launch.png")

    calculator.clear()
    assert calculator.verify(cfg("formula"), cfg("exp_result"))

def test_calculator_data ():
    '''
    This case is used to verify the primary functionality of calculator
    for data-driven
    '''
    calculator = app_calculator.app_calculator()
    calculator.launch()

    print("Save a screen-shot at calculator_launch.png")
    calculator.screenshot("calculator_launch.png")

    calculator.clear()
    assert calculator.verify(cfg("formula"), cfg("exp_result"))


