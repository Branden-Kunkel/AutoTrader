# library to access API Data from 'polygon.io and then export that data
import re
import requests
import json
import exceptions.exceptions as AuthEx
import pprint 


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

    def sort_aggregates(self, data_object):

        aggregates_dictionary_sorted =  {
                                            "options_ticker": None,
                                            "open_price" : None,
                                            "close_price" : None,
                                            "high_price" : None,
                                            "low_price" : None,
                                            "transactions" : None,
                                            "otc_ticker" : None,
                                            "unix_timestamp" : None,
                                            "trading_volume" : None,
                                            "weighted_avg_price" : None
                                        }

        try:
            
            # polygon.io API gives a list with a (single) dictionary for the 'aggregates' response object rather than just a nested dictionary? BELOW
            aggregates_dict = data_object["results"]["underlying"]["aggregates"][0]

            for key in aggregates_dict:
                if key == 'T':
                    aggregates_dictionary_sorted["options_ticker"] = aggregates_dict[key]
                elif key == 'o':
                    aggregates_dictionary_sorted["open_price"] = aggregates_dict[key]
                elif key == 'c':
                    aggregates_dictionary_sorted["close_price"] = aggregates_dict[key]
                elif key == 'h':
                    aggregates_dictionary_sorted["high_price"] = aggregates_dict[key]
                elif key == 'l':
                    aggregates_dictionary_sorted["low_price"] = aggregates_dict[key]
                elif key == 'n':
                    aggregates_dictionary_sorted["transactions"] = aggregates_dict[key]
                elif key == 't':
                    aggregates_dictionary_sorted["unix_timestamp"] = aggregates_dict[key]
                elif key == 'v':
                    aggregates_dictionary_sorted["trading_volume"] = aggregates_dict[key]    
                elif key == 'vw':
                    aggregates_dictionary_sorted["weighted_avg_price"] = aggregates_dict[key]
                else:
                    pass
            print(aggregates_dict)
            print("\n")
            print(aggregates_dictionary_sorted)

        except KeyError as key_error:
            print("Error: Empty response object for {}".format(key_error.args))
            return

        

        




