# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function7 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.cubesum(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.cubesum(bool_0)
    assert var_0 == 0
    bool_1 = True
    module_0.cubesum(bool_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 555.4 - 1347j
    module_0.cubesum(complex_0)
