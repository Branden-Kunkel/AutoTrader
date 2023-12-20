# custom error handling

class RequestStatusCodeError(Exception):
    """handles an API request status code != 200"""

    def __init__(self, status_code):
        self.status_code = status_code

    def __str__(self) -> str:
        return(repr(self.status_code))
    

class NoResponseAggregates(Exception):
    """handles no aggregate data from an API response"""
    
    def __init__(self, request_url):
        self.request_url = request_url

    def __str__(self) -> str:
        return(repr(self.request_url))
    
class DataNotDict(Exception):
    """handles getting a data type that is not 'dict' when 'dict' is expected"""

    def __init__(self, data_type):
        self.data_type = data_type

    def __str__(self) -> str:
        return(repr(self.data_type))
    
class DataExportFail(Exception):
    """handles data export file not being written"""

    def __str__(self) -> str:
        return(repr("Error: Data from the api was not written to a file.\nStart troubleshooting by checking the file path in file_paths.yaml -> [api_files][api_export]"))