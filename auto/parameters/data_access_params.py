# paramaters for the data access

static_parameters = {
                        "base_polygonio_url" : "https://api.polygon.io/",
                        "api_key" : "Bearer "
                    }


class ReferenceDataApiParameters():
    """class for endpoints and their respective parameters"""

    view_all_tickers_paramaters =   {
                                        "ticker" : None, #string 
                                        "type" : None, #string
                                        "market" : None, #string
                                        "exchange" : None, #string
                                        "cusip" : None, #string
                                        "cik" : None, #string
                                        "date" : None, #string
                                        "search" : None, #string
                                        "active" : "true", # string
                                        "order" : "asc", #string
                                        "limit" : "10", #string
                                        "sort" : "ticker", #string
                                    }
    
    view_all_tickers_url = "https://api.polygon.io/v3/reference/tickers?"



