import sys
import inspect
from generated import openfeed_api_pb2
from generated import openfeed_pb2
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time


class OpenfeedClient(object):

    def __init__(self, username, password, server="openfeed.aws.barchart.com", debug=False):
        self.server = server
        self.username = username
        self.password = password
        self.debug = debug
        self.ws = websocket.WebSocket()
        self.stop = True
        self.token = None

        self.instrument_definitions = {}
        self.instruments_by_symbol = {}
        self.symbol_handlers = {}
        self.exchange_handlers = {}
        self.heartbeat_handlers = []

        self.login_req = openfeed_api_pb2.OpenfeedGatewayRequest(
            loginRequest=openfeed_api_pb2.LoginRequest(
                username=username, password=password))

        self.on_connected = None
        self.on_disconnected = None
        self.on_error = None

        websocket.enableTrace(self.debug)

    def start(self):
        self.__connect()

    def add_heartbeat_subscription(self, callback):
        self.heartbeat_handlers.append(callback)

    def add_symbol_subscription(self, symbol, callback):
        if symbol not in self.symbol_handlers:
            self.symbol_handlers[symbol] = []

            if self.token is not None:
                self._send_message(self.__create_symbol_request([symbol]))

        self.symbol_handlers[symbol].append(callback)

    def add_exchange_subscription(self, exchange, callback):
        if exchange not in self.exchange_handlers:
            self.exchange_handlers[exchange] = []

            if self.token is not None:
                self._send_message(self.__create_exchange_request([exchange]))

        self.exchange_handlers[exchange].append(callback)

    def get_instrument_definition(self, id):
        return self.instrument_definitions[id]

    def get_instrument_definition_by_symbol(self, symbol):
        return self.instruments_by_symbol[symbol]

    def _send_message(self, msg):
        self.ws.send(msg.SerializeToString(), websocket.ABNF.OPCODE_BINARY)

    def __connect(self):
        self.stop = False

        def handleLogin(msg):

            if msg.loginResponse.status.result > 1:
                raise Exception("Login has failed", msg)

            self.token = msg.loginResponse.token

            # sub to all existing interest
            self._send_message(self.__create_symbol_request(
                self.symbol_handlers.keys()))

            # sub to all existing exchanges
            self._send_message(self.__create_exchange_request(
                self.exchange_handlers.keys()))

            return msg

        def handleHeartbeat(msg):
            self.__notify_heartbeat_listeners(msg)
            return msg

        def handleSubscriptionResponse(msg):

            if msg.subscriptionResponse.status.result > 1:
                raise Exception("Subscription has failed", msg)

            self.__notify_symbol_listeners(
                msg.subscriptionResponse.symbol, msg)
            return msg

        def handleInstrumentDefinition(msg):
            self.instrument_definitions[msg.instrumentDefinition.marketId] = msg
            self.instruments_by_symbol[msg.instrumentDefinition.symbol] = msg
            return msg

        def handleMarketUpdate(msg):
            symbol = self.instrument_definitions[msg.marketUpdate.marketId].instrumentDefinition.symbol

            self.__notify_symbol_listeners(symbol, msg)

            return msg

        def handleMarketSnapshot(msg):
            symbol = self.instrument_definitions[msg.marketSnapshot.marketId].instrumentDefinition.symbol

            self.__notify_symbol_listeners(symbol, msg)
            return msg

        def on_message(ws, message):

            msg = openfeed_api_pb2.OpenfeedGatewayMessage()
            msg.ParseFromString(message)

            handlers = {
                "loginResponse": handleLogin,
                "heartBeat": handleHeartbeat,
                "subscriptionResponse": handleSubscriptionResponse,
                "instrumentDefinition": handleInstrumentDefinition,
                "marketSnapshot": handleMarketSnapshot,
                "marketUpdate": handleMarketUpdate,
            }

            handler = handlers.get(msg.WhichOneof(
                "data"), lambda x: print("Unhandled Message: ", x))

            try:
                handler(msg)
            except Exception as e:
                if self.debug:
                    print("Failed to handling incoming message:", e)
                self.__callback(self.on_error, e)

        def on_error(ws, error):
            if self.debug:
                print("WS Error: ", error)
            self.__callback(self.on_error, error)

        def on_close(ws):
            if self.debug:
                print("WS Close")
            self.__callback(self.on_disconnected, ws)

        def on_open(ws):
            if self.debug:
                print("WS Open")

            self._send_message(self.login_req)

            self.__callback(self.on_connected, ws)

        self.ws = websocket.WebSocketApp("ws://" + self.server + "/ws",
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close,
                                         on_open=on_open)

        self.ws.run_forever()

    def __notify_symbol_listeners(self, symbol, msg):
        for cb in self.symbol_handlers[symbol]:
            try:
                cb(msg)
            except Exception as e:
                if self.debug:
                    print("Failed to notify `symbol` callback", e)
                self.__callback(self.on_error, e)

    def __notify_heartbeat_listeners(self, msg):
        for cb in self.heartbeat_handlers:
            try:
                cb(msg)
            except Exception as e:
                if self.debug:
                    print("Failed to notify `heartbeat` callback", e)
                self.__callback(self.on_error, e)

    def __create_symbol_request(self, symbols):
        requests = []

        for sym in symbols:
            requests.append(openfeed_api_pb2.SubscriptionRequest.Request(
                symbol=sym,
            ))

        of_req = openfeed_api_pb2.OpenfeedGatewayRequest(
            subscriptionRequest=openfeed_api_pb2.SubscriptionRequest(
                token=self.token,
                service=openfeed_pb2.Service.Value("REAL_TIME"),
                requests=requests
            ))

        return of_req

    def __create_exchange_request(self, exchanges):
        requests = []

        for exch in exchanges:
            requests.append(openfeed_api_pb2.SubscriptionRequest.Request(
                exchange=exch,
            ))

        of_req = openfeed_api_pb2.OpenfeedGatewayRequest(
            subscriptionRequest=openfeed_api_pb2.SubscriptionRequest(
                token=self.token,
                service=openfeed_pb2.Service.Value("REAL_TIME"),
                requests=requests
            ))

        return of_req

    def __callback(self, callback, *args):
        try:
            if callback is not None:
                callback(*args)
        except Exception as e:
            print("Failed to call callback", e)


if __name__ == "__main__":

    def handle_message(msg):
        print("of-client: Market Data: ", msg.WhichOneof("data"))

    def handle_heartbeat(msg):
        print("of-client: Heartbeat: ", msg)

    of_client = OpenfeedClient("username", "password", debug=False)

    of_client.add_symbol_subscription(symbol="AAPL", callback=handle_message)
    # of_client.add_exchange_subscription(
    #    exchange="NYSE", callback=handle_message)
    of_client.add_heartbeat_subscription(callback=handle_heartbeat)

    of_client.on_error = lambda x: print("of-client: something went wrong:", x)
    of_client.on_disconnected = lambda x: print("of-client: disconnected")
    of_client.on_connected = lambda x: print("of-client: connected")

    # blocking mode

    of_client.start()

    # non-blocking mode
    # thread.start_new_thread(of_client.start, ())

    # print("Started Openfeed Client")

    # while True:
    #   time.sleep(1000)
