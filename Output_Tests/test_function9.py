# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function9 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "5bU"
    var_0 = module_0.pig_latin(str_0)
    assert var_0 == "u5bay"
    var_1 = module_0.pig_latin(var_0)
    assert var_1 == "u5bayway"
    var_2 = module_0.pig_latin(str_0)
    assert var_2 == "u5bay"
    var_3 = module_0.pig_latin(str_0)
    assert var_3 == "u5bay"
    var_4 = module_0.pig_latin(var_2)
    assert var_4 == "u5bayway"
    var_5 = module_0.pig_latin(var_1)
    assert var_5 == "u5baywayway"
    var_6 = module_0.pig_latin(var_0)
    assert var_6 == "u5bayway"
    var_7 = module_0.pig_latin(var_0)
    assert var_7 == "u5bayway"
    var_8 = module_0.pig_latin(var_3)
    assert var_8 == "u5bayway"
    var_9 = module_0.pig_latin(var_0)
    assert var_9 == "u5bayway"
    var_10 = module_0.pig_latin(var_5)
    assert var_10 == "u5baywaywayway"
    none_type_0 = None
    module_0.pig_latin(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "ZJs_d9K|!+\nw:Y2{V7}"
    var_0 = module_0.pig_latin(str_0)
    assert var_0 == "zjs_d9k|!+ay w:y2{v7}ay"
    var_1 = module_0.pig_latin(var_0)
    assert var_1 == "ayzjs_d9k|!+ay ayw:y2{v7}ay"
    complex_0 = -1618 - 869.19j
    tuple_0 = (str_0, complex_0)
    module_0.pig_latin(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b".\xbe\xd1\xd0\xca"
    module_0.pig_latin(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2264
    module_0.pig_latin(int_0)
