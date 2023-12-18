# library to access API Data from 'polygon.io and then export that data
import re
import requests
import json
import yaml
import exceptions.exceptions as AuthEx
from datetime import datetime


class GetApiData():
    """class serves as an engine to access API data"""

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
            return response_object

        except AuthEx.RequestStatusCodeError as err:
            print("Error: Response status code: {} > {}".format(err, response.reason))
            return

        except TypeError as err:
            print("Error: Parameter Type: Make sure all parameters in \'request_parameters.yaml\' are of \'string\' type.\n")
            return



class ExportApiData():
    """class serves as an engine to export api data"""

    def sort_api_data(self, data_object, request_url, timezone=str):

        if timezone == None:
            timezone = "America/Los_Angeles"
        else:
            pass

        timestamp = datetime.now()

        mutable_dict = data_object

        try:
            # polygon.io API gives a list with a (single) dictionary for the 'aggregates' response object rather than just a nested dictionary? BELOW
            for key in mutable_dict["results"]["underlying"]["aggregates"][0]:
                if key == "T":
                    key = "options_ticker"
                elif key == "c":
                    key = "close_price"
                elif key == "h":
                    key = "high_price"
                elif key == "l":
                    key = "low_price"
                elif key == "n":
                    key = "transactions"
                elif key == "o":
                    key = "open_price"
                elif key == "t":
                    key = "unix_timestamp"
                elif key == "v":
                    key = "trade_volume"
                elif key == "vw":
                    key = "vol_weight_avg"
                else:
                    pass

            mutable_dict["auto_timestamp"] = timestamp
            mutable_dict["auto_url"] = request_url 

            return mutable_dict

        except KeyError as key_error:
            print("Error: No aggregates present in response for : {}".format(key_error.args))
            return
        

    def write_yaml(self, write_file_dir, data_object, filename):

        write_directory = write_file_dir
        full_path = write_directory + filename

        try:
            with open(full_path, mode='+a') as write_file:
                yaml.safe_dump(data_object, write_file, explicit_start=True)

        except Exception:
            print("Author, check this exception")
            return
        

    def write_csv():
        
        pass

