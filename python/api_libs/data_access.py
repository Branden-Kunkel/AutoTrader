# library to access API Data from 'polygon.io and then export that data
import re
import requests
import json
import yaml
import exceptions.exceptions as AuthEx
from datetime import datetime
import os.path as path

class DataAccessToolkit():
    """toolkit for various checks and functions pertaining to the 'data_access.py' module"""

    def validate_parameters(self, *params):
        try:
            for arg in params:
                if arg == None:
                    raise AuthEx.EmptyParameter(arg)
                else:
                    pass
        except AuthEx.EmptyParameter as err:
            print(err.error_msg())
            return
                


class GetApiData():
    """class serves as an engine to access API data"""

    def generate_request_url2(self, url: str, options_ticker: str, ticker: str, date: str, request_parameters: dict):
        
        try:

            date_regex = re.compile("(?<=/)\{(?:date)\}")
            options_ticker_regex = re.compile("(?<=/)\{(?:optionsTicker)\}")
            ticker_regex = re.compile("(?<=/)\{(?:ticker)\}")

            url_buffer = re.sub(date_regex, date, url)
            url_buffer2 = re.sub(options_ticker_regex, options_ticker, url_buffer)
            url_buffer3 = re.sub(ticker_regex, ticker, url_buffer2)

            parameters_list = []
            endpoint_string = ""
            try:
                for key, value in request_parameters.items():
                    if request_parameters[key] == None:
                        pass  
                    else:
                        parameters_list.append(key + "=" + value)
            except AttributeError as err:
                print(AuthEx.ErrorMessage.not_dict_type)
                return

            endpoint_string = "&".join(parameters_list)

            request_url = url_buffer3 + endpoint_string

            print("\n" + request_url + "\n")    
            
            return request_url
        
        except TypeError as err:
            if err.__cause__ == None:
                pass
            else:
                print("check exception")
                print(err)
                print(err.__cause__)
                return
            


    def request_data(self, url: str, api_key: str):

        try:
            
            headers = {"Authorization" : api_key}
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                raise AuthEx.RequestStatusCodeError(response.reason, response.status_code)
            else:
                if response.content == None:
                    raise AuthEx.NoDataInResponse(url)
                else:
                    response_object = json.loads(response.content)
                    return response_object

        except requests.exceptions.MissingSchema as err:
            print("Error: Missing Url! URL: {}.".format(url))
            return
        except requests.exceptions.InvalidSchema as err:
            print("Error: Url not valid! URL: {}.".format(url))
            return
        except AuthEx.RequestStatusCodeError as err:
            print(err.error_msg())
            return
        except AuthEx.NoDataInResponse as err:
            print(err.error_msg())
            return
        


class ExportApiData():
    """class serves as an engine to export api data"""

    def sort_api_data(self, data_object: dict, request_url: str):

        timestamp_object = datetime.now()
        timestamp = str(timestamp_object)
        req_url = request_url
        data = data_object

        try:

            data.update({"auto": {}})
            data["auto"]["auto_timestamp"] = timestamp 
            data["auto"]["auto_url"] = req_url 

            return data

        except TypeError as type_error:
            if type_error.__cause__ == None:
                print("Error: No response to sort for <request: {}>. Check data objects/api response.\n".format(request_url))
        except AttributeError as att_err:
            if att_err.__cause__ == None:
                print("Error: No response to sort for <request: {}>. Check data objects/api response.\n".format(request_url))



    def write_yaml(self, write_file_dir: str, data_object: dict, filename: str):

        write_directory = write_file_dir
        full_path = write_directory + filename

        try:
            with open(full_path, mode='a+') as write_file:
                yaml.safe_dump(data_object, write_file, explicit_start=True)
            return

        except FileNotFoundError as err:
            print("Error: API export file directory path in file_paths.yaml -> [api_files][api_export] does not exist!")
            return
        
        

    def write_json(self, write_file_dir: str, data_object: dict, filename: str):
        
        write_directory = write_file_dir
        full_path = write_directory + filename

        try:
            with open(full_path, mode='a+') as write_file:
                json.dump(data_object, write_file, indent=4, sort_keys=True)
            return

        except FileNotFoundError as err:
            print("Error: API export file directory path in file_paths.yaml -> [api_files][api_export] does not exist!")
            return
        
    
