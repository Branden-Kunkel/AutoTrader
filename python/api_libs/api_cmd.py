import function_tests as test
import pprint
import cmd
import os
import yaml

file_paths = "file_paths.yaml"


def display_test(object):
    pprint.pprint(object)
    return
   

class TestCmdInterface(cmd.Cmd):
    """command interface"""

    prompt = "PolygonTestCMD$"

    def do_help(self, arg):
        keywords =  ["rsi - relative strength index",
                     "sma - simple moving average",
                     "ema - exponential moving average",
                     "tickers - view tickers (defaults to all)",
                     "options - display options contracts (defaults to all)",
                     "macd = moving average convergence/divergence",
                    ]
        print("Type keyword > Enter to test api endpoint. Customize request parameters in request_parameters.yaml! " + "\n")
        print("\n" + "KEYWORDS: " + "\n")
        for keyword in keywords:
            print(keyword)


    def do_rsi(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "relative_strength_index"))
        return
    
    def do_sma(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "simple_moving_average"))
        return
    
    def do_ema(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "exponential_moving_average"))
        return

    def do_macd(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "macd"))
        return
    
    def do_options(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "options_contracts"))
        return
    
    def do_contract(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "options_contract"))
        return

    def do_tickers(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "view_tickers"))
        return
    
    def do_tickerv3(self, arg):
        test.test_data_export(test.test_endpoints(file_paths, "ticker_v3"))

    def do_cwd(self, arg):
        print(os.getcwd())

    
cli = TestCmdInterface()
cli.cmdloop()

