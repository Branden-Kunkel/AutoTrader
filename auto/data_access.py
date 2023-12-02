# library to access API Data from 'polygon.io'
import re
import requests
import json
import exceptions.exceptions as AuthEx

base_regex_expression = "(?<=/)\{[a-zA-Z]*\}"
options_ticker_exp = "(?<=/)\{(?:optionsTicker)\}"
date_exp = "(?<=/)\{(?:date)\}"

class ApiDataPort():
    """class serves as an engine to access API data"""


################ REFERENCE DATA ENDPOINTS #####################

    def generate_request_url2(self, url, ticker, date, parameters=dict):
        
        date_regex = re.compile("(?<=/)\{(?:date)\}")
        ticker_regex = re.compile("(?<=/)\{(?:optionsTicker)\}")

        url_buffer = re.sub(ticker_regex, ticker, url)
        url_buffer2 = re.sub(date_regex, date, url_buffer)

        parameters_list = []
        endpoint_string = ""

        for key, value in parameters.items():
            if parameters[key] == None:
                pass
            else:
                parameters_list.append(key + "=" + value)
            
        endpoint_string = "&".join(parameters_list)

        request_url = url_buffer2 + endpoint_string

        print(request_url)    
        
        return request_url



    def request_data(self, url, api_key):

        headers = {"Authorization" : api_key}
        
        try:
        
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                raise AuthEx.RequestStatusCodeError(response.status_code)
            else:
                print(response.content) 

        except AuthEx.RequestStatusCodeError as err:
            print("Error: Response status code: {} > {}".format(err, response.reason))

        




