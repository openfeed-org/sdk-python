import openfeed
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='Username')
    parser.add_argument('-p', help='Password')
    args = parser.parse_args()

    # new client with credentials
    of_client = openfeed.OpenfeedClient(
        args.u, args.p, debug=False, server="demo.openfeed.barchart.com")

    # app state handlers
    of_client.on_error = lambda x: print("OnError:", x)
    of_client.on_connected = lambda x: print("OnConnected")
    of_client.on_disconnected = lambda x: print("OnDisconnected")
    of_client.on_login = lambda x: print("OnLogin:", x)
    of_client.on_logout = lambda x: print("OnLogout:", x)

    # add a global message handler for all incoming OF messages
    # of_client.on_message = lambda msg: print("Global Message:", msg)

    # sub message handler
    def on_message(msg):
        print("Market Data Message: ", msg)

    # subscribe to UDS an filter by type (optional)
    of_client.add_symbol_subscription(
        "T8^UDS", callback=on_message, subscription_type=["QUOTE"], spread_type_filter=["RR", "JR"])

    # of_client.request_instruments_for_exchange("AMEX", callback=on_message)

    # list exchanges

    # of_client.request_available_exchanges(
    #    lambda x: print("Openfeed Exchanges:", x))

    # sub to markets by exchange
    # of_client.add_exchange_subscription("NYSE", callback=on_message)

    # blocking mode
    of_client.start()

    #
    # non-blocking mode
    #
    # of_client.start(blocking=False)

    # print("Started Openfeed Client")

    # add additional market data subscriptions

    # of_client.add_symbol_subscription("NEM", callback=on_message)

    # simulate block to keep app alive
    # while True:
    #   time.sleep(1000)
