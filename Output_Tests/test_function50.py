# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function50 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xff\xf9\x03\x04\xe4\x8b\xd8\xfc\x9f`5\x96mK\x15\xf8F"
    module_0.checkIsoGram(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa6\x8aY\xab#\xaf\xc6\x02\xe5+"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.checkIsoGram(list_0)
    assert var_0 is True
    int_0 = -2732
    module_0.checkIsoGram(int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "#0UvY-#[p/av@7*"
    var_0 = module_0.checkIsoGram(str_0)
    assert var_0 is False
    none_type_0 = None
    module_0.checkIsoGram(none_type_0)
