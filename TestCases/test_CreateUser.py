import requests
import pytest
import yaml


class TestSet_Users(object):
    """
    Test Set for testing users functionality of https://gorest.co.in
    """
    format = "json"

    url = "https://gorest.co.in/public-api/users"

    def setup_method(self):
        settingsFile = open("Test_Settings.yaml", "r")
        setting = yaml.safe_load(settingsFile)
        self.acc_token = setting["api_key"]

    def __find_string_in_response(self, fullResponse, searchFor):
        check = True
        rawResponse = fullResponse
        if "data" not in rawResponse.text:
            check = False
        else:
            responseJSON = rawResponse.json()
            length_responseJSON = len(responseJSON["data"])
            for i in range(0,length_responseJSON,1):
                check =  searchFor in responseJSON["data"][i]["name"]
                print('The value is ',length_responseJSON,searchFor,i)
                if check == False:
                    return check
        return check

    def test_Create(self):

        payload = {"name": "firstuser3","email": "Firstuser3@testonly.com","gender": "Male","status": "Active"}
        headers = {
                'Authorization': 'Bearer ' + self.acc_token,
                'Content-Type': 'application/json'
              }

        response = requests.post(self.url, headers=headers, json = payload)

        print('Test is executing')

        print(response.text.encode('utf8'))

    # Test-2
    @pytest.mark.parametrize("name", ["firstuser2", "firstuser", "Oscar"])
    def test_get_a_user(self, name):
        payload = {"name": name}
        headers = {
            'Authorization': 'Bearer ' + self.acc_token,
            'Content-Type': 'application/json'
        }

        response = requests.get(self.url, headers=headers, json=payload)

        print('Test is executing')

        print(response.text.encode('utf8'))

        check = self.__find_string_in_response(response, name)
        assert check == True, "GEt API Test failed"
