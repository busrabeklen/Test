#any pytest file should start with "test"
#pytest method names should start with test
#any code should be wrapped in method only
#method name should have simple(sense)
#-k stands for method name execution, -s logs in output, -v more info
import pytest


#you can run as py.test (in test runner(terminal? )
#py.test -v (gives more information about test)
#py.test -v -s (it will print "hello" and gives results
#if you want to run only test_demo2 file then open terminal , cd pytestsDemo, py.test test_demo2 -v -s
#py.test -k CreditCard -v -s :it will only run method include CreditCard
#if I want to run only smoke test (py.test -m smoke -v -s)
#if I want to skip one (@pytest.mark.skip)
#@pytest.mark.xfail :  it will still run but don't show me report
#those are called annotation  xfail , skip ,smoke
#fixtures are used for setup and teardown methods for testcases
# conftest.py file to generalize fixture and make it avaliable to all test cases



@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram(setup):
    print("hello")

@pytest.mark.xfail
def test_secondGreetCreditCArd():
    print("Good morning!!")


def test_crossBrowser(crossBrowser):
    print(crossBrowser) #this will be run 2 times because we pass(chrome,firefox)


#if you want to run all test cases on the comman line
#pytest --html=report.html











