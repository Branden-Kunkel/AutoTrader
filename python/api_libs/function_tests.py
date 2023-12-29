# This module is simply to provide a basic working example of data_access module. The module is simple and efficient, as has virtually no hard coded values
#   making it reliable, maintainable and customizable. This function test is linked to the librarie's command prompt for easy and streamlined function testing.

#import needed libraries
import data_access
import yaml
import json
import os.path as path

# initialize classes from the data_access module
api_access = data_access.GetApiData()
export_api = data_access.ExportApiData()
tools = data_access.DataAccessToolkit()

# declaring some static global variables for storing parameters
export_file_path = "" 
api_key = ""
date = ""
ticker = ""
options_ticker = ""

# generating the respective parameters into a python dict via library functions
settings = tools.settings()
req_params = tools.req_params()
file_paths = tools.file_paths()

# loading the required values into the global variables using the generated python dict
export_file_path = file_paths["api_files"]["api_export"]
api_key = settings["static"]["api_key"]
date = req_params['asset_parameters']["date"]
ticker = req_params["asset_parameters"]["ticker"]
options_ticker = req_params["asset_parameters"]["options_ticker"]

# function to test a basic implementation of the program. This will make one request and then write the sorted response to a .yaml AND a .json file
def test(endpoint_yaml):

    # dynamic parameter allocation with our generated dictionaries
    parameters = req_params[endpoint_yaml]["parameters"]
    base_url = req_params[endpoint_yaml]["url"]

    # create request url, make the request and then sort/stamp the response object in that order
    # Module make a good one liner easy!
    # ONE LINER: data = export_api.sort_api_data(api_access.request_data(api_access.generate_request_url2(base_url, options_ticker, ticker, date, parameters), api_key), api_access.generate_request_url2(base_url, options_ticker, ticker, date, parameters))

    url = api_access.generate_request_url2(base_url, options_ticker, ticker, date, parameters)
    api_data = api_access.request_data(url, api_key)
    sorted_data = export_api.sort_api_data(api_data, url)

    # write data to .yaml and .json respectively
    export_api.write_yaml(export_file_path, sorted_data, "test.yaml")
    export_api.write_json(export_file_path, sorted_data, "test.json")

    # DONE!
    return
