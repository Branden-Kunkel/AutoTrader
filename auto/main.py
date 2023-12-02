import data_access
import yaml

api_tools = data_access.ApiDataPort()

def test_get_req_param_path():

    try:
        with open("file_paths.yaml", mode='r') as paths:

            paths_dict = yaml.safe_load(paths)
            request_parameters_path = paths_dict["api_parameters"]["request_parameters"]

    except FileNotFoundError:
         print("File not Found: \"file_paths.yaml\". Make sure the file is in the programs working directory and try again.")

    return request_parameters_path


def test_get_tickers_parameters(parameters_path):

    try:
        with open(test_get_req_param_path(), mode='r') as params_file:

                params_object = yaml.safe_load(params_file)

                ticker = params_object["ticker"][0]
                date = params_object["date"][0]
                url = params_object["view_tickers"]["url"]
                parameters = params_object["view_tickers"]["parameters"]
                key = params_object["static_parameters"]["api_key"]
    except FileNotFoundError:
        print("File not Found: \"request_parameters.yaml\". Make sure the file path in \"file_paths.yaml\" is correct and try again.")

    return url, parameters, key, ticker, date
    

def test_get_dailyopenclose_parameters(parameters_path):

    with open(test_get_req_param_path(), mode='r') as params_file:

            params_object = yaml.safe_load(params_file)

            ticker = params_object["ticker"][0]
            date = params_object["date"][0]
            url = params_object["daily_open_close"]["url"]
            parameters = params_object["daily_open_close"]["parameters"]
            key = params_object["static_parameters"]["api_key"]

            return url, parameters, key, ticker, date

    
tickers_test_url, tickers_test_parameters, api_key, ticker, date = test_get_tickers_parameters(test_get_req_param_path)

doc_test_url, doc_test_parameters, api_key2, ticker2, date2 = test_get_dailyopenclose_parameters(test_get_req_param_path)



def test_tickers():
    api_tools.request_data(api_tools.generate_request_url2(tickers_test_url, ticker, date, tickers_test_parameters),api_key)

def test_dailyopenclose():
     api_tools.request_data(api_tools.generate_request_url2(doc_test_url, ticker2, date2, doc_test_parameters), api_key)

#test_tickers()
test_dailyopenclose()

    


print("DONE")