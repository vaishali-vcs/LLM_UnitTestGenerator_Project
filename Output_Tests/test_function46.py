# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function46 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.checkLeapYear(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_0.checkLeapYear(bool_0)
    module_0.checkLeapYear(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.checkLeapYear(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    var_0 = module_0.checkLeapYear(bool_0)
    int_0 = 1104
    var_1 = module_0.checkLeapYear(int_0)
    var_2 = module_0.checkLeapYear(bool_0)
    bool_1 = True
    var_3 = module_0.checkLeapYear(bool_1)
    var_4 = module_0.checkLeapYear(bool_1)
    list_0 = []
    module_0.checkLeapYear(list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    var_0 = module_0.checkLeapYear(bool_0)
    bool_1 = False
    var_1 = module_0.checkLeapYear(bool_1)
    object_0 = module_1.object()
    int_0 = 1100
    var_2 = module_0.checkLeapYear(int_0)
    module_0.checkLeapYear(var_2)
