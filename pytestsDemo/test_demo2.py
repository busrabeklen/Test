import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi" , "Test Failed because  strings do not match"


def test_SecondCreditCard(): #test case name is SecondCreditCard
    a = 4
    b = 6
    assert a+2  == 6 , "Addition does not match "
