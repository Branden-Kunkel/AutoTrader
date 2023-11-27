
import data_access
import parameters.data_access_params as test_engine

test_build = test_engine.ReferenceDataApiParameters
url = test_build.view_all_tickers_url
params = test_build.view_all_tickers_paramaters

test = data_access.ApiDataPort()

test.request_data(test.generate_request_url(url, params))

print("DONE")