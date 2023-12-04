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

    def generate_request_url2(self, url, options_ticker, ticker, date, parameters=dict):
        
        try:

            date_regex = re.compile("(?<=/)\{(?:date)\}")
            options_ticker_regex = re.compile("(?<=/)\{(?:optionsTicker)\}")
            ticker_regex = re.compile("(?<=/)\{(?:ticker)\}")

            url_buffer = re.sub(date_regex, date, url)
            url_buffer2 = re.sub(options_ticker_regex, options_ticker, url_buffer)
            url_buffer3 = re.sub(ticker, ticker, url_buffer2)

            parameters_list = []
            endpoint_string = ""

            for key, value in parameters.items():
                if parameters[key] == None:
                    pass
                else:
                    parameters_list.append(key + "=" + value)
                
            endpoint_string = "&".join(parameters_list)

            request_url = url_buffer3 + endpoint_string

            print("\n" + request_url + "\n")    
            
            return request_url
        
        except TypeError as err:
            print("Error: Parameter Type: Make sure all parameters in \'request_parameters.yaml\' are of \'string\' type.\n")
            return


    def request_data(self, url, api_key):

        headers = {"Authorization" : api_key}
        
        try:
        
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                raise AuthEx.RequestStatusCodeError(response.status_code)
            else:
                response_object = json.loads(response.content)
                #print(response_object)    
            return response_object

        except AuthEx.RequestStatusCodeError as err:
            print("Error: Response status code: {} > {}".format(err, response.reason))

        except TypeError as err:
            print("Error: Parameter Type: Make sure all parameters in \'request_parameters.yaml\' are of \'string\' type.\n")

        




