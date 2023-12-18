import data_access
import yaml

api_tools = data_access.GetApiData()
export_api = data_access.ExportApiData()

shared_test_url = ""


def test_endpoints(file_paths, endpoint_yaml):

    with open(file_paths, mode='r') as path_file:

        paths = yaml.safe_load(path_file)
        parameters_file = paths["api_parameters"]["request_parameters"]

    with open(parameters_file, mode='r') as parameters_file:

        parameters = yaml.safe_load(parameters_file)

        assets = parameters["asset_parameters"]
        static = parameters["static_parameters"]
        request = parameters[endpoint_yaml]

        options_ticker = assets["options_ticker"]
        ticker = assets["ticker"]
        date = assets["date"]
        parameters = request["parameters"]
        key = static["api_key"]
        url = request["url"]
        
        request_url = api_tools.generate_request_url2(url, options_ticker, ticker, date, parameters)
        global shared_test_url
        shared_test_url = request_url

        data_object = api_tools.request_data(request_url, key)

        return data_object
    

def test_data_export(data):
    
    with open("file_paths.yaml", mode='r') as paths_file:
        paths_yaml = yaml.safe_load(paths_file)
        write_dir = paths_yaml["api_parameters"]["api_export"]
        export_data = export_api.sort_api_data(data, shared_test_url)
        export_api.write_yaml(write_dir, export_data, "single_test.yaml")
    return