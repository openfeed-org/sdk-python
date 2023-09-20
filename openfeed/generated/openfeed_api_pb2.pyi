import openfeed_instrument_pb2 as _openfeed_instrument_pb2
import openfeed_pb2 as _openfeed_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_RESULT: _ClassVar[Result]
    SUCCESS: _ClassVar[Result]
    JWT_EXPIRED: _ClassVar[Result]
    JWT_INVALID: _ClassVar[Result]
    DUPLICATE_LOGIN: _ClassVar[Result]
    INVALID_SYMBOL: _ClassVar[Result]
    INVALID_MARKET_ID: _ClassVar[Result]
    INVALID_EXCHANGE: _ClassVar[Result]
    INVALID_CHANNEL_ID: _ClassVar[Result]
    MALFORMED_MESSAGE: _ClassVar[Result]
    UNEXPECTED_MESSAGE: _ClassVar[Result]
    NOT_SUBSCRIBED: _ClassVar[Result]
    DUPLICATE_SUBSCRIPTION: _ClassVar[Result]
    INVALID_CREDENTIALS: _ClassVar[Result]
    INSUFFICIENT_PRIVILEGES: _ClassVar[Result]
    AUTHENTICATION_REQUIRED: _ClassVar[Result]
    GENERIC_FAILURE: _ClassVar[Result]

class SubscriptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ALL: _ClassVar[SubscriptionType]
    QUOTE: _ClassVar[SubscriptionType]
    QUOTE_PARTICIPANT: _ClassVar[SubscriptionType]
    DEPTH_PRICE: _ClassVar[SubscriptionType]
    DEPTH_ORDER: _ClassVar[SubscriptionType]
    TRADES: _ClassVar[SubscriptionType]
    CUMLATIVE_VOLUME: _ClassVar[SubscriptionType]
    OHLC: _ClassVar[SubscriptionType]
    OHLC_NON_REGULAR: _ClassVar[SubscriptionType]

class SymbolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BARCHART: _ClassVar[SymbolType]
    EXCHANGE: _ClassVar[SymbolType]
UNKNOWN_RESULT: Result
SUCCESS: Result
JWT_EXPIRED: Result
JWT_INVALID: Result
DUPLICATE_LOGIN: Result
INVALID_SYMBOL: Result
INVALID_MARKET_ID: Result
INVALID_EXCHANGE: Result
INVALID_CHANNEL_ID: Result
MALFORMED_MESSAGE: Result
UNEXPECTED_MESSAGE: Result
NOT_SUBSCRIBED: Result
DUPLICATE_SUBSCRIPTION: Result
INVALID_CREDENTIALS: Result
INSUFFICIENT_PRIVILEGES: Result
AUTHENTICATION_REQUIRED: Result
GENERIC_FAILURE: Result
ALL: SubscriptionType
QUOTE: SubscriptionType
QUOTE_PARTICIPANT: SubscriptionType
DEPTH_PRICE: SubscriptionType
DEPTH_ORDER: SubscriptionType
TRADES: SubscriptionType
CUMLATIVE_VOLUME: SubscriptionType
OHLC: SubscriptionType
OHLC_NON_REGULAR: SubscriptionType
BARCHART: SymbolType
EXCHANGE: SymbolType

class OpenfeedGatewayRequest(_message.Message):
    __slots__ = ["loginRequest", "logoutRequest", "subscriptionRequest", "instrumentRequest", "instrumentReferenceRequest", "exchangeRequest"]
    LOGINREQUEST_FIELD_NUMBER: _ClassVar[int]
    LOGOUTREQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTREQUEST_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTREFERENCEREQUEST_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEREQUEST_FIELD_NUMBER: _ClassVar[int]
    loginRequest: LoginRequest
    logoutRequest: LogoutRequest
    subscriptionRequest: SubscriptionRequest
    instrumentRequest: InstrumentRequest
    instrumentReferenceRequest: InstrumentReferenceRequest
    exchangeRequest: ExchangeRequest
    def __init__(self, loginRequest: _Optional[_Union[LoginRequest, _Mapping]] = ..., logoutRequest: _Optional[_Union[LogoutRequest, _Mapping]] = ..., subscriptionRequest: _Optional[_Union[SubscriptionRequest, _Mapping]] = ..., instrumentRequest: _Optional[_Union[InstrumentRequest, _Mapping]] = ..., instrumentReferenceRequest: _Optional[_Union[InstrumentReferenceRequest, _Mapping]] = ..., exchangeRequest: _Optional[_Union[ExchangeRequest, _Mapping]] = ...) -> None: ...

class OpenfeedGatewayMessage(_message.Message):
    __slots__ = ["loginResponse", "logoutResponse", "instrumentResponse", "instrumentReferenceResponse", "subscriptionResponse", "marketStatus", "heartBeat", "instrumentDefinition", "marketSnapshot", "marketUpdate", "volumeAtPrice", "ohlc", "exchangeResponse", "instrumentAction"]
    LOGINRESPONSE_FIELD_NUMBER: _ClassVar[int]
    LOGOUTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTREFERENCERESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    MARKETSTATUS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTDEFINITION_FIELD_NUMBER: _ClassVar[int]
    MARKETSNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    MARKETUPDATE_FIELD_NUMBER: _ClassVar[int]
    VOLUMEATPRICE_FIELD_NUMBER: _ClassVar[int]
    OHLC_FIELD_NUMBER: _ClassVar[int]
    EXCHANGERESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTACTION_FIELD_NUMBER: _ClassVar[int]
    loginResponse: LoginResponse
    logoutResponse: LogoutResponse
    instrumentResponse: InstrumentResponse
    instrumentReferenceResponse: InstrumentReferenceResponse
    subscriptionResponse: SubscriptionResponse
    marketStatus: _openfeed_pb2.MarketStatus
    heartBeat: _openfeed_pb2.HeartBeat
    instrumentDefinition: _openfeed_instrument_pb2.InstrumentDefinition
    marketSnapshot: _openfeed_pb2.MarketSnapshot
    marketUpdate: _openfeed_pb2.MarketUpdate
    volumeAtPrice: _openfeed_pb2.VolumeAtPrice
    ohlc: _openfeed_pb2.Ohlc
    exchangeResponse: ExchangeResponse
    instrumentAction: _openfeed_pb2.InstrumentAction
    def __init__(self, loginResponse: _Optional[_Union[LoginResponse, _Mapping]] = ..., logoutResponse: _Optional[_Union[LogoutResponse, _Mapping]] = ..., instrumentResponse: _Optional[_Union[InstrumentResponse, _Mapping]] = ..., instrumentReferenceResponse: _Optional[_Union[InstrumentReferenceResponse, _Mapping]] = ..., subscriptionResponse: _Optional[_Union[SubscriptionResponse, _Mapping]] = ..., marketStatus: _Optional[_Union[_openfeed_pb2.MarketStatus, _Mapping]] = ..., heartBeat: _Optional[_Union[_openfeed_pb2.HeartBeat, _Mapping]] = ..., instrumentDefinition: _Optional[_Union[_openfeed_instrument_pb2.InstrumentDefinition, _Mapping]] = ..., marketSnapshot: _Optional[_Union[_openfeed_pb2.MarketSnapshot, _Mapping]] = ..., marketUpdate: _Optional[_Union[_openfeed_pb2.MarketUpdate, _Mapping]] = ..., volumeAtPrice: _Optional[_Union[_openfeed_pb2.VolumeAtPrice, _Mapping]] = ..., ohlc: _Optional[_Union[_openfeed_pb2.Ohlc, _Mapping]] = ..., exchangeResponse: _Optional[_Union[ExchangeResponse, _Mapping]] = ..., instrumentAction: _Optional[_Union[_openfeed_pb2.InstrumentAction, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["result", "message", "service"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    result: Result
    message: str
    service: _openfeed_pb2.Service
    def __init__(self, result: _Optional[_Union[Result, str]] = ..., message: _Optional[str] = ..., service: _Optional[_Union[_openfeed_pb2.Service, str]] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ["correlationId", "username", "password", "clientVersion", "protocolVersion", "jwt"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLIENTVERSION_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLVERSION_FIELD_NUMBER: _ClassVar[int]
    JWT_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    username: str
    password: str
    clientVersion: str
    protocolVersion: int
    jwt: str
    def __init__(self, correlationId: _Optional[int] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., clientVersion: _Optional[str] = ..., protocolVersion: _Optional[int] = ..., jwt: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ["correlationId", "status", "token"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    status: Status
    token: str
    def __init__(self, correlationId: _Optional[int] = ..., status: _Optional[_Union[Status, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ["correlationId", "token"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    token: str
    def __init__(self, correlationId: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ["correlationId", "status"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    status: Status
    def __init__(self, correlationId: _Optional[int] = ..., status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class InstrumentRequest(_message.Message):
    __slots__ = ["correlationId", "token", "symbol", "marketId", "exchange", "channelId"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    token: str
    symbol: str
    marketId: int
    exchange: str
    channelId: int
    def __init__(self, correlationId: _Optional[int] = ..., token: _Optional[str] = ..., symbol: _Optional[str] = ..., marketId: _Optional[int] = ..., exchange: _Optional[str] = ..., channelId: _Optional[int] = ...) -> None: ...

class InstrumentResponse(_message.Message):
    __slots__ = ["correlationId", "status", "numberOfDefinitions", "symbol", "marketId", "exchange", "channelId", "exchangeId"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEID_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    status: Status
    numberOfDefinitions: int
    symbol: str
    marketId: int
    exchange: str
    channelId: int
    exchangeId: int
    def __init__(self, correlationId: _Optional[int] = ..., status: _Optional[_Union[Status, _Mapping]] = ..., numberOfDefinitions: _Optional[int] = ..., symbol: _Optional[str] = ..., marketId: _Optional[int] = ..., exchange: _Optional[str] = ..., channelId: _Optional[int] = ..., exchangeId: _Optional[int] = ...) -> None: ...

class InstrumentReferenceRequest(_message.Message):
    __slots__ = ["correlationId", "token", "symbol", "marketId", "exchange", "channelId"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    token: str
    symbol: str
    marketId: int
    exchange: str
    channelId: int
    def __init__(self, correlationId: _Optional[int] = ..., token: _Optional[str] = ..., symbol: _Optional[str] = ..., marketId: _Optional[int] = ..., exchange: _Optional[str] = ..., channelId: _Optional[int] = ...) -> None: ...

class InstrumentReferenceResponse(_message.Message):
    __slots__ = ["correlationId", "status", "numberOfDefinitions", "channelId", "marketId", "symbol", "exchange", "ddfSymbol", "ddfExchange", "ddfBaseCode", "exchangeSymbol", "exchangeId"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    DDFSYMBOL_FIELD_NUMBER: _ClassVar[int]
    DDFEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    DDFBASECODE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGESYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEID_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    status: Status
    numberOfDefinitions: int
    channelId: int
    marketId: int
    symbol: str
    exchange: str
    ddfSymbol: str
    ddfExchange: str
    ddfBaseCode: str
    exchangeSymbol: str
    exchangeId: int
    def __init__(self, correlationId: _Optional[int] = ..., status: _Optional[_Union[Status, _Mapping]] = ..., numberOfDefinitions: _Optional[int] = ..., channelId: _Optional[int] = ..., marketId: _Optional[int] = ..., symbol: _Optional[str] = ..., exchange: _Optional[str] = ..., ddfSymbol: _Optional[str] = ..., ddfExchange: _Optional[str] = ..., ddfBaseCode: _Optional[str] = ..., exchangeSymbol: _Optional[str] = ..., exchangeId: _Optional[int] = ...) -> None: ...

class ExchangeRequest(_message.Message):
    __slots__ = ["correlationId", "token"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    token: str
    def __init__(self, correlationId: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class ExchangeResponse(_message.Message):
    __slots__ = ["correlationId", "status", "exchanges"]
    class Exchange(_message.Message):
        __slots__ = ["code", "description", "aliases", "exchangeId"]
        CODE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ALIASES_FIELD_NUMBER: _ClassVar[int]
        EXCHANGEID_FIELD_NUMBER: _ClassVar[int]
        code: str
        description: str
        aliases: _containers.RepeatedScalarFieldContainer[str]
        exchangeId: int
        def __init__(self, code: _Optional[str] = ..., description: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ..., exchangeId: _Optional[int] = ...) -> None: ...
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    status: Status
    exchanges: _containers.RepeatedCompositeFieldContainer[ExchangeResponse.Exchange]
    def __init__(self, correlationId: _Optional[int] = ..., status: _Optional[_Union[Status, _Mapping]] = ..., exchanges: _Optional[_Iterable[_Union[ExchangeResponse.Exchange, _Mapping]]] = ...) -> None: ...

class BulkSubscriptionFilter(_message.Message):
    __slots__ = ["symbolType", "symbolPattern"]
    SYMBOLTYPE_FIELD_NUMBER: _ClassVar[int]
    SYMBOLPATTERN_FIELD_NUMBER: _ClassVar[int]
    symbolType: SymbolType
    symbolPattern: str
    def __init__(self, symbolType: _Optional[_Union[SymbolType, str]] = ..., symbolPattern: _Optional[str] = ...) -> None: ...

class SubscriptionRequest(_message.Message):
    __slots__ = ["correlationId", "token", "service", "unsubscribe", "requests"]
    class Request(_message.Message):
        __slots__ = ["symbol", "marketId", "exchange", "channelId", "subscriptionType", "snapshotIntervalSeconds", "instrumentType", "bulkSubscriptionFilter", "spreadTypeFilter"]
        SYMBOL_FIELD_NUMBER: _ClassVar[int]
        MARKETID_FIELD_NUMBER: _ClassVar[int]
        EXCHANGE_FIELD_NUMBER: _ClassVar[int]
        CHANNELID_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOTINTERVALSECONDS_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENTTYPE_FIELD_NUMBER: _ClassVar[int]
        BULKSUBSCRIPTIONFILTER_FIELD_NUMBER: _ClassVar[int]
        SPREADTYPEFILTER_FIELD_NUMBER: _ClassVar[int]
        symbol: str
        marketId: int
        exchange: str
        channelId: int
        subscriptionType: _containers.RepeatedScalarFieldContainer[SubscriptionType]
        snapshotIntervalSeconds: int
        instrumentType: _containers.RepeatedScalarFieldContainer[_openfeed_instrument_pb2.InstrumentDefinition.InstrumentType]
        bulkSubscriptionFilter: _containers.RepeatedCompositeFieldContainer[BulkSubscriptionFilter]
        spreadTypeFilter: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, symbol: _Optional[str] = ..., marketId: _Optional[int] = ..., exchange: _Optional[str] = ..., channelId: _Optional[int] = ..., subscriptionType: _Optional[_Iterable[_Union[SubscriptionType, str]]] = ..., snapshotIntervalSeconds: _Optional[int] = ..., instrumentType: _Optional[_Iterable[_Union[_openfeed_instrument_pb2.InstrumentDefinition.InstrumentType, str]]] = ..., bulkSubscriptionFilter: _Optional[_Iterable[_Union[BulkSubscriptionFilter, _Mapping]]] = ..., spreadTypeFilter: _Optional[_Iterable[str]] = ...) -> None: ...
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    token: str
    service: _openfeed_pb2.Service
    unsubscribe: bool
    requests: _containers.RepeatedCompositeFieldContainer[SubscriptionRequest.Request]
    def __init__(self, correlationId: _Optional[int] = ..., token: _Optional[str] = ..., service: _Optional[_Union[_openfeed_pb2.Service, str]] = ..., unsubscribe: bool = ..., requests: _Optional[_Iterable[_Union[SubscriptionRequest.Request, _Mapping]]] = ...) -> None: ...

class SubscriptionResponse(_message.Message):
    __slots__ = ["correlationId", "status", "symbol", "marketId", "exchange", "channelId", "numberOfDefinitions", "subscriptionType", "unsubscribe", "snapshotIntervalSeconds"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTINTERVALSECONDS_FIELD_NUMBER: _ClassVar[int]
    correlationId: int
    status: Status
    symbol: str
    marketId: int
    exchange: str
    channelId: int
    numberOfDefinitions: int
    subscriptionType: SubscriptionType
    unsubscribe: bool
    snapshotIntervalSeconds: int
    def __init__(self, correlationId: _Optional[int] = ..., status: _Optional[_Union[Status, _Mapping]] = ..., symbol: _Optional[str] = ..., marketId: _Optional[int] = ..., exchange: _Optional[str] = ..., channelId: _Optional[int] = ..., numberOfDefinitions: _Optional[int] = ..., subscriptionType: _Optional[_Union[SubscriptionType, str]] = ..., unsubscribe: bool = ..., snapshotIntervalSeconds: _Optional[int] = ...) -> None: ...
