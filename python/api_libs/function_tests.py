import data_access
import yaml
import json
import os.path as path

api_tools = data_access.GetApiData()
export_api = data_access.ExportApiData()
datakit = data_access.DataAccessToolkit()

shared_test_url = ""

def test_reload_export(file_dir, file_name):
    full_path = file_dir + file_name
    try:
        with open(full_path, mode='r') as test_file:
            if path.splitext(file_name)[1] == ".yaml":
                yaml_obj = yaml.safe_load(test_file)
                print(yaml_obj)
                return
            elif path.splitext(file_name)[1] == ".json":
                json_obj = json.load(test_file)
                print(json_obj)
                return
            else:
                print("File type not in this test scope!\n")
                return
    except yaml.YAMLError as err:
        pass 


def test_endpoints(file_paths, endpoint_yaml):

    with open(file_paths, mode='r') as path_file:

        paths = yaml.safe_load(path_file)
        parameters_file = paths["api_files"]["request_parameters"]

    with open(parameters_file, mode='r') as parameters_file:

        parameters = yaml.safe_load(parameters_file)

        assets = parameters["asset_parameters"]
        static = parameters["static_parameters"]
        request = parameters[endpoint_yaml]

        options_ticker = assets["options_ticker"]
        ticker = assets["ticker"]
        date = assets["date"]
        params = request["parameters"]
        key = static["api_key"]
        url = request["url"]

        datakit.validate_parameters(assets, static, request, options_ticker, ticker, date, params, key, url)
                
        request_url = api_tools.generate_request_url2(url, options_ticker, ticker, date, params)
        global shared_test_url
        shared_test_url = request_url

        data_object = api_tools.request_data(request_url, key)

        return data_object
    

def test_data_export(data):
    
    with open("file_paths.yaml", mode='r') as paths_file:
        paths_yaml = yaml.safe_load(paths_file)
        write_dir = paths_yaml["api_files"]["api_export"]
        export_data = export_api.sort_api_data(data, shared_test_url)
        export_api.write_yaml(write_dir, export_data, "single_test.yaml")
        export_api.write_json(write_dir, export_data, "single_test.json")
    return

