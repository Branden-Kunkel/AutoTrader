# library to access API Data from 'polygon.io'

import requests
import json
import exceptions.exceptions as AuthEx
import parameters.data_access_params as params

api_key = params.static_parameters["api_key"]

class ApiDataPort():
    """class serves as an engine to access API data"""

    def generate_request_url(self, url=str, paramaters=dict):

        parameters_list = []
        endpoint_string = ""

        for key, value in paramaters.items():
            if paramaters[key] == None:
                pass
            else:
                parameters_list.append(key + "=" + value)

        endpoint_string = "&".join(parameters_list)

        request_url = url + endpoint_string

        print(parameters_list) 
        print(endpoint_string)
        print(request_url)

        return request_url

        

    def request_data(self, url=str):

        headers = {"Authorization" : api_key}
        
        try:
        
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                raise AuthEx.RequestStatusCodeError(response.status_code)
            else:
                print(response.content) 

        except AuthEx.RequestStatusCodeError as err:
            print("Error: Response status code:{}".format(err))

        






