import requests


class TestBasicApi:
    #GET api example
    #@staticmethod #you dont have to type self if you use staticmethod
    #def test_basic_get_api():
    #req = requests.request('GET', 'https://httpbin.org/get')
    #print(req.json())

    @staticmethod
    def test_basic_get_api():
        req = requests.get('https://httpbin.org/get')
        print(req.json())
        #both way is same

    @staticmethod
    def test_basic_get_api2():
        req = requests.get('https://reqres.in/api/users?page=2')
        print(req.json())
        assert req.status_code == 200, "API CALL IS FAILED"
        print("Api status code passed")
        total_pages = req.json()['total_pages']
        print(f"Total Pages is {total_pages}")
        user_email = req.json()['data'][0]['email']
        print(f"This is email {user_email}")
        assert total_pages == 2, "PAGE SIZE IS WRONG"
        assert user_email == 'michael.lawson@reqres.in', "Email is wrong"
        print("Response assertion is passed")


    @staticmethod
    def test_basic_post_api2():
        request_json = {
  "id": 0,
  "title": "string",
  "dueDate": "2025-07-18T23:59:52.775Z",
}
        header = {"Content-Type" : "application/json"} #you can pass multiple headers

        response = requests.request('POST',
                                    'https://fakerestapi.azurewebsites.net/api/v1/Activities',
                                    json = request_json,
                                    headers = header) #anybody can understand this constructure
        print(response.json())
        assert response.status_code == 200




#TestBasicApi.test_basic_get_api()
#TestBasicApi.test_basic_get_api2()
