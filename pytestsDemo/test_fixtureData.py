import pytest

from pytestsDemo.conftest import dataLoad


@pytest.mark.usefixtures("dataLoad") #we declare globally here
class TestExample2:

    def test_editProfile(self,dataLoad): #why we have to add parameter(datalod)
        print(dataLoad[0]) #if you want to data from spesific test then ypu have to pass "dataload"
#also in this case we are returning something that why we have to pass parameter
#INTERVIEW!! what scenario you will be pass fixture name ? if you are returning something you have to pass fixture name as a parameter
        print(dataLoad[2])
