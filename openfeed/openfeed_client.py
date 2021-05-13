from typing import Union
from generated import openfeed_api_pb2
from generated import openfeed_pb2
from generated import openfeed_instrument_pb2
import time
import traceback
import sys
import inspect
import collections
import websocket
import random
try:
    import thread
except ImportError:
    import _thread as thread


class OpenfeedClient(object):

    def __init__(self, username, password, server="openfeed.aws.barchart.com", debug=False):
        self.server = server
        self.username = username
        self.password = password
        self.debug = debug
        self.ws = websocket.WebSocket()
        self.token = None

        self.instrument_definitions = {}
        self.instruments_by_symbol = {}
        self.snapshots = {}

        self.symbol_handlers = {}
        self.exchange_handlers = {}
        self.heartbeat_handlers = []
        self.request_id_handlers = {}

        self.on_connected = None
        self.on_disconnected = None
        self.on_error = None

        websocket.enableTrace(self.debug)

    def start(self, blocking=True):
        """Starts the Openfeed client and underlying WebSocket connection

        Set blocking to False to disable blocking the calling thread.
        """
        if self.token is None:
            if blocking is not True:
                thread.start_new_thread(self.__connect, ())
            else:
                self.__connect()

        return self

    def stop(self):
        if self.token is not None:
            self.__reset()

        return self

    def add_heartbeat_subscription(self, callback):
        """Subscribe to [Heartbeat] messages (keep alive)

        [Heartbeat]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.HeartBeat
        """
        self.heartbeat_handlers.append(callback)

        return self

    def add_symbol_subscription(self, symbol: Union[str, list], callback, service="REAL_TIME", subscription_type=["QUOTE"], snapshot_interval_seconds=60):
        """Subscribe to [Market Data] by Barchart Symbols

        Complete list of [SubscriptionTypes]. List of [Service] types.

        Parameters
        ----------
        service: str, optional
            Default is `REAL_TIME` for delayed market data, set it to `DELAYED`, or for snapshots set it as one of `REAL_TIME_SNAPSHOT` or `DELAYED_SNAPSHOT'
        callback: Callable
            Your callback function for Market Data messages
        subscription_type: list, optional
            Default is ['QUOTE']. Can contain any of: 'ALL', 'QUOTE', 'QUOTE_PARTICIPANT', 'DEPTH_PRICE', 'DEPTH_ORDER', 'TRADES', 'OHLC'

        [Market Data]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.MarketUpdate
        [SubscriptionTypes]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.SubscriptionType
        [Service]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.Service
        """
        symbols = []

        if isinstance(symbol, list) == False:
            symbols = [symbol]
        else:
            symbols = symbol

        for sym in symbols:
            if sym not in self.symbol_handlers:
                self.symbol_handlers[sym] = []

            self.symbol_handlers[sym].append(
                Listener(symbol=sym, callback=callback, service=service, subscription_type=subscription_type, snapshot_interval_seconds=snapshot_interval_seconds))

        if self.token is not None:
            self._send_message(
                self.__create_subscription_request(symbols=symbols, service=service, subscription_type=subscription_type, snapshot_interval_seconds=snapshot_interval_seconds))

        return self

    def add_exchange_subscription(self, exchange: Union[str, list], callback, service="REAL_TIME", subscription_type=["QUOTE"], snapshot_interval_seconds=60):
        """Subscribe to [Market Data] by Barchart Exchange code(s).

        Complete list of [SubscriptionTypes]. List of [Service] types.

        Note: your credentials must have the correct service level (FEED) for this operation.

        [Market Data]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.MarketUpdate
        [SubscriptionTypes]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.SubscriptionType
        [Service]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.Service
        """
        exchanges = []

        if isinstance(exchange, list) == False:
            exchanges = [exchange]
        else:
            exchanges = exchange

        for exch in exchanges:
            if exch not in self.exchange_handlers:
                self.exchange_handlers[exch] = []

            self.exchange_handlers[exch].append(Listener(
                exchange=exch, callback=callback, service=service, subscription_type=subscription_type, snapshot_interval_seconds=snapshot_interval_seconds))

        if self.token is not None:
            self._send_message(
                self.__create_subscription_request(exchanges=exchanges, service=service, subscription_type=subscription_type, snapshot_interval_seconds=snapshot_interval_seconds))

        return self

    def request_available_exchanges(self, callback):
        """Request a list of available [Exchanges] for subscription.

        [Exchanges]: https://github.com/openfeed-org/proto/blob/master/openfeed_api.proto#L159-L173
        """
        rid = random.getrandbits(32)
        req = self.__create_exchange_request(rid)

        self.request_id_handlers[rid] = Request(callback, req)

        if self.token is not None:
            self._send_message(req)

        return self

    def request_instruments_for_exchange(self, exchange, callback):
        """Request a list of [Instrument Definitions] actively trading trading on an exchange.

        [Instrument Definitions]: https://openfeed-org.github.io/documentation/Message%20Specification/#openfeed_instrumentproto
        """

        rid = random.getrandbits(32)
        req = self.__create_instrument_request(rid, exchange=exchange)

        self.request_id_handlers[rid] = Request(callback, req)

        if self.token is not None:
            self._send_message(req)

        return self

    def request_instruments(self, callback, symbol=None, market_id=None, exchange=None):
        """Request [Instrument Definitions] by `symbol`, `market_id`, or `exchange` 

        See [Instrument Request]

        [Instrument Definitions]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.InstrumentDefinition
        [Instrument Request]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.InstrumentRequest
        """

        rid = random.getrandbits(32)
        req = self.__create_instrument_request(
            rid, market_id=market_id, symbol=symbol, exchange=exchange)

        self.request_id_handlers[rid] = Request(callback, req)

        if self.token is not None:
            self._send_message(req)

        return self

    def get_instrument_definitions(self):
        """Returns a dict of Openfeed [Instrument Definitions] keyed by MarketID

        [Instrument Definitions]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.InstrumentDefinition
        """
        return self.instrument_definitions

    def get_instrument_definition(self, id):
        """Returns an [Instrument Definition] for a Market ID

        [Instrument Definition]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.InstrumentDefinition
        """
        return self.instrument_definitions[id].instrumentDefinition

    def get_instrument_definition_by_symbol(self, symbol):
        """Returns an [Instrument Definition] for a [Symbol] string

        [Instrument Definition]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.InstrumentDefinition
        [Symbol]: https://openfeed-org.github.io/documentation/Message%20Specification/#org.openfeed.InstrumentDefinition.Symbol
        """
        return self.instruments_by_symbol[symbol].instrumentDefinition

    def _send_message(self, msg):
        if self.debug:
            print("Sending:", msg)
        self.ws.send(msg.SerializeToString(), websocket.ABNF.OPCODE_BINARY)

    def __reset(self):
        self.ws.close()
        self.token = None
        self.ws = websocket.WebSocket()

    def __connect(self):

        def handleLogin(msg):

            if msg.loginResponse.status.result > 1:
                raise Exception("Login has failed: ", msg)

            self.token = msg.loginResponse.token
            self.__send_existing_interest()

            return msg

        def handleHeartbeat(msg):
            self.__notify_heartbeat_listeners(msg)
            return msg

        def handleExchangeRequest(msg):
            rid = msg.exchangeResponse.correlationId

            if rid not in self.request_id_handlers:
                return msg

            self.request_id_handlers[rid].callback(msg)

            return msg

        def handleInstrumentResponse(msg):
            rid = msg.instrumentResponse.correlationId

            if rid not in self.request_id_handlers:
                return msg

            self.request_id_handlers[rid].callback(msg)

            return msg

        def handleInstrumentReferenceResponse(msg):
            rid = msg.instrumentReferenceResponse.correlationId

            self.instrument_definitions[msg.instrumentReferenceResponse.marketId] = msg
            self.instruments_by_symbol[msg.instrumentReferenceResponse.symbol] = msg

            if rid not in self.request_id_handlers:
                return msg

            self.request_id_handlers[rid].callback(msg)

            return msg

        def handleSubscriptionResponse(msg):

            if msg.subscriptionResponse.status.result > 1:
                raise Exception("Subscription has failed: ", msg)

            if len(msg.subscriptionResponse.symbol) > 0:
                self.__notify_symbol_listeners(
                    self.__create_instrument(msg.subscriptionResponse.symbol), msg)
            else:
                self.__notify_exchange_listeners(
                    msg.subscriptionResponse.exchange, msg)

            return msg

        def handleInstrumentDefinition(msg):
            self.instrument_definitions[msg.instrumentDefinition.marketId] = msg

            for symbol in msg.instrumentDefinition.symbols:
                self.instruments_by_symbol[symbol.symbol] = msg

            self.__notify_exchange_listeners(
                msg.instrumentDefinition.exchangeCode, msg)
            self.__notify_symbol_listeners(msg.instrumentDefinition, msg)

            return msg

        def handleMarketUpdate(msg):
            inst = self.instrument_definitions[msg.marketUpdate.marketId].instrumentDefinition

            self.__notify_exchange_listeners(inst.exchangeCode, msg)
            self.__notify_symbol_listeners(inst, msg)

            return msg

        def handleMarketSnapshot(msg):
            inst = self.instrument_definitions[msg.marketSnapshot.marketId].instrumentDefinition

            self.snapshots[inst.marketId] = msg

            self.__notify_exchange_listeners(inst.exchangeCode, msg)
            self.__notify_symbol_listeners(inst, msg)

            return msg

        def handleOHLC(msg):
            inst = self.instrument_definitions[msg.ohlc.marketId].instrumentDefinition

            self.__notify_exchange_listeners(inst.exchangeCode, msg)
            self.__notify_symbol_listeners(inst, msg)

            return msg

        handlers = {
            "loginResponse": handleLogin,
            "heartBeat": handleHeartbeat,
            "exchangeResponse": handleExchangeRequest,
            "subscriptionResponse": handleSubscriptionResponse,
            "instrumentResponse": handleInstrumentResponse,
            "instrumentReferenceResponse": handleInstrumentReferenceResponse,
            "instrumentDefinition": handleInstrumentDefinition,
            "marketSnapshot": handleMarketSnapshot,
            "marketUpdate": handleMarketUpdate,
            "ohlc": handleOHLC
        }

        def on_message(ws: websocket.WebSocketApp, message):

            msg = openfeed_api_pb2.OpenfeedGatewayMessage()
            msg.ParseFromString(message)

            msg_type = msg.WhichOneof("data")

            handler = handlers.get(
                msg_type, lambda x: print("Unhandled Message:", x))

            try:
                handler(msg)
            except Exception as e:
                if self.debug:
                    print("Failed handling incoming message:", msg_type, e)
                    traceback.print_exc()
                self.__callback(self.on_error, e)

        def on_error(ws, error):
            if self.debug:
                print("WebSocket Error: ", error)
                traceback.print_exc()
            self.__callback(self.on_error, error)

        def on_close(ws):
            if self.debug:
                print("WebSocket Close")

            self.__reset()
            self.__callback(self.on_disconnected, ws)

        def on_open(ws):
            if self.debug:
                print("WebSocket Open")

            self._send_message(self.__create_login_request())
            self.__callback(self.on_connected, ws)

        self.ws = websocket.WebSocketApp("ws://" + self.server + "/ws",
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close,
                                         on_open=on_open)

        self.ws.run_forever()

    def __notify_symbol_listeners(self, instrument, msg):

        # TODO review symbology handling, subbing by one and keying off the other can create unexpected results
        # for example subscribing to "ZCYAIA40.CM" will come back with OF symbol (less the suffix) in `instrument.symbol`
        # given the below, if the instrument contains duplicate `instrument.symbols`, the listeners will get duplicate callbacks

        for s in instrument.symbols:
            if s.symbol not in self.symbol_handlers or s.vendor != "Barchart":
                continue

            for cb in self.symbol_handlers[s.symbol]:
                try:
                    cb.callback(msg)
                except Exception as e:
                    if self.debug:
                        print("Failed to notify `symbol` callback:", s, e)
                    self.__callback(self.on_error, e)

    def __notify_exchange_listeners(self, exchange, msg):
        if exchange not in self.exchange_handlers:
            return

        for cb in self.exchange_handlers[exchange]:
            try:
                cb.callback(msg)
            except Exception as e:
                if self.debug:
                    print("Failed to notify `exchange` callback:", exchange, e)
                self.__callback(self.on_error, e)

    def __notify_heartbeat_listeners(self, msg):
        for cb in self.heartbeat_handlers:
            try:
                cb(msg)
            except Exception as e:
                if self.debug:
                    print("Failed to notify `heartbeat` callback:", e)
                self.__callback(self.on_error, e)

    def __send_existing_interest(self):
        all_listeners = list(self.symbol_handlers.values()) + \
            list(self.exchange_handlers.values())

        interest = {}

        # group symbols / exchanges by service and subscription_type
        for listeners in all_listeners:
            for l in listeners:
                if l.service not in interest:
                    interest[l.service] = {}
                listeners_by_service = interest[l.service]
                if l.key() not in listeners_by_service:
                    listeners_by_service[l.key()] = Listener(
                        symbol=l.symbol, exchange=l.exchange, service=l.service, subscription_type=l.subscription_type, snapshot_interval_seconds=l.snapshot_interval_seconds)
                else:
                    existing = listeners_by_service[l.key()]
                    existing.subscription_type = list(set(
                        existing.subscription_type + l.subscription_type))

        # send subscriptions
        for service in interest.keys():
            for i in interest[service].values():
                self._send_message(
                    self.__create_subscription_request(exchanges=i.exchanges(), symbols=i.symbols(), service=service, subscription_type=i.subscription_type, snapshot_interval_seconds=i.snapshot_interval_seconds))

        # send other rpc requests
        for req in self.request_id_handlers.values():
            req.send(self)

    def __create_subscription_request(self, exchanges=[], symbols=[], service="REAL_TIME", subscription_type=["QUOTE"], snapshot_interval_seconds=60):
        requests = []

        if len(exchanges) > 0:
            for exch in exchanges:
                requests.append(openfeed_api_pb2.SubscriptionRequest.Request(
                    exchange=exch,
                    subscriptionType=[openfeed_api_pb2.SubscriptionType.Value(
                        t) for t in subscription_type],
                    snapshotIntervalSeconds=snapshot_interval_seconds
                ))

        if len(symbols) > 0:
            for sym in symbols:
                requests.append(openfeed_api_pb2.SubscriptionRequest.Request(
                    symbol=sym,
                    subscriptionType=[openfeed_api_pb2.SubscriptionType.Value(
                        t) for t in subscription_type],
                    snapshotIntervalSeconds=snapshot_interval_seconds
                ))

        of_req = openfeed_api_pb2.OpenfeedGatewayRequest(
            subscriptionRequest=openfeed_api_pb2.SubscriptionRequest(
                token=self.token,
                service=openfeed_pb2.Service.Value(service),
                requests=requests
            ))

        return of_req

    def __create_exchange_request(self, correlation_id):
        return openfeed_api_pb2.OpenfeedGatewayRequest(
            exchangeRequest=openfeed_api_pb2.ExchangeRequest(
                correlationId=correlation_id,
                token=self.token
            )
        )

    def __create_instrument_reference_request(self, correlation_id, exchange):
        return openfeed_api_pb2.OpenfeedGatewayRequest(
            instrumentReferenceRequest=openfeed_api_pb2.InstrumentReferenceRequest(
                correlationId=correlation_id,
                token=self.token,
                exchange=exchange
            )
        )

    def __create_instrument_request(self, correlation_id, symbol=None, market_id=None, exchange=None):
        ir = openfeed_api_pb2.InstrumentRequest(
            correlationId=correlation_id,
            token=self.token,
            marketId=market_id
        )

        if symbol is not None:
            ir.symbol = symbol
        if market_id is not None:
            ir.marketId = market_id
        if exchange is not None:
            ir.exchange = exchange

        return openfeed_api_pb2.OpenfeedGatewayRequest(
            instrumentRequest=ir
        )

    def __create_instrument(self, symbol):
        return openfeed_instrument_pb2.InstrumentDefinition(
            symbol=symbol,
            symbols=[
                openfeed_instrument_pb2.InstrumentDefinition.Symbol(
                    vendor="Barchart",
                    symbol=symbol
                )
            ]
        )

    def __create_login_request(self):
        return openfeed_api_pb2.OpenfeedGatewayRequest(
            loginRequest=openfeed_api_pb2.LoginRequest(
                username=self.username, password=self.password))

    def __callback(self, callback, *args):
        try:
            if callback is not None:
                callback(*args)
        except Exception as e:
            print("Failed to call callback", e)


class Listener(object):
    def __init__(self, symbol="", exchange="", callback=None, service="REAL_TIME", subscription_type=["QUOTE"], snapshot_interval_seconds=60):
        self.symbol = symbol
        self.exchange = exchange
        self.callback = callback
        self.service = service
        self.subscription_type = subscription_type
        self.snapshot_interval_seconds = snapshot_interval_seconds

    def key(self):
        if len(self.exchange) > 0:
            return self.exchange
        return self.symbol

    def symbols(self):
        if len(self.symbol) > 0:
            return [self.symbol]
        return []

    def exchanges(self):
        if len(self.exchange) > 0:
            return [self.exchange]
        return []

    def has_same_interest(self, other):
        return collections.Counter(self.subscription_type) == collections.Counter(other.subscription_type)

    def send_interest(self, of_client: OpenfeedClient):
        pass


class Request(object):
    def __init__(self, callback, req):
        self.callback = callback
        self.request = req

    def send(self, of_client):
        request_type = self.request.WhichOneof("data")

        if request_type == "exchangeRequest":
            self.request.exchangeRequest.token = of_client.token
        elif request_type == "instrumentReferenceRequest":
            self.request.instrumentReferenceRequest.token = of_client.token
        elif request_type == "instrumentRequest":
            self.request.instrumentRequest.token = of_client.token

        of_client._send_message(self.request)


if __name__ == "__main__":

    def handle_message(msg):
        print("of-client: Market Data: ", msg.WhichOneof("data"))

    def handle_heartbeat(msg):
        print("of-client: Heartbeat: ", msg)

    of_client = OpenfeedClient("username", "password", debug=False)

    of_client.add_exchange_subscription(
        exchange="FOREX", callback=handle_message)
    of_client.add_heartbeat_subscription(callback=handle_heartbeat)

    of_client.on_error = lambda x: print("of-client: something went wrong:", x)
    of_client.on_disconnected = lambda x: print("of-client: disconnected")
    of_client.on_connected = lambda x: print("of-client: connected")

    # blocking mode
    of_client.start(blocking=False)

    while True:
        print("Number of Instruments:", len(
            of_client.get_instrument_definitions()))
        time.sleep(10)
