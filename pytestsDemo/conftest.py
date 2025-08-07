import pytest

@pytest.fixture(scope="class") #if you dont mention anything it is method level but now class level
def setup():
    print("I will be executing first") #pre request
    yield
    print("I will be executing last") #post request



@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Busra","Beklen","rahulshettyacademy.com"] #your accualt data here

# @pytest.fixture(params=["chrome", "firefox"])
# def crossBrowser(request):
#     return request.param

