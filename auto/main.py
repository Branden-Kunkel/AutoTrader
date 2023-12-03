import endpoint_tests as test
import pprint
import cmd



#test.test_options_contracts() ## works as intended

#test.test_dailyopenclose() ##cant get to work? response 404 'not found'

#test.test_sma() ## works as intended

#test.test_ema() ##works as intended

#test.test_macd() ##works as inteded

#test.test_rsi() ## works as intended

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
        display_test(test.test_rsi())
        return
    
    def do_sma(self, arg):
        display_test(test.test_sma())
        return
    
    def do_ema(self, arg):
        display_test(test.test_ema())
        return

    def do_macd(self, arg):
        display_test(test.test_macd())
        return
    
    def do_options(self, arg):
        display_test(test.test_options_contracts())
        return
    
    def do_tickers(self, arg):
        display_test(test.test_tickers())
        return
    

cli = TestCmdInterface()
cli.cmdloop()
        

