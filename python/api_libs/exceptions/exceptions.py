# custom error handling

class RequestStatusCodeError(Exception):
    """handles an API request status code != 200"""

    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def error_msg(self):
        msg = "Error!: Response status code: {} > {}.\n".format(self.status_code, self.reason)
        return msg
    


class NoDataInResponse(Exception):
    """handles no aggregate data from an API response"""
    
    def __init__(self, request_url):
        self.request_url = request_url

    def error_msg(self):
        msg = "Error!: No data in response object from <request:{}>. Check tickers, options tickers and dates in request_parameters.yaml\n".format(self.request_url)
        return msg
    


class EmptyParameter(Exception):
    """handles a required program parameter not being present(p=None/p=Null)"""

    def error_msg(self):
        msg = "Error!: Missing required program parameter.\n Start troubleshooting by verifying parameters in request_parameters.yaml\n"
        return msg


class InvalidParameterType(Exception):
    """handles recieving a parameter with a type that was unexpected"""

    def __init__(self, parameter, expected_type):
        self.parameter = parameter
        self.type = expected_type

    def error_msg(self):
        msg = "Error!: Expected a {} type parameter, got {} instead! Make sure all parameters in 'request_parameters.yaml are of <string> type.\n".format(str(self.type), str(type(self.parameter)))
        return msg
    


class ErrorMessage(Exception):
    """Custom Error messages for built in Exceptions"""

    not_dict_type = "Error!: Expected parameters wrapped in a <dict> object, got a different type instead."
