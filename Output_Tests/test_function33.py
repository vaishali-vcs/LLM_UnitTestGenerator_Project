# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function33 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    set_0 = {bool_0}
    var_0 = module_0.turnItemtoSquare(set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.turnItemtoSquare(object_0)
