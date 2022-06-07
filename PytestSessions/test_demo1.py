import pytest

@pytest.mark.login
def test_m1():
    a = 3
    b = 4
    assert a + 2 == b, "test failed"
    assert a == b, "test failed as a is not eq to b"


def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert True


def test_m4():
    assert False


def test_m5():
    assert 100 == 101, "not eqaul"

@pytest.mark.login
def test_m6():
    assert "dhyay" == "DHYAY"


def test_login_fb():
    assert "admin" == "admin"