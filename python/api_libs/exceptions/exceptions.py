# custom error handling

class RequestStatusCodeError(Exception):
    """handles an API request status code != 200"""

    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def error_msg(self):
        msg = "Error: Response status code: {} > {}.\n".format(self.status_code, self.reason)
        return msg
    

class NoDataInResponse(Exception):
    """handles no aggregate data from an API response"""
    
    def __init__(self, request_url):
        self.request_url = request_url

    def error_msg(self):
        msg = "Error: No data in response object from <request:{}>. Check tickers, options tickers and dates in request_parameters.yaml".format(self.request_url)
        return msg
    
    
class DataExportFail(Exception):
    """handles data export file not being written"""

    def __str__(self) -> str:
        return(repr("Error: Data from the api was not written to a file.\nStart troubleshooting by checking the file path in file_paths.yaml -> [api_files][api_export]"))


class EmptyParameter(Exception):
    """handles a required program parameter not being present(p=None/p=Null)"""

    def __init__(self, parameter):
        self.parameter = parameter

    def error_msg(self):
        msg = "Error: Missing required program parameter! Check request_parameters.yaml and verify parameters for request."
        return msg
    

    
class ErrorMessage(Exception):
    """Custom Error messages for built in Exceptions"""
    def __init__(self, object):
        self.object = object

    not_dict_type = "Error: Expected parameters wrapped in a <dict> object, got a different type instead."
