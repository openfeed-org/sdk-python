import openfeed

if __name__ == "__main__":

    # new client with credentials
    of_client = openfeed.OpenfeedClient("username", "password")

    # app state handlers
    of_client.on_error = lambda x: print("Error:", x)
    of_client.on_connected = lambda x: print("Connected")
    of_client.on_disconnected = lambda x: print("Disconnected")

    # sub to markets by symbol
    def on_message(msg):
        print("Market Data Message: ", msg)

    of_client.add_symbol_subscription("AAPL", callback=on_message)

    # sub to markets by exchange
    of_client.add_exchange_subscription("NYSE", callback=on_message)

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
