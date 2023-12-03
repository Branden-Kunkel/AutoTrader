import data_access
import yaml

api_tools = data_access.ApiDataPort()


def test_tickers():

    with open("file_paths.yaml", mode='r') as path_file:

        paths = yaml.safe_load(path_file)
        parameters_file = paths["api_parameters"]["request_parameters"]

    with open(parameters_file, mode='r') as parameters_file:

        parameters = yaml.safe_load(parameters_file)

        assets = parameters["asset_parameters"]
        static = parameters["static_parameters"]
        request = parameters["view_tickers"]

        options_ticker = assets["options_ticker"]
        ticker = assets["ticker"]
        date = assets["date"]
        parameters = request["parameters"]
        key = static["api_key"]
        url = request["url"]
        request_url = api_tools.generate_request_url2(url, options_ticker, ticker, date, parameters)

        api_tools.request_data(request_url, key)



def test_dailyopenclose():

    with open("file_paths.yaml", mode='r') as path_file:

        paths = yaml.safe_load(path_file)
        parameters_file = paths["api_parameters"]["request_parameters"]

    with open(parameters_file, mode='r') as parameters_file:

        parameters = yaml.safe_load(parameters_file)

        assets = parameters["asset_parameters"]
        static = parameters["static_parameters"]
        request = parameters["daily_open_close"]

        options_ticker = assets["options_ticker"]
        ticker = assets["ticker"]
        date = assets["date"]
        parameters = request["parameters"]
        key = static["api_key"]
        url = request["url"]
        request_url = api_tools.generate_request_url2(url, options_ticker, ticker, date, parameters)

        api_tools.request_data(request_url, key)



def test_options_contracts():

    with open("file_paths.yaml", mode='r') as path_file:

        paths = yaml.safe_load(path_file)
        parameters_file = paths["api_parameters"]["request_parameters"]

    with open(parameters_file, mode='r') as parameters_file:

        parameters = yaml.safe_load(parameters_file)

        assets = parameters["asset_parameters"]
        static = parameters["static_parameters"]
        request = parameters["options_contracts"]

        options_ticker = assets["options_ticker"]
        ticker = assets["ticker"]
        date = assets["date"]
        parameters = request["parameters"]
        key = static["api_key"]
        url = request["url"]
        request_url = api_tools.generate_request_url2(url, options_ticker, ticker, date, parameters)

        api_tools.request_data(request_url, key)



def test_sma():

    with open("file_paths.yaml", mode='r') as path_file:

        paths = yaml.safe_load(path_file)
        parameters_file = paths["api_parameters"]["request_parameters"]

    with open(parameters_file, mode='r') as parameters_file:

        parameters = yaml.safe_load(parameters_file)

        assets = parameters["asset_parameters"]
        static = parameters["static_parameters"]
        request = parameters["simple_moving_average"]

        options_ticker = assets["options_ticker"]
        ticker = assets["ticker"]
        date = assets["date"]
        parameters = request["parameters"]
        key = static["api_key"]
        url = request["url"]
        request_url = api_tools.generate_request_url2(url, options_ticker, ticker, date, parameters)

        api_tools.request_data(request_url, key)


