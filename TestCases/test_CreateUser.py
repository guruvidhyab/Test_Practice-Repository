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
        print(self.acc_token)

    def __find_string_in_response(self, fullResponse, searchFor):
        check = False
        rawResponse = fullResponse
        if "data" not in rawResponse.text:
            return check
        else:
            responseJSON = rawResponse.json()
            length_responseJSON = len(responseJSON["data"])
            if length_responseJSON == 0:
                return check
            else:
                for i in range(0,length_responseJSON,1):
                    check =  searchFor in responseJSON["data"][i]["email"]
                    print('The value is ',length_responseJSON,searchFor,i)
                    if check == False:
                        print("i am inside the if email does not match with the name")
                        return check
            return check

    def test_Create(self):

        payload = {"name": "forcheck","email": "forcheck@testonly.com","gender": "Male","status": "Active"}
        headers = {
                'Authorization': 'Bearer ' + self.acc_token,
                'Content-Type': 'application/json'
              }

        response = requests.post(self.url, headers=headers, json = payload)

        print('Test is executing')
        print(response.status_code)


        print(response.text.encode('utf8'))

    # Test-2
    @pytest.mark.parametrize("name", ["zzfirstuser3", "forcheck", "revathi"])
    def test_get_a_user(self, name):
        payload = {"name": name}
        headers = {
            'Authorization': 'Bearer ' + self.acc_token,
            'Content-Type': 'application/json'
        }
        print(headers, self.url)

        response = requests.get(self.url, headers=headers, json=payload)

        print('Test is executing')

        print(response.text.encode('utf8'))

        print(name)

        check = self.__find_string_in_response(response, name)

        assert check == True
