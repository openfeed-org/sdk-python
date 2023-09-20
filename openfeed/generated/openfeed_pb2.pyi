import openfeed_instrument_pb2 as _openfeed_instrument_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookSide(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_BOOK_SIDE: _ClassVar[BookSide]
    BID: _ClassVar[BookSide]
    OFFER: _ClassVar[BookSide]

class InstrumentTradingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_TRADING_STATUS: _ClassVar[InstrumentTradingStatus]
    TRADING_RESUME: _ClassVar[InstrumentTradingStatus]
    PRE_OPEN: _ClassVar[InstrumentTradingStatus]
    OPEN: _ClassVar[InstrumentTradingStatus]
    PRE_CLOSE: _ClassVar[InstrumentTradingStatus]
    CLOSE: _ClassVar[InstrumentTradingStatus]
    TRADING_HALT: _ClassVar[InstrumentTradingStatus]
    QUOTATION_RESUME: _ClassVar[InstrumentTradingStatus]
    OPEN_DELAY: _ClassVar[InstrumentTradingStatus]
    NO_OPEN_NO_RESUME: _ClassVar[InstrumentTradingStatus]
    FAST_MARKET: _ClassVar[InstrumentTradingStatus]
    FAST_MARKET_END: _ClassVar[InstrumentTradingStatus]
    LATE_MARKET: _ClassVar[InstrumentTradingStatus]
    LATE_MARKET_END: _ClassVar[InstrumentTradingStatus]
    POST_SESSION: _ClassVar[InstrumentTradingStatus]
    POST_SESSION_END: _ClassVar[InstrumentTradingStatus]
    NEW_PRICE_INDICATION: _ClassVar[InstrumentTradingStatus]
    NOT_AVAILABLE_FOR_TRADING: _ClassVar[InstrumentTradingStatus]
    PRE_CROSS: _ClassVar[InstrumentTradingStatus]
    CROSS: _ClassVar[InstrumentTradingStatus]
    POST_CLOSE: _ClassVar[InstrumentTradingStatus]
    NO_CHANGE: _ClassVar[InstrumentTradingStatus]
    NAFT: _ClassVar[InstrumentTradingStatus]
    TRADING_RANGE_INDICATION: _ClassVar[InstrumentTradingStatus]
    MARKET_IMBALANCE_BUY: _ClassVar[InstrumentTradingStatus]
    MARKET_IMBALANCE_SELL: _ClassVar[InstrumentTradingStatus]
    MOC_IMBALANCE_BUY: _ClassVar[InstrumentTradingStatus]
    MOC_IMBALANCE_SELL: _ClassVar[InstrumentTradingStatus]
    NO_MARKET_IMBALANCE: _ClassVar[InstrumentTradingStatus]
    NO_MOC_IMBALANCE: _ClassVar[InstrumentTradingStatus]
    SHORT_SELL_RESTRICTION: _ClassVar[InstrumentTradingStatus]
    LIMIT_UP_LIMIT_DOWN: _ClassVar[InstrumentTradingStatus]

class RegulationSHOShortSalePriceTest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_PRICE_TEST: _ClassVar[RegulationSHOShortSalePriceTest]
    PRICE_TEST_NONE: _ClassVar[RegulationSHOShortSalePriceTest]
    PRICE_TEST_IN_EFFECT: _ClassVar[RegulationSHOShortSalePriceTest]
    PRICE_TEST_REMAINS_IN_EFFECT: _ClassVar[RegulationSHOShortSalePriceTest]

class SettlementTerms(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_SETTLEMENT_TERMS: _ClassVar[SettlementTerms]
    CASH: _ClassVar[SettlementTerms]
    NON_NET: _ClassVar[SettlementTerms]
    CONTINGENT_TRADE: _ClassVar[SettlementTerms]
    CASH_TODAY: _ClassVar[SettlementTerms]
    DATE: _ClassVar[SettlementTerms]

class CrossType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_CROSS_TYPE: _ClassVar[CrossType]
    DEFAULT: _ClassVar[CrossType]
    INTERNAL: _ClassVar[CrossType]
    BASIS: _ClassVar[CrossType]
    CONTINGENT: _ClassVar[CrossType]
    SPECIAL: _ClassVar[CrossType]
    VWAP: _ClassVar[CrossType]
    REGULAR: _ClassVar[CrossType]

class OpenCloseSettlementFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[OpenCloseSettlementFlag]
    DAILY_OPEN: _ClassVar[OpenCloseSettlementFlag]
    INDICATIVE_OPEN_PRICE: _ClassVar[OpenCloseSettlementFlag]

class SettlementSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_SETTLEMENT_SOURCE: _ClassVar[SettlementSource]
    GLOBEX: _ClassVar[SettlementSource]
    ITC: _ClassVar[SettlementSource]
    MANUAL: _ClassVar[SettlementSource]

class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_SERVICE: _ClassVar[Service]
    REAL_TIME: _ClassVar[Service]
    DELAYED: _ClassVar[Service]
    REAL_TIME_SNAPSHOT: _ClassVar[Service]
    DELAYED_SNAPSHOT: _ClassVar[Service]
    END_OF_DAY: _ClassVar[Service]

class MarketWideStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STATUS_UNKNOWN: _ClassVar[MarketWideStatus]
    STATUS_START_OF_DAY: _ClassVar[MarketWideStatus]
    STATUS_END_OF_DAY: _ClassVar[MarketWideStatus]
    STATUS_OPEN: _ClassVar[MarketWideStatus]
    STATUS_CLOSE: _ClassVar[MarketWideStatus]

class SnapshotRequestResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SNAPSHOT_REQUEST_UNKNOWN_RESULT: _ClassVar[SnapshotRequestResult]
    SNAPSHOT_REQUEST_SUCCESS: _ClassVar[SnapshotRequestResult]
    SNAPSHOT_REQUEST_NOT_FOUND: _ClassVar[SnapshotRequestResult]
    SNAPSHOT_REQUEST_SERVICE_NOT_AVAILABLE: _ClassVar[SnapshotRequestResult]
    SNAPSHOT_REQUEST_GENERIC_FAILURE: _ClassVar[SnapshotRequestResult]

class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_ACTION: _ClassVar[ActionType]
    LISTING: _ClassVar[ActionType]
    DELISTING: _ClassVar[ActionType]
    EXCHANGE_MOVE: _ClassVar[ActionType]
UNKNOWN_BOOK_SIDE: BookSide
BID: BookSide
OFFER: BookSide
UNKNOWN_TRADING_STATUS: InstrumentTradingStatus
TRADING_RESUME: InstrumentTradingStatus
PRE_OPEN: InstrumentTradingStatus
OPEN: InstrumentTradingStatus
PRE_CLOSE: InstrumentTradingStatus
CLOSE: InstrumentTradingStatus
TRADING_HALT: InstrumentTradingStatus
QUOTATION_RESUME: InstrumentTradingStatus
OPEN_DELAY: InstrumentTradingStatus
NO_OPEN_NO_RESUME: InstrumentTradingStatus
FAST_MARKET: InstrumentTradingStatus
FAST_MARKET_END: InstrumentTradingStatus
LATE_MARKET: InstrumentTradingStatus
LATE_MARKET_END: InstrumentTradingStatus
POST_SESSION: InstrumentTradingStatus
POST_SESSION_END: InstrumentTradingStatus
NEW_PRICE_INDICATION: InstrumentTradingStatus
NOT_AVAILABLE_FOR_TRADING: InstrumentTradingStatus
PRE_CROSS: InstrumentTradingStatus
CROSS: InstrumentTradingStatus
POST_CLOSE: InstrumentTradingStatus
NO_CHANGE: InstrumentTradingStatus
NAFT: InstrumentTradingStatus
TRADING_RANGE_INDICATION: InstrumentTradingStatus
MARKET_IMBALANCE_BUY: InstrumentTradingStatus
MARKET_IMBALANCE_SELL: InstrumentTradingStatus
MOC_IMBALANCE_BUY: InstrumentTradingStatus
MOC_IMBALANCE_SELL: InstrumentTradingStatus
NO_MARKET_IMBALANCE: InstrumentTradingStatus
NO_MOC_IMBALANCE: InstrumentTradingStatus
SHORT_SELL_RESTRICTION: InstrumentTradingStatus
LIMIT_UP_LIMIT_DOWN: InstrumentTradingStatus
UNKNOWN_PRICE_TEST: RegulationSHOShortSalePriceTest
PRICE_TEST_NONE: RegulationSHOShortSalePriceTest
PRICE_TEST_IN_EFFECT: RegulationSHOShortSalePriceTest
PRICE_TEST_REMAINS_IN_EFFECT: RegulationSHOShortSalePriceTest
UNKNOWN_SETTLEMENT_TERMS: SettlementTerms
CASH: SettlementTerms
NON_NET: SettlementTerms
CONTINGENT_TRADE: SettlementTerms
CASH_TODAY: SettlementTerms
DATE: SettlementTerms
UNKNOWN_CROSS_TYPE: CrossType
DEFAULT: CrossType
INTERNAL: CrossType
BASIS: CrossType
CONTINGENT: CrossType
SPECIAL: CrossType
VWAP: CrossType
REGULAR: CrossType
UNKNOWN: OpenCloseSettlementFlag
DAILY_OPEN: OpenCloseSettlementFlag
INDICATIVE_OPEN_PRICE: OpenCloseSettlementFlag
UNKNOWN_SETTLEMENT_SOURCE: SettlementSource
GLOBEX: SettlementSource
ITC: SettlementSource
MANUAL: SettlementSource
UNKNOWN_SERVICE: Service
REAL_TIME: Service
DELAYED: Service
REAL_TIME_SNAPSHOT: Service
DELAYED_SNAPSHOT: Service
END_OF_DAY: Service
STATUS_UNKNOWN: MarketWideStatus
STATUS_START_OF_DAY: MarketWideStatus
STATUS_END_OF_DAY: MarketWideStatus
STATUS_OPEN: MarketWideStatus
STATUS_CLOSE: MarketWideStatus
SNAPSHOT_REQUEST_UNKNOWN_RESULT: SnapshotRequestResult
SNAPSHOT_REQUEST_SUCCESS: SnapshotRequestResult
SNAPSHOT_REQUEST_NOT_FOUND: SnapshotRequestResult
SNAPSHOT_REQUEST_SERVICE_NOT_AVAILABLE: SnapshotRequestResult
SNAPSHOT_REQUEST_GENERIC_FAILURE: SnapshotRequestResult
UNKNOWN_ACTION: ActionType
LISTING: ActionType
DELISTING: ActionType
EXCHANGE_MOVE: ActionType

class OpenfeedMessage(_message.Message):
    __slots__ = ["sendingTime", "totalCount", "syncSequence", "context", "channelReset", "heartBeat", "adminMessage", "instrumentDefinition", "instrumentGroupStatus", "marketSnapshot", "marketUpdate", "marketStatus", "eodCommoditySummary", "instrumentAction"]
    SENDINGTIME_FIELD_NUMBER: _ClassVar[int]
    TOTALCOUNT_FIELD_NUMBER: _ClassVar[int]
    SYNCSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CHANNELRESET_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    ADMINMESSAGE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTDEFINITION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTGROUPSTATUS_FIELD_NUMBER: _ClassVar[int]
    MARKETSNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    MARKETUPDATE_FIELD_NUMBER: _ClassVar[int]
    MARKETSTATUS_FIELD_NUMBER: _ClassVar[int]
    EODCOMMODITYSUMMARY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTACTION_FIELD_NUMBER: _ClassVar[int]
    sendingTime: int
    totalCount: int
    syncSequence: int
    context: Context
    channelReset: ChannelReset
    heartBeat: HeartBeat
    adminMessage: AdminMessage
    instrumentDefinition: _openfeed_instrument_pb2.InstrumentDefinition
    instrumentGroupStatus: InstrumentGroupStatus
    marketSnapshot: MarketSnapshot
    marketUpdate: MarketUpdate
    marketStatus: MarketStatus
    eodCommoditySummary: EODCommoditySummary
    instrumentAction: InstrumentAction
    def __init__(self, sendingTime: _Optional[int] = ..., totalCount: _Optional[int] = ..., syncSequence: _Optional[int] = ..., context: _Optional[_Union[Context, _Mapping]] = ..., channelReset: _Optional[_Union[ChannelReset, _Mapping]] = ..., heartBeat: _Optional[_Union[HeartBeat, _Mapping]] = ..., adminMessage: _Optional[_Union[AdminMessage, _Mapping]] = ..., instrumentDefinition: _Optional[_Union[_openfeed_instrument_pb2.InstrumentDefinition, _Mapping]] = ..., instrumentGroupStatus: _Optional[_Union[InstrumentGroupStatus, _Mapping]] = ..., marketSnapshot: _Optional[_Union[MarketSnapshot, _Mapping]] = ..., marketUpdate: _Optional[_Union[MarketUpdate, _Mapping]] = ..., marketStatus: _Optional[_Union[MarketStatus, _Mapping]] = ..., eodCommoditySummary: _Optional[_Union[EODCommoditySummary, _Mapping]] = ..., instrumentAction: _Optional[_Union[InstrumentAction, _Mapping]] = ...) -> None: ...

class ChannelReset(_message.Message):
    __slots__ = ["channel", "transactionTime"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    channel: int
    transactionTime: int
    def __init__(self, channel: _Optional[int] = ..., transactionTime: _Optional[int] = ...) -> None: ...

class HeartBeat(_message.Message):
    __slots__ = ["transactionTime", "status", "exchange", "channel"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    status: str
    exchange: bool
    channel: int
    def __init__(self, transactionTime: _Optional[int] = ..., status: _Optional[str] = ..., exchange: bool = ..., channel: _Optional[int] = ...) -> None: ...

class AdminMessage(_message.Message):
    __slots__ = ["originationTime", "source", "languageCode", "headLine", "text", "status", "channel"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        OK: _ClassVar[AdminMessage.Status]
    OK: AdminMessage.Status
    ORIGINATIONTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    originationTime: int
    source: str
    languageCode: str
    headLine: str
    text: str
    status: AdminMessage.Status
    channel: int
    def __init__(self, originationTime: _Optional[int] = ..., source: _Optional[str] = ..., languageCode: _Optional[str] = ..., headLine: _Optional[str] = ..., text: _Optional[str] = ..., status: _Optional[_Union[AdminMessage.Status, str]] = ..., channel: _Optional[int] = ...) -> None: ...

class InstrumentGroupStatus(_message.Message):
    __slots__ = ["transactionTime", "instrumentGroupId", "tradingStatus", "tradeDate", "channel"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTGROUPID_FIELD_NUMBER: _ClassVar[int]
    TRADINGSTATUS_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    instrumentGroupId: str
    tradingStatus: InstrumentTradingStatus
    tradeDate: int
    channel: int
    def __init__(self, transactionTime: _Optional[int] = ..., instrumentGroupId: _Optional[str] = ..., tradingStatus: _Optional[_Union[InstrumentTradingStatus, str]] = ..., tradeDate: _Optional[int] = ..., channel: _Optional[int] = ...) -> None: ...

class MarketStatus(_message.Message):
    __slots__ = ["transactionTime", "channel", "marketWideStatus"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    MARKETWIDESTATUS_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    channel: int
    marketWideStatus: MarketWideStatus
    def __init__(self, transactionTime: _Optional[int] = ..., channel: _Optional[int] = ..., marketWideStatus: _Optional[_Union[MarketWideStatus, str]] = ...) -> None: ...

class EODCommoditySummary(_message.Message):
    __slots__ = ["tradeDate", "contractRoot", "consolidatedVolume", "consolidatedOpenInterest", "auxiliaryData"]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTROOT_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATEDVOLUME_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATEDOPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    AUXILIARYDATA_FIELD_NUMBER: _ClassVar[int]
    tradeDate: int
    contractRoot: str
    consolidatedVolume: int
    consolidatedOpenInterest: int
    auxiliaryData: bytes
    def __init__(self, tradeDate: _Optional[int] = ..., contractRoot: _Optional[str] = ..., consolidatedVolume: _Optional[int] = ..., consolidatedOpenInterest: _Optional[int] = ..., auxiliaryData: _Optional[bytes] = ...) -> None: ...

class MarketSession(_message.Message):
    __slots__ = ["tradeDate", "open", "high", "low", "last", "volume", "settlement", "prevSettlement", "openInterest", "numberOfTrades", "monetaryValue", "transactionTime"]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    PREVSETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFTRADES_FIELD_NUMBER: _ClassVar[int]
    MONETARYVALUE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    tradeDate: int
    open: Open
    high: High
    low: Low
    last: Last
    volume: Volume
    settlement: Settlement
    prevSettlement: Settlement
    openInterest: OpenInterest
    numberOfTrades: NumberOfTrades
    monetaryValue: MonetaryValue
    transactionTime: int
    def __init__(self, tradeDate: _Optional[int] = ..., open: _Optional[_Union[Open, _Mapping]] = ..., high: _Optional[_Union[High, _Mapping]] = ..., low: _Optional[_Union[Low, _Mapping]] = ..., last: _Optional[_Union[Last, _Mapping]] = ..., volume: _Optional[_Union[Volume, _Mapping]] = ..., settlement: _Optional[_Union[Settlement, _Mapping]] = ..., prevSettlement: _Optional[_Union[Settlement, _Mapping]] = ..., openInterest: _Optional[_Union[OpenInterest, _Mapping]] = ..., numberOfTrades: _Optional[_Union[NumberOfTrades, _Mapping]] = ..., monetaryValue: _Optional[_Union[MonetaryValue, _Mapping]] = ..., transactionTime: _Optional[int] = ...) -> None: ...

class MarketSnapshot(_message.Message):
    __slots__ = ["marketId", "transactionTime", "marketSequence", "tradeDate", "totalChunks", "currentChunk", "symbol", "priceDenominator", "service", "instrumentStatus", "bbo", "index", "priceLevels", "orders", "news", "open", "high", "low", "close", "prevClose", "last", "yearHigh", "yearLow", "volume", "settlement", "openInterest", "vwap", "dividendsIncomeDistributions", "numberOfTrades", "monetaryValue", "capitalDistributions", "sharesOutstanding", "netAssetValue", "previousSession", "tSession", "volumeAtPrice", "highRolling", "lowRolling", "zSession"]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    MARKETSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    TOTALCHUNKS_FIELD_NUMBER: _ClassVar[int]
    CURRENTCHUNK_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    PRICEDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTSTATUS_FIELD_NUMBER: _ClassVar[int]
    BBO_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PRICELEVELS_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    NEWS_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    PREVCLOSE_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    YEARHIGH_FIELD_NUMBER: _ClassVar[int]
    YEARLOW_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    VWAP_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDSINCOMEDISTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFTRADES_FIELD_NUMBER: _ClassVar[int]
    MONETARYVALUE_FIELD_NUMBER: _ClassVar[int]
    CAPITALDISTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    SHARESOUTSTANDING_FIELD_NUMBER: _ClassVar[int]
    NETASSETVALUE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSSESSION_FIELD_NUMBER: _ClassVar[int]
    TSESSION_FIELD_NUMBER: _ClassVar[int]
    VOLUMEATPRICE_FIELD_NUMBER: _ClassVar[int]
    HIGHROLLING_FIELD_NUMBER: _ClassVar[int]
    LOWROLLING_FIELD_NUMBER: _ClassVar[int]
    ZSESSION_FIELD_NUMBER: _ClassVar[int]
    marketId: int
    transactionTime: int
    marketSequence: int
    tradeDate: int
    totalChunks: int
    currentChunk: int
    symbol: str
    priceDenominator: int
    service: Service
    instrumentStatus: InstrumentStatus
    bbo: BestBidOffer
    index: IndexValue
    priceLevels: _containers.RepeatedCompositeFieldContainer[AddPriceLevel]
    orders: _containers.RepeatedCompositeFieldContainer[AddOrder]
    news: News
    open: Open
    high: High
    low: Low
    close: Close
    prevClose: PrevClose
    last: Last
    yearHigh: YearHigh
    yearLow: YearLow
    volume: Volume
    settlement: Settlement
    openInterest: OpenInterest
    vwap: Vwap
    dividendsIncomeDistributions: DividendsIncomeDistributions
    numberOfTrades: NumberOfTrades
    monetaryValue: MonetaryValue
    capitalDistributions: CapitalDistributions
    sharesOutstanding: SharesOutstanding
    netAssetValue: NetAssetValue
    previousSession: MarketSession
    tSession: MarketSession
    volumeAtPrice: VolumeAtPrice
    highRolling: HighRolling
    lowRolling: LowRolling
    zSession: MarketSession
    def __init__(self, marketId: _Optional[int] = ..., transactionTime: _Optional[int] = ..., marketSequence: _Optional[int] = ..., tradeDate: _Optional[int] = ..., totalChunks: _Optional[int] = ..., currentChunk: _Optional[int] = ..., symbol: _Optional[str] = ..., priceDenominator: _Optional[int] = ..., service: _Optional[_Union[Service, str]] = ..., instrumentStatus: _Optional[_Union[InstrumentStatus, _Mapping]] = ..., bbo: _Optional[_Union[BestBidOffer, _Mapping]] = ..., index: _Optional[_Union[IndexValue, _Mapping]] = ..., priceLevels: _Optional[_Iterable[_Union[AddPriceLevel, _Mapping]]] = ..., orders: _Optional[_Iterable[_Union[AddOrder, _Mapping]]] = ..., news: _Optional[_Union[News, _Mapping]] = ..., open: _Optional[_Union[Open, _Mapping]] = ..., high: _Optional[_Union[High, _Mapping]] = ..., low: _Optional[_Union[Low, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., prevClose: _Optional[_Union[PrevClose, _Mapping]] = ..., last: _Optional[_Union[Last, _Mapping]] = ..., yearHigh: _Optional[_Union[YearHigh, _Mapping]] = ..., yearLow: _Optional[_Union[YearLow, _Mapping]] = ..., volume: _Optional[_Union[Volume, _Mapping]] = ..., settlement: _Optional[_Union[Settlement, _Mapping]] = ..., openInterest: _Optional[_Union[OpenInterest, _Mapping]] = ..., vwap: _Optional[_Union[Vwap, _Mapping]] = ..., dividendsIncomeDistributions: _Optional[_Union[DividendsIncomeDistributions, _Mapping]] = ..., numberOfTrades: _Optional[_Union[NumberOfTrades, _Mapping]] = ..., monetaryValue: _Optional[_Union[MonetaryValue, _Mapping]] = ..., capitalDistributions: _Optional[_Union[CapitalDistributions, _Mapping]] = ..., sharesOutstanding: _Optional[_Union[SharesOutstanding, _Mapping]] = ..., netAssetValue: _Optional[_Union[NetAssetValue, _Mapping]] = ..., previousSession: _Optional[_Union[MarketSession, _Mapping]] = ..., tSession: _Optional[_Union[MarketSession, _Mapping]] = ..., volumeAtPrice: _Optional[_Union[VolumeAtPrice, _Mapping]] = ..., highRolling: _Optional[_Union[HighRolling, _Mapping]] = ..., lowRolling: _Optional[_Union[LowRolling, _Mapping]] = ..., zSession: _Optional[_Union[MarketSession, _Mapping]] = ...) -> None: ...

class MarketSnapshotResponse(_message.Message):
    __slots__ = ["result", "message", "marketSnapshot"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MARKETSNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    result: SnapshotRequestResult
    message: str
    marketSnapshot: MarketSnapshot
    def __init__(self, result: _Optional[_Union[SnapshotRequestResult, str]] = ..., message: _Optional[str] = ..., marketSnapshot: _Optional[_Union[MarketSnapshot, _Mapping]] = ...) -> None: ...

class MarketUpdate(_message.Message):
    __slots__ = ["marketId", "symbol", "transactionTime", "distributionTime", "marketSequence", "sourceSequence", "originatorId", "priceDenominator", "context", "session", "tSession", "previousSession", "regional", "zSession", "news", "clearBook", "instrumentStatus", "bbo", "depthPriceLevel", "depthOrder", "index", "trades", "open", "high", "low", "close", "prevClose", "last", "yearHigh", "yearLow", "volume", "settlement", "openInterest", "vwap", "dividendsIncomeDistributions", "numberOfTrades", "monetaryValue", "capitalDistributions", "sharesOutstanding", "netAssetValue", "marketSummary", "highRolling", "lowRolling", "requestForQuote"]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTIONTIME_FIELD_NUMBER: _ClassVar[int]
    MARKETSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SOURCESEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ORIGINATORID_FIELD_NUMBER: _ClassVar[int]
    PRICEDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TSESSION_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSSESSION_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_FIELD_NUMBER: _ClassVar[int]
    ZSESSION_FIELD_NUMBER: _ClassVar[int]
    NEWS_FIELD_NUMBER: _ClassVar[int]
    CLEARBOOK_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTSTATUS_FIELD_NUMBER: _ClassVar[int]
    BBO_FIELD_NUMBER: _ClassVar[int]
    DEPTHPRICELEVEL_FIELD_NUMBER: _ClassVar[int]
    DEPTHORDER_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    PREVCLOSE_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    YEARHIGH_FIELD_NUMBER: _ClassVar[int]
    YEARLOW_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    VWAP_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDSINCOMEDISTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFTRADES_FIELD_NUMBER: _ClassVar[int]
    MONETARYVALUE_FIELD_NUMBER: _ClassVar[int]
    CAPITALDISTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    SHARESOUTSTANDING_FIELD_NUMBER: _ClassVar[int]
    NETASSETVALUE_FIELD_NUMBER: _ClassVar[int]
    MARKETSUMMARY_FIELD_NUMBER: _ClassVar[int]
    HIGHROLLING_FIELD_NUMBER: _ClassVar[int]
    LOWROLLING_FIELD_NUMBER: _ClassVar[int]
    REQUESTFORQUOTE_FIELD_NUMBER: _ClassVar[int]
    marketId: int
    symbol: str
    transactionTime: int
    distributionTime: int
    marketSequence: int
    sourceSequence: int
    originatorId: bytes
    priceDenominator: int
    context: Context
    session: MarketSession
    tSession: MarketSession
    previousSession: MarketSession
    regional: bool
    zSession: MarketSession
    news: News
    clearBook: ClearBook
    instrumentStatus: InstrumentStatus
    bbo: BestBidOffer
    depthPriceLevel: DepthPriceLevel
    depthOrder: DepthOrder
    index: IndexValue
    trades: Trades
    open: Open
    high: High
    low: Low
    close: Close
    prevClose: PrevClose
    last: Last
    yearHigh: YearHigh
    yearLow: YearLow
    volume: Volume
    settlement: Settlement
    openInterest: OpenInterest
    vwap: Vwap
    dividendsIncomeDistributions: DividendsIncomeDistributions
    numberOfTrades: NumberOfTrades
    monetaryValue: MonetaryValue
    capitalDistributions: CapitalDistributions
    sharesOutstanding: SharesOutstanding
    netAssetValue: NetAssetValue
    marketSummary: MarketSummary
    highRolling: HighRolling
    lowRolling: LowRolling
    requestForQuote: RequestForQuote
    def __init__(self, marketId: _Optional[int] = ..., symbol: _Optional[str] = ..., transactionTime: _Optional[int] = ..., distributionTime: _Optional[int] = ..., marketSequence: _Optional[int] = ..., sourceSequence: _Optional[int] = ..., originatorId: _Optional[bytes] = ..., priceDenominator: _Optional[int] = ..., context: _Optional[_Union[Context, _Mapping]] = ..., session: _Optional[_Union[MarketSession, _Mapping]] = ..., tSession: _Optional[_Union[MarketSession, _Mapping]] = ..., previousSession: _Optional[_Union[MarketSession, _Mapping]] = ..., regional: bool = ..., zSession: _Optional[_Union[MarketSession, _Mapping]] = ..., news: _Optional[_Union[News, _Mapping]] = ..., clearBook: _Optional[_Union[ClearBook, _Mapping]] = ..., instrumentStatus: _Optional[_Union[InstrumentStatus, _Mapping]] = ..., bbo: _Optional[_Union[BestBidOffer, _Mapping]] = ..., depthPriceLevel: _Optional[_Union[DepthPriceLevel, _Mapping]] = ..., depthOrder: _Optional[_Union[DepthOrder, _Mapping]] = ..., index: _Optional[_Union[IndexValue, _Mapping]] = ..., trades: _Optional[_Union[Trades, _Mapping]] = ..., open: _Optional[_Union[Open, _Mapping]] = ..., high: _Optional[_Union[High, _Mapping]] = ..., low: _Optional[_Union[Low, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., prevClose: _Optional[_Union[PrevClose, _Mapping]] = ..., last: _Optional[_Union[Last, _Mapping]] = ..., yearHigh: _Optional[_Union[YearHigh, _Mapping]] = ..., yearLow: _Optional[_Union[YearLow, _Mapping]] = ..., volume: _Optional[_Union[Volume, _Mapping]] = ..., settlement: _Optional[_Union[Settlement, _Mapping]] = ..., openInterest: _Optional[_Union[OpenInterest, _Mapping]] = ..., vwap: _Optional[_Union[Vwap, _Mapping]] = ..., dividendsIncomeDistributions: _Optional[_Union[DividendsIncomeDistributions, _Mapping]] = ..., numberOfTrades: _Optional[_Union[NumberOfTrades, _Mapping]] = ..., monetaryValue: _Optional[_Union[MonetaryValue, _Mapping]] = ..., capitalDistributions: _Optional[_Union[CapitalDistributions, _Mapping]] = ..., sharesOutstanding: _Optional[_Union[SharesOutstanding, _Mapping]] = ..., netAssetValue: _Optional[_Union[NetAssetValue, _Mapping]] = ..., marketSummary: _Optional[_Union[MarketSummary, _Mapping]] = ..., highRolling: _Optional[_Union[HighRolling, _Mapping]] = ..., lowRolling: _Optional[_Union[LowRolling, _Mapping]] = ..., requestForQuote: _Optional[_Union[RequestForQuote, _Mapping]] = ...) -> None: ...

class DepthPriceLevel(_message.Message):
    __slots__ = ["levels"]
    class Entry(_message.Message):
        __slots__ = ["addPriceLevel", "deletePriceLevel", "modifyPriceLevel"]
        ADDPRICELEVEL_FIELD_NUMBER: _ClassVar[int]
        DELETEPRICELEVEL_FIELD_NUMBER: _ClassVar[int]
        MODIFYPRICELEVEL_FIELD_NUMBER: _ClassVar[int]
        addPriceLevel: AddPriceLevel
        deletePriceLevel: DeletePriceLevel
        modifyPriceLevel: ModifyPriceLevel
        def __init__(self, addPriceLevel: _Optional[_Union[AddPriceLevel, _Mapping]] = ..., deletePriceLevel: _Optional[_Union[DeletePriceLevel, _Mapping]] = ..., modifyPriceLevel: _Optional[_Union[ModifyPriceLevel, _Mapping]] = ...) -> None: ...
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedCompositeFieldContainer[DepthPriceLevel.Entry]
    def __init__(self, levels: _Optional[_Iterable[_Union[DepthPriceLevel.Entry, _Mapping]]] = ...) -> None: ...

class DepthOrder(_message.Message):
    __slots__ = ["orders"]
    class Entry(_message.Message):
        __slots__ = ["addOrder", "deleteOrder", "modifyOrder"]
        ADDORDER_FIELD_NUMBER: _ClassVar[int]
        DELETEORDER_FIELD_NUMBER: _ClassVar[int]
        MODIFYORDER_FIELD_NUMBER: _ClassVar[int]
        addOrder: AddOrder
        deleteOrder: DeleteOrder
        modifyOrder: ModifyOrder
        def __init__(self, addOrder: _Optional[_Union[AddOrder, _Mapping]] = ..., deleteOrder: _Optional[_Union[DeleteOrder, _Mapping]] = ..., modifyOrder: _Optional[_Union[ModifyOrder, _Mapping]] = ...) -> None: ...
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[DepthOrder.Entry]
    def __init__(self, orders: _Optional[_Iterable[_Union[DepthOrder.Entry, _Mapping]]] = ...) -> None: ...

class News(_message.Message):
    __slots__ = ["originationTime", "source", "languageCode", "headLine", "text", "symbols"]
    ORIGINATIONTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    originationTime: int
    source: str
    languageCode: str
    headLine: str
    text: str
    symbols: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, originationTime: _Optional[int] = ..., source: _Optional[str] = ..., languageCode: _Optional[str] = ..., headLine: _Optional[str] = ..., text: _Optional[str] = ..., symbols: _Optional[_Iterable[str]] = ...) -> None: ...

class ClearBook(_message.Message):
    __slots__ = ["reserved", "transactionTime"]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    reserved: int
    transactionTime: int
    def __init__(self, reserved: _Optional[int] = ..., transactionTime: _Optional[int] = ...) -> None: ...

class InstrumentStatus(_message.Message):
    __slots__ = ["transactionTime", "tradingStatus", "openingTime", "note", "tradeDate", "regulationSHOShortSalePriceTest"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADINGSTATUS_FIELD_NUMBER: _ClassVar[int]
    OPENINGTIME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    REGULATIONSHOSHORTSALEPRICETEST_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradingStatus: InstrumentTradingStatus
    openingTime: int
    note: str
    tradeDate: int
    regulationSHOShortSalePriceTest: RegulationSHOShortSalePriceTest
    def __init__(self, transactionTime: _Optional[int] = ..., tradingStatus: _Optional[_Union[InstrumentTradingStatus, str]] = ..., openingTime: _Optional[int] = ..., note: _Optional[str] = ..., tradeDate: _Optional[int] = ..., regulationSHOShortSalePriceTest: _Optional[_Union[RegulationSHOShortSalePriceTest, str]] = ...) -> None: ...

class BestBidOffer(_message.Message):
    __slots__ = ["transactionTime", "bidPrice", "bidQuantity", "bidOrderCount", "bidOriginator", "bidQuoteCondition", "offerPrice", "offerQuantity", "offerOrderCount", "offerOriginator", "offerQuoteCondition", "quoteCondition", "regional", "transient"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    BIDPRICE_FIELD_NUMBER: _ClassVar[int]
    BIDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    BIDORDERCOUNT_FIELD_NUMBER: _ClassVar[int]
    BIDORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    BIDQUOTECONDITION_FIELD_NUMBER: _ClassVar[int]
    OFFERPRICE_FIELD_NUMBER: _ClassVar[int]
    OFFERQUANTITY_FIELD_NUMBER: _ClassVar[int]
    OFFERORDERCOUNT_FIELD_NUMBER: _ClassVar[int]
    OFFERORIGINATOR_FIELD_NUMBER: _ClassVar[int]
    OFFERQUOTECONDITION_FIELD_NUMBER: _ClassVar[int]
    QUOTECONDITION_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    bidPrice: int
    bidQuantity: int
    bidOrderCount: int
    bidOriginator: bytes
    bidQuoteCondition: bytes
    offerPrice: int
    offerQuantity: int
    offerOrderCount: int
    offerOriginator: bytes
    offerQuoteCondition: bytes
    quoteCondition: bytes
    regional: bool
    transient: bool
    def __init__(self, transactionTime: _Optional[int] = ..., bidPrice: _Optional[int] = ..., bidQuantity: _Optional[int] = ..., bidOrderCount: _Optional[int] = ..., bidOriginator: _Optional[bytes] = ..., bidQuoteCondition: _Optional[bytes] = ..., offerPrice: _Optional[int] = ..., offerQuantity: _Optional[int] = ..., offerOrderCount: _Optional[int] = ..., offerOriginator: _Optional[bytes] = ..., offerQuoteCondition: _Optional[bytes] = ..., quoteCondition: _Optional[bytes] = ..., regional: bool = ..., transient: bool = ...) -> None: ...

class AddPriceLevel(_message.Message):
    __slots__ = ["transactionTime", "level", "side", "price", "quantity", "orderCount", "impliedQuantity"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDERCOUNT_FIELD_NUMBER: _ClassVar[int]
    IMPLIEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    level: int
    side: BookSide
    price: int
    quantity: int
    orderCount: int
    impliedQuantity: int
    def __init__(self, transactionTime: _Optional[int] = ..., level: _Optional[int] = ..., side: _Optional[_Union[BookSide, str]] = ..., price: _Optional[int] = ..., quantity: _Optional[int] = ..., orderCount: _Optional[int] = ..., impliedQuantity: _Optional[int] = ...) -> None: ...

class DeletePriceLevel(_message.Message):
    __slots__ = ["transactionTime", "level", "side"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    level: int
    side: BookSide
    def __init__(self, transactionTime: _Optional[int] = ..., level: _Optional[int] = ..., side: _Optional[_Union[BookSide, str]] = ...) -> None: ...

class ModifyPriceLevel(_message.Message):
    __slots__ = ["transactionTime", "level", "side", "price", "quantity", "orderCount", "impliedQuantity"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDERCOUNT_FIELD_NUMBER: _ClassVar[int]
    IMPLIEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    level: int
    side: BookSide
    price: int
    quantity: int
    orderCount: int
    impliedQuantity: int
    def __init__(self, transactionTime: _Optional[int] = ..., level: _Optional[int] = ..., side: _Optional[_Union[BookSide, str]] = ..., price: _Optional[int] = ..., quantity: _Optional[int] = ..., orderCount: _Optional[int] = ..., impliedQuantity: _Optional[int] = ...) -> None: ...

class AddOrder(_message.Message):
    __slots__ = ["transactionTime", "orderId", "side", "price", "quantity", "isImplied", "priority"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ISIMPLIED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    orderId: int
    side: BookSide
    price: int
    quantity: int
    isImplied: bool
    priority: int
    def __init__(self, transactionTime: _Optional[int] = ..., orderId: _Optional[int] = ..., side: _Optional[_Union[BookSide, str]] = ..., price: _Optional[int] = ..., quantity: _Optional[int] = ..., isImplied: bool = ..., priority: _Optional[int] = ...) -> None: ...

class DeleteOrder(_message.Message):
    __slots__ = ["transactionTime", "orderId", "side"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    orderId: int
    side: BookSide
    def __init__(self, transactionTime: _Optional[int] = ..., orderId: _Optional[int] = ..., side: _Optional[_Union[BookSide, str]] = ...) -> None: ...

class ModifyOrder(_message.Message):
    __slots__ = ["transactionTime", "orderId", "side", "price", "quantity", "isImplied", "priority"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ISIMPLIED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    orderId: int
    side: BookSide
    price: int
    quantity: int
    isImplied: bool
    priority: int
    def __init__(self, transactionTime: _Optional[int] = ..., orderId: _Optional[int] = ..., side: _Optional[_Union[BookSide, str]] = ..., price: _Optional[int] = ..., quantity: _Optional[int] = ..., isImplied: bool = ..., priority: _Optional[int] = ...) -> None: ...

class IndexValue(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "last", "volume", "open", "settlementOpen", "specialOpen", "high", "low", "close", "bid", "offer"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENTOPEN_FIELD_NUMBER: _ClassVar[int]
    SPECIALOPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    BID_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    last: int
    volume: int
    open: int
    settlementOpen: int
    specialOpen: int
    high: int
    low: int
    close: int
    bid: int
    offer: int
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., last: _Optional[int] = ..., volume: _Optional[int] = ..., open: _Optional[int] = ..., settlementOpen: _Optional[int] = ..., specialOpen: _Optional[int] = ..., high: _Optional[int] = ..., low: _Optional[int] = ..., close: _Optional[int] = ..., bid: _Optional[int] = ..., offer: _Optional[int] = ...) -> None: ...

class Trades(_message.Message):
    __slots__ = ["trades"]
    class Entry(_message.Message):
        __slots__ = ["trade", "tradeCorrection", "tradeCancel"]
        TRADE_FIELD_NUMBER: _ClassVar[int]
        TRADECORRECTION_FIELD_NUMBER: _ClassVar[int]
        TRADECANCEL_FIELD_NUMBER: _ClassVar[int]
        trade: Trade
        tradeCorrection: TradeCorrection
        tradeCancel: TradeCancel
        def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ..., tradeCorrection: _Optional[_Union[TradeCorrection, _Mapping]] = ..., tradeCancel: _Optional[_Union[TradeCancel, _Mapping]] = ...) -> None: ...
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[Trades.Entry]
    def __init__(self, trades: _Optional[_Iterable[_Union[Trades.Entry, _Mapping]]] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ["originatorId", "transactionTime", "price", "quantity", "tradeId", "side", "tradeDate", "buyerId", "sellerId", "openingTrade", "systemPriced", "marketOnClose", "oddLot", "settlementTerms", "crossType", "byPass", "lastPrice", "saleCondition", "currency", "doesNotUpdateLast", "doesNotUpdateVolume", "session", "blockTrade", "distributionTime", "transactionTime2", "consolidatedPriceIndicator", "transient", "indexShortName"]
    ORIGINATORID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TRADEID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    BUYERID_FIELD_NUMBER: _ClassVar[int]
    SELLERID_FIELD_NUMBER: _ClassVar[int]
    OPENINGTRADE_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPRICED_FIELD_NUMBER: _ClassVar[int]
    MARKETONCLOSE_FIELD_NUMBER: _ClassVar[int]
    ODDLOT_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENTTERMS_FIELD_NUMBER: _ClassVar[int]
    CROSSTYPE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_FIELD_NUMBER: _ClassVar[int]
    LASTPRICE_FIELD_NUMBER: _ClassVar[int]
    SALECONDITION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DOESNOTUPDATELAST_FIELD_NUMBER: _ClassVar[int]
    DOESNOTUPDATEVOLUME_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    BLOCKTRADE_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME2_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATEDPRICEINDICATOR_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_FIELD_NUMBER: _ClassVar[int]
    INDEXSHORTNAME_FIELD_NUMBER: _ClassVar[int]
    originatorId: bytes
    transactionTime: int
    price: int
    quantity: int
    tradeId: bytes
    side: BookSide
    tradeDate: int
    buyerId: bytes
    sellerId: bytes
    openingTrade: bool
    systemPriced: bool
    marketOnClose: bool
    oddLot: bool
    settlementTerms: SettlementTerms
    crossType: CrossType
    byPass: bool
    lastPrice: int
    saleCondition: bytes
    currency: str
    doesNotUpdateLast: bool
    doesNotUpdateVolume: bool
    session: str
    blockTrade: bool
    distributionTime: int
    transactionTime2: int
    consolidatedPriceIndicator: str
    transient: bool
    indexShortName: str
    def __init__(self, originatorId: _Optional[bytes] = ..., transactionTime: _Optional[int] = ..., price: _Optional[int] = ..., quantity: _Optional[int] = ..., tradeId: _Optional[bytes] = ..., side: _Optional[_Union[BookSide, str]] = ..., tradeDate: _Optional[int] = ..., buyerId: _Optional[bytes] = ..., sellerId: _Optional[bytes] = ..., openingTrade: bool = ..., systemPriced: bool = ..., marketOnClose: bool = ..., oddLot: bool = ..., settlementTerms: _Optional[_Union[SettlementTerms, str]] = ..., crossType: _Optional[_Union[CrossType, str]] = ..., byPass: bool = ..., lastPrice: _Optional[int] = ..., saleCondition: _Optional[bytes] = ..., currency: _Optional[str] = ..., doesNotUpdateLast: bool = ..., doesNotUpdateVolume: bool = ..., session: _Optional[str] = ..., blockTrade: bool = ..., distributionTime: _Optional[int] = ..., transactionTime2: _Optional[int] = ..., consolidatedPriceIndicator: _Optional[str] = ..., transient: bool = ..., indexShortName: _Optional[str] = ...) -> None: ...

class TradeCorrection(_message.Message):
    __slots__ = ["originatorId", "transactionTime", "price", "quantity", "tradeId", "side", "tradeDate", "buyerId", "sellerId", "openingTrade", "systemPriced", "marketOnClose", "oddLot", "settlementTerms", "crossType", "byPass", "originalTradeId", "saleCondition", "currency", "distributionTime", "transactionTime2", "originalTradePrice", "originalTradeQuantity"]
    ORIGINATORID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TRADEID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    BUYERID_FIELD_NUMBER: _ClassVar[int]
    SELLERID_FIELD_NUMBER: _ClassVar[int]
    OPENINGTRADE_FIELD_NUMBER: _ClassVar[int]
    SYSTEMPRICED_FIELD_NUMBER: _ClassVar[int]
    MARKETONCLOSE_FIELD_NUMBER: _ClassVar[int]
    ODDLOT_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENTTERMS_FIELD_NUMBER: _ClassVar[int]
    CROSSTYPE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_FIELD_NUMBER: _ClassVar[int]
    ORIGINALTRADEID_FIELD_NUMBER: _ClassVar[int]
    SALECONDITION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME2_FIELD_NUMBER: _ClassVar[int]
    ORIGINALTRADEPRICE_FIELD_NUMBER: _ClassVar[int]
    ORIGINALTRADEQUANTITY_FIELD_NUMBER: _ClassVar[int]
    originatorId: bytes
    transactionTime: int
    price: int
    quantity: int
    tradeId: bytes
    side: BookSide
    tradeDate: int
    buyerId: bytes
    sellerId: bytes
    openingTrade: bool
    systemPriced: bool
    marketOnClose: bool
    oddLot: bool
    settlementTerms: SettlementTerms
    crossType: CrossType
    byPass: bool
    originalTradeId: bytes
    saleCondition: bytes
    currency: str
    distributionTime: int
    transactionTime2: int
    originalTradePrice: int
    originalTradeQuantity: int
    def __init__(self, originatorId: _Optional[bytes] = ..., transactionTime: _Optional[int] = ..., price: _Optional[int] = ..., quantity: _Optional[int] = ..., tradeId: _Optional[bytes] = ..., side: _Optional[_Union[BookSide, str]] = ..., tradeDate: _Optional[int] = ..., buyerId: _Optional[bytes] = ..., sellerId: _Optional[bytes] = ..., openingTrade: bool = ..., systemPriced: bool = ..., marketOnClose: bool = ..., oddLot: bool = ..., settlementTerms: _Optional[_Union[SettlementTerms, str]] = ..., crossType: _Optional[_Union[CrossType, str]] = ..., byPass: bool = ..., originalTradeId: _Optional[bytes] = ..., saleCondition: _Optional[bytes] = ..., currency: _Optional[str] = ..., distributionTime: _Optional[int] = ..., transactionTime2: _Optional[int] = ..., originalTradePrice: _Optional[int] = ..., originalTradeQuantity: _Optional[int] = ...) -> None: ...

class TradeCancel(_message.Message):
    __slots__ = ["originatorId", "transactionTime", "correctedTradePrice", "correctedTradeQuantity", "tradeId", "saleCondition", "currency", "distributionTime", "transactionTime2"]
    ORIGINATORID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    CORRECTEDTRADEPRICE_FIELD_NUMBER: _ClassVar[int]
    CORRECTEDTRADEQUANTITY_FIELD_NUMBER: _ClassVar[int]
    TRADEID_FIELD_NUMBER: _ClassVar[int]
    SALECONDITION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME2_FIELD_NUMBER: _ClassVar[int]
    originatorId: bytes
    transactionTime: int
    correctedTradePrice: int
    correctedTradeQuantity: int
    tradeId: bytes
    saleCondition: bytes
    currency: str
    distributionTime: int
    transactionTime2: int
    def __init__(self, originatorId: _Optional[bytes] = ..., transactionTime: _Optional[int] = ..., correctedTradePrice: _Optional[int] = ..., correctedTradeQuantity: _Optional[int] = ..., tradeId: _Optional[bytes] = ..., saleCondition: _Optional[bytes] = ..., currency: _Optional[str] = ..., distributionTime: _Optional[int] = ..., transactionTime2: _Optional[int] = ...) -> None: ...

class Open(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "OpenCloseSettlementFlag", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    OPENCLOSESETTLEMENTFLAG_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    OpenCloseSettlementFlag: OpenCloseSettlementFlag
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., OpenCloseSettlementFlag: _Optional[_Union[OpenCloseSettlementFlag, str]] = ..., currency: _Optional[str] = ...) -> None: ...

class High(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class HighRolling(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class Low(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class LowRolling(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class Close(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class PrevClose(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class Last(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "quantity", "currency", "session"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    quantity: int
    currency: str
    session: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., quantity: _Optional[int] = ..., currency: _Optional[str] = ..., session: _Optional[str] = ...) -> None: ...

class YearHigh(_message.Message):
    __slots__ = ["transactionTime", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class YearLow(_message.Message):
    __slots__ = ["transactionTime", "price", "currency"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    price: int
    currency: str
    def __init__(self, transactionTime: _Optional[int] = ..., price: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "volume"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    volume: int
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., volume: _Optional[int] = ...) -> None: ...

class NumberOfTrades(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "numberTrades"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    NUMBERTRADES_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    numberTrades: int
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., numberTrades: _Optional[int] = ...) -> None: ...

class MonetaryValue(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "value", "valueCurrencyCode"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUECURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    value: int
    valueCurrencyCode: str
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., value: _Optional[int] = ..., valueCurrencyCode: _Optional[str] = ...) -> None: ...

class Settlement(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "price", "preliminarySettle", "currency", "settlementSource", "session", "transient", "reserved"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRELIMINARYSETTLE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENTSOURCE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    price: int
    preliminarySettle: bool
    currency: str
    settlementSource: SettlementSource
    session: str
    transient: bool
    reserved: bool
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., price: _Optional[int] = ..., preliminarySettle: bool = ..., currency: _Optional[str] = ..., settlementSource: _Optional[_Union[SettlementSource, str]] = ..., session: _Optional[str] = ..., transient: bool = ..., reserved: bool = ...) -> None: ...

class OpenInterest(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "volume"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    volume: int
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., volume: _Optional[int] = ...) -> None: ...

class Vwap(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "vwap"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    VWAP_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    vwap: int
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., vwap: _Optional[int] = ...) -> None: ...

class DividendsIncomeDistributions(_message.Message):
    __slots__ = ["transactionTime", "instrumentType", "corporateAction", "distributionType", "payableDate", "recordDate", "exDividendDate", "amount", "currencyCode", "notes", "totalCashDistribution", "nonQualifiedCashDistribution", "qualifiedCashDistribution", "taxFreeCashDistribution", "ordinaryForeignTaxCredit", "qualifiedForeignTaxCredit", "stockDividendRatio", "reinvestDate"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CORPORATEACTION_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    PAYABLEDATE_FIELD_NUMBER: _ClassVar[int]
    RECORDDATE_FIELD_NUMBER: _ClassVar[int]
    EXDIVIDENDDATE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    TOTALCASHDISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    NONQUALIFIEDCASHDISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    QUALIFIEDCASHDISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    TAXFREECASHDISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    ORDINARYFOREIGNTAXCREDIT_FIELD_NUMBER: _ClassVar[int]
    QUALIFIEDFOREIGNTAXCREDIT_FIELD_NUMBER: _ClassVar[int]
    STOCKDIVIDENDRATIO_FIELD_NUMBER: _ClassVar[int]
    REINVESTDATE_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    instrumentType: str
    corporateAction: str
    distributionType: str
    payableDate: int
    recordDate: int
    exDividendDate: int
    amount: int
    currencyCode: str
    notes: _containers.RepeatedScalarFieldContainer[str]
    totalCashDistribution: int
    nonQualifiedCashDistribution: int
    qualifiedCashDistribution: int
    taxFreeCashDistribution: int
    ordinaryForeignTaxCredit: int
    qualifiedForeignTaxCredit: int
    stockDividendRatio: int
    reinvestDate: int
    def __init__(self, transactionTime: _Optional[int] = ..., instrumentType: _Optional[str] = ..., corporateAction: _Optional[str] = ..., distributionType: _Optional[str] = ..., payableDate: _Optional[int] = ..., recordDate: _Optional[int] = ..., exDividendDate: _Optional[int] = ..., amount: _Optional[int] = ..., currencyCode: _Optional[str] = ..., notes: _Optional[_Iterable[str]] = ..., totalCashDistribution: _Optional[int] = ..., nonQualifiedCashDistribution: _Optional[int] = ..., qualifiedCashDistribution: _Optional[int] = ..., taxFreeCashDistribution: _Optional[int] = ..., ordinaryForeignTaxCredit: _Optional[int] = ..., qualifiedForeignTaxCredit: _Optional[int] = ..., stockDividendRatio: _Optional[int] = ..., reinvestDate: _Optional[int] = ...) -> None: ...

class CapitalDistributions(_message.Message):
    __slots__ = ["transactionTime", "instrumentType", "corporateAction", "payableDate", "recordDate", "exDate", "shortTermCapitalGain", "longTermCapitalGain", "unallocatedDistributions", "returnOfCapital", "currencyCode", "notes", "reinvestDate"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CORPORATEACTION_FIELD_NUMBER: _ClassVar[int]
    PAYABLEDATE_FIELD_NUMBER: _ClassVar[int]
    RECORDDATE_FIELD_NUMBER: _ClassVar[int]
    EXDATE_FIELD_NUMBER: _ClassVar[int]
    SHORTTERMCAPITALGAIN_FIELD_NUMBER: _ClassVar[int]
    LONGTERMCAPITALGAIN_FIELD_NUMBER: _ClassVar[int]
    UNALLOCATEDDISTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    RETURNOFCAPITAL_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    REINVESTDATE_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    instrumentType: str
    corporateAction: str
    payableDate: int
    recordDate: int
    exDate: int
    shortTermCapitalGain: int
    longTermCapitalGain: int
    unallocatedDistributions: int
    returnOfCapital: int
    currencyCode: str
    notes: _containers.RepeatedScalarFieldContainer[str]
    reinvestDate: int
    def __init__(self, transactionTime: _Optional[int] = ..., instrumentType: _Optional[str] = ..., corporateAction: _Optional[str] = ..., payableDate: _Optional[int] = ..., recordDate: _Optional[int] = ..., exDate: _Optional[int] = ..., shortTermCapitalGain: _Optional[int] = ..., longTermCapitalGain: _Optional[int] = ..., unallocatedDistributions: _Optional[int] = ..., returnOfCapital: _Optional[int] = ..., currencyCode: _Optional[str] = ..., notes: _Optional[_Iterable[str]] = ..., reinvestDate: _Optional[int] = ...) -> None: ...

class SharesOutstanding(_message.Message):
    __slots__ = ["sharesOutstanding", "transactionTime"]
    SHARESOUTSTANDING_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    sharesOutstanding: int
    transactionTime: int
    def __init__(self, sharesOutstanding: _Optional[int] = ..., transactionTime: _Optional[int] = ...) -> None: ...

class NetAssetValue(_message.Message):
    __slots__ = ["netAssetValue", "transactionTime"]
    NETASSETVALUE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    netAssetValue: int
    transactionTime: int
    def __init__(self, netAssetValue: _Optional[int] = ..., transactionTime: _Optional[int] = ...) -> None: ...

class MarketSummary(_message.Message):
    __slots__ = ["transactionTime", "tradingDate", "startOfDay", "endOfDay", "clear", "instrumentStatus", "bbo", "open", "high", "low", "close", "prevClose", "last", "volume", "settlement", "openInterest", "vwap", "session", "summaryType", "prevVolume", "transient"]
    class ClearSet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NONE: _ClassVar[MarketSummary.ClearSet]
        ALL: _ClassVar[MarketSummary.ClearSet]
        BA: _ClassVar[MarketSummary.ClearSet]
        CUSTOM_1: _ClassVar[MarketSummary.ClearSet]
    NONE: MarketSummary.ClearSet
    ALL: MarketSummary.ClearSet
    BA: MarketSummary.ClearSet
    CUSTOM_1: MarketSummary.ClearSet
    class SummaryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        EXCHANGE_REFRESH: _ClassVar[MarketSummary.SummaryType]
        REFRESH_LIVE_PRICE: _ClassVar[MarketSummary.SummaryType]
        EOD_COMMODITY_PRICES: _ClassVar[MarketSummary.SummaryType]
        EOD_STOCK_FOREX_PRICES: _ClassVar[MarketSummary.SummaryType]
        EOD_COMMODITY_STATS: _ClassVar[MarketSummary.SummaryType]
    EXCHANGE_REFRESH: MarketSummary.SummaryType
    REFRESH_LIVE_PRICE: MarketSummary.SummaryType
    EOD_COMMODITY_PRICES: MarketSummary.SummaryType
    EOD_STOCK_FOREX_PRICES: MarketSummary.SummaryType
    EOD_COMMODITY_STATS: MarketSummary.SummaryType
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADINGDATE_FIELD_NUMBER: _ClassVar[int]
    STARTOFDAY_FIELD_NUMBER: _ClassVar[int]
    ENDOFDAY_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTSTATUS_FIELD_NUMBER: _ClassVar[int]
    BBO_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    PREVCLOSE_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    VWAP_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARYTYPE_FIELD_NUMBER: _ClassVar[int]
    PREVVOLUME_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradingDate: int
    startOfDay: bool
    endOfDay: bool
    clear: MarketSummary.ClearSet
    instrumentStatus: InstrumentStatus
    bbo: BestBidOffer
    open: Open
    high: High
    low: Low
    close: Close
    prevClose: PrevClose
    last: Last
    volume: Volume
    settlement: Settlement
    openInterest: OpenInterest
    vwap: Vwap
    session: str
    summaryType: MarketSummary.SummaryType
    prevVolume: Volume
    transient: bool
    def __init__(self, transactionTime: _Optional[int] = ..., tradingDate: _Optional[int] = ..., startOfDay: bool = ..., endOfDay: bool = ..., clear: _Optional[_Union[MarketSummary.ClearSet, str]] = ..., instrumentStatus: _Optional[_Union[InstrumentStatus, _Mapping]] = ..., bbo: _Optional[_Union[BestBidOffer, _Mapping]] = ..., open: _Optional[_Union[Open, _Mapping]] = ..., high: _Optional[_Union[High, _Mapping]] = ..., low: _Optional[_Union[Low, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., prevClose: _Optional[_Union[PrevClose, _Mapping]] = ..., last: _Optional[_Union[Last, _Mapping]] = ..., volume: _Optional[_Union[Volume, _Mapping]] = ..., settlement: _Optional[_Union[Settlement, _Mapping]] = ..., openInterest: _Optional[_Union[OpenInterest, _Mapping]] = ..., vwap: _Optional[_Union[Vwap, _Mapping]] = ..., session: _Optional[str] = ..., summaryType: _Optional[_Union[MarketSummary.SummaryType, str]] = ..., prevVolume: _Optional[_Union[Volume, _Mapping]] = ..., transient: bool = ...) -> None: ...

class Context(_message.Message):
    __slots__ = ["data", "tracePoints"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TRACEPOINTS_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[ContextData]
    tracePoints: _containers.RepeatedCompositeFieldContainer[TracePoint]
    def __init__(self, data: _Optional[_Iterable[_Union[ContextData, _Mapping]]] = ..., tracePoints: _Optional[_Iterable[_Union[TracePoint, _Mapping]]] = ...) -> None: ...

class ContextData(_message.Message):
    __slots__ = ["id", "vstring", "vbytes", "vbool", "vsint32", "vsint64", "vfloat", "vdouble"]
    ID_FIELD_NUMBER: _ClassVar[int]
    VSTRING_FIELD_NUMBER: _ClassVar[int]
    VBYTES_FIELD_NUMBER: _ClassVar[int]
    VBOOL_FIELD_NUMBER: _ClassVar[int]
    VSINT32_FIELD_NUMBER: _ClassVar[int]
    VSINT64_FIELD_NUMBER: _ClassVar[int]
    VFLOAT_FIELD_NUMBER: _ClassVar[int]
    VDOUBLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    vstring: str
    vbytes: bytes
    vbool: bool
    vsint32: int
    vsint64: int
    vfloat: float
    vdouble: float
    def __init__(self, id: _Optional[str] = ..., vstring: _Optional[str] = ..., vbytes: _Optional[bytes] = ..., vbool: bool = ..., vsint32: _Optional[int] = ..., vsint64: _Optional[int] = ..., vfloat: _Optional[float] = ..., vdouble: _Optional[float] = ...) -> None: ...

class TracePoint(_message.Message):
    __slots__ = ["id", "componentId", "timestampNs", "componentLatencyNs"]
    ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENTID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPNS_FIELD_NUMBER: _ClassVar[int]
    COMPONENTLATENCYNS_FIELD_NUMBER: _ClassVar[int]
    id: str
    componentId: str
    timestampNs: int
    componentLatencyNs: int
    def __init__(self, id: _Optional[str] = ..., componentId: _Optional[str] = ..., timestampNs: _Optional[int] = ..., componentLatencyNs: _Optional[int] = ...) -> None: ...

class TCPHistoricalReplayRequest(_message.Message):
    __slots__ = ["channel", "resetNumber", "sequence", "count", "requestId"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RESETNUMBER_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    channel: int
    resetNumber: int
    sequence: int
    count: int
    requestId: str
    def __init__(self, channel: _Optional[int] = ..., resetNumber: _Optional[int] = ..., sequence: _Optional[int] = ..., count: _Optional[int] = ..., requestId: _Optional[str] = ...) -> None: ...

class SnapshotRequest(_message.Message):
    __slots__ = ["channel", "resetNumber", "requestId", "snapshotRequestTypes"]
    class SnapshotRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ALL: _ClassVar[SnapshotRequest.SnapshotRequestType]
        QUOTE: _ClassVar[SnapshotRequest.SnapshotRequestType]
        DEPTH: _ClassVar[SnapshotRequest.SnapshotRequestType]
        VOLUME_AT_PRICE: _ClassVar[SnapshotRequest.SnapshotRequestType]
    ALL: SnapshotRequest.SnapshotRequestType
    QUOTE: SnapshotRequest.SnapshotRequestType
    DEPTH: SnapshotRequest.SnapshotRequestType
    VOLUME_AT_PRICE: SnapshotRequest.SnapshotRequestType
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RESETNUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTREQUESTTYPES_FIELD_NUMBER: _ClassVar[int]
    channel: int
    resetNumber: int
    requestId: str
    snapshotRequestTypes: _containers.RepeatedScalarFieldContainer[SnapshotRequest.SnapshotRequestType]
    def __init__(self, channel: _Optional[int] = ..., resetNumber: _Optional[int] = ..., requestId: _Optional[str] = ..., snapshotRequestTypes: _Optional[_Iterable[_Union[SnapshotRequest.SnapshotRequestType, str]]] = ...) -> None: ...

class VolumeAtPrice(_message.Message):
    __slots__ = ["marketId", "symbol", "transactionTime", "lastPrice", "lastQuantity", "lastCumulativeVolume", "tradeDate", "priceVolumes"]
    class PriceLevelVolume(_message.Message):
        __slots__ = ["price", "volume"]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        price: int
        volume: int
        def __init__(self, price: _Optional[int] = ..., volume: _Optional[int] = ...) -> None: ...
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    LASTPRICE_FIELD_NUMBER: _ClassVar[int]
    LASTQUANTITY_FIELD_NUMBER: _ClassVar[int]
    LASTCUMULATIVEVOLUME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    PRICEVOLUMES_FIELD_NUMBER: _ClassVar[int]
    marketId: int
    symbol: str
    transactionTime: int
    lastPrice: int
    lastQuantity: int
    lastCumulativeVolume: int
    tradeDate: int
    priceVolumes: _containers.RepeatedCompositeFieldContainer[VolumeAtPrice.PriceLevelVolume]
    def __init__(self, marketId: _Optional[int] = ..., symbol: _Optional[str] = ..., transactionTime: _Optional[int] = ..., lastPrice: _Optional[int] = ..., lastQuantity: _Optional[int] = ..., lastCumulativeVolume: _Optional[int] = ..., tradeDate: _Optional[int] = ..., priceVolumes: _Optional[_Iterable[_Union[VolumeAtPrice.PriceLevelVolume, _Mapping]]] = ...) -> None: ...

class Ohlc(_message.Message):
    __slots__ = ["marketId", "symbol", "open", "high", "low", "close", "volume", "priceVolume", "numberTrades", "tradeDate", "transactionTime", "tradeIds", "openStartTime", "closeEndTime"]
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PRICEVOLUME_FIELD_NUMBER: _ClassVar[int]
    NUMBERTRADES_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEIDS_FIELD_NUMBER: _ClassVar[int]
    OPENSTARTTIME_FIELD_NUMBER: _ClassVar[int]
    CLOSEENDTIME_FIELD_NUMBER: _ClassVar[int]
    marketId: int
    symbol: str
    open: Open
    high: High
    low: Low
    close: Close
    volume: int
    priceVolume: float
    numberTrades: int
    tradeDate: int
    transactionTime: int
    tradeIds: _containers.RepeatedScalarFieldContainer[str]
    openStartTime: int
    closeEndTime: int
    def __init__(self, marketId: _Optional[int] = ..., symbol: _Optional[str] = ..., open: _Optional[_Union[Open, _Mapping]] = ..., high: _Optional[_Union[High, _Mapping]] = ..., low: _Optional[_Union[Low, _Mapping]] = ..., close: _Optional[_Union[Close, _Mapping]] = ..., volume: _Optional[int] = ..., priceVolume: _Optional[float] = ..., numberTrades: _Optional[int] = ..., tradeDate: _Optional[int] = ..., transactionTime: _Optional[int] = ..., tradeIds: _Optional[_Iterable[str]] = ..., openStartTime: _Optional[int] = ..., closeEndTime: _Optional[int] = ...) -> None: ...

class InstrumentAction(_message.Message):
    __slots__ = ["transactionTime", "tradeDate", "action", "message", "instrument", "newInstrument"]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    TRADEDATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    NEWINSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    transactionTime: int
    tradeDate: int
    action: ActionType
    message: str
    instrument: _openfeed_instrument_pb2.InstrumentDefinition
    newInstrument: _openfeed_instrument_pb2.InstrumentDefinition
    def __init__(self, transactionTime: _Optional[int] = ..., tradeDate: _Optional[int] = ..., action: _Optional[_Union[ActionType, str]] = ..., message: _Optional[str] = ..., instrument: _Optional[_Union[_openfeed_instrument_pb2.InstrumentDefinition, _Mapping]] = ..., newInstrument: _Optional[_Union[_openfeed_instrument_pb2.InstrumentDefinition, _Mapping]] = ...) -> None: ...

class RequestForQuote(_message.Message):
    __slots__ = ["quoteRequestId", "symbol", "securityId", "orderQuantity", "quoteType", "side"]
    QUOTEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SECURITYID_FIELD_NUMBER: _ClassVar[int]
    ORDERQUANTITY_FIELD_NUMBER: _ClassVar[int]
    QUOTETYPE_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    quoteRequestId: str
    symbol: str
    securityId: int
    orderQuantity: int
    quoteType: int
    side: int
    def __init__(self, quoteRequestId: _Optional[str] = ..., symbol: _Optional[str] = ..., securityId: _Optional[int] = ..., orderQuantity: _Optional[int] = ..., quoteType: _Optional[int] = ..., side: _Optional[int] = ...) -> None: ...
