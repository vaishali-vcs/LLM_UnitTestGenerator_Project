# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import function29 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xfc\x86\x15Z\n\x85\xd2\x8eSr\x8fh\xf7\x9dj\xcb\xf8"
    module_0.find_digits_chars_symbols(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.find_digits_chars_symbols(list_0)
    list_1 = [list_0, list_0]
    module_0.find_digits_chars_symbols(list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_digits_chars_symbols(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '\nF"b<}9:\x0cA.G%I^'
    var_0 = module_0.find_digits_chars_symbols(str_0)
    int_0 = -1877
    module_0.find_digits_chars_symbols(int_0)
