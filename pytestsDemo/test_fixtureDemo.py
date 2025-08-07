import pytest

@pytest.mark.usefixtures("setup") #it will automatically apply all class
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo method")

