# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function26 as module_0


def test_case_0():
    bytes_0 = b"\x7f\xc2\xd5"
    list_0 = [bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, list_0, bytes_0]
    var_0 = module_0.printOddIndexNumbers(list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.printOddIndexNumbers(bool_0)
