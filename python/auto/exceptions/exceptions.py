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