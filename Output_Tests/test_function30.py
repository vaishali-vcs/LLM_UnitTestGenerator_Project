# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function30 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xcc\xfc\xa5\xfb8\x03^xG\xbb"
    module_0.createMixString(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\x0c)Y>(!9p]H\n"
    var_0 = module_0.createMixString(str_0, str_0)
    none_type_0 = None
    module_0.createMixString(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    module_0.createMixString(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.createMixString(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\x0c)Y>(!9p]H\n"
    var_0 = module_0.createMixString(str_0, str_0)
    list_0 = [str_0, str_0]
    var_1 = module_0.createMixString(str_0, list_0)
    var_2 = module_0.createMixString(list_0, str_0)
    module_0.createMixString(str_0, var_1)
