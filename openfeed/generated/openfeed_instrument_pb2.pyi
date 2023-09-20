from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstrumentDefinition(_message.Message):
    __slots__ = ["marketId", "instrumentType", "supportBookTypes", "bookDepth", "vendorId", "symbol", "description", "cfiCode", "currencyCode", "exchangeCode", "minimumPriceIncrement", "contractPointValue", "schedule", "calendar", "recordCreateTime", "recordUpdateTime", "timeZoneName", "instrumentGroup", "symbolExpiration", "state", "channel", "underlyingMarketId", "priceFormat", "optionStrikePriceFormat", "priceDenominator", "quantityDenominator", "isTradable", "transactionTime", "auxiliaryData", "symbols", "optionStrike", "optionType", "optionStyle", "optionStrikeDenominator", "spreadCode", "spreadLeg", "userDefinedSpread", "marketTier", "financialStatusIndicator", "isin", "currencyPair", "exchangeSendsVolume", "exchangeSendsHigh", "exchangeSendsLow", "exchangeSendsOpen", "consolidatedFeedInstrument", "openOutcryInstrument", "syntheticAmericanOptionInstrument", "barchartExchangeCode", "barchartBaseCode", "volumeDenominator", "bidOfferQuantityDenominator", "primaryListingMarketParticipantId", "subscriptionSymbol", "contractMaturity", "underlying", "commodity", "exchangeId", "priceScalingExponent", "underlyingOpenfeedMarketId"]
    class InstrumentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_INSTRUMENT_TYPE: _ClassVar[InstrumentDefinition.InstrumentType]
        FOREX: _ClassVar[InstrumentDefinition.InstrumentType]
        INDEX: _ClassVar[InstrumentDefinition.InstrumentType]
        EQUITY: _ClassVar[InstrumentDefinition.InstrumentType]
        FUTURE: _ClassVar[InstrumentDefinition.InstrumentType]
        OPTION: _ClassVar[InstrumentDefinition.InstrumentType]
        SPREAD: _ClassVar[InstrumentDefinition.InstrumentType]
        MUTUAL_FUND: _ClassVar[InstrumentDefinition.InstrumentType]
        MONEY_MARKET_FUND: _ClassVar[InstrumentDefinition.InstrumentType]
        USER_DEFINED_SPREAD: _ClassVar[InstrumentDefinition.InstrumentType]
        EQUITY_OPTION: _ClassVar[InstrumentDefinition.InstrumentType]
    UNKNOWN_INSTRUMENT_TYPE: InstrumentDefinition.InstrumentType
    FOREX: InstrumentDefinition.InstrumentType
    INDEX: InstrumentDefinition.InstrumentType
    EQUITY: InstrumentDefinition.InstrumentType
    FUTURE: InstrumentDefinition.InstrumentType
    OPTION: InstrumentDefinition.InstrumentType
    SPREAD: InstrumentDefinition.InstrumentType
    MUTUAL_FUND: InstrumentDefinition.InstrumentType
    MONEY_MARKET_FUND: InstrumentDefinition.InstrumentType
    USER_DEFINED_SPREAD: InstrumentDefinition.InstrumentType
    EQUITY_OPTION: InstrumentDefinition.InstrumentType
    class BookType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_BOOK_TYPE: _ClassVar[InstrumentDefinition.BookType]
        TOP_OF_BOOK: _ClassVar[InstrumentDefinition.BookType]
        PRICE_LEVEL_DEPTH: _ClassVar[InstrumentDefinition.BookType]
        ORDER_DEPTH: _ClassVar[InstrumentDefinition.BookType]
    UNKNOWN_BOOK_TYPE: InstrumentDefinition.BookType
    TOP_OF_BOOK: InstrumentDefinition.BookType
    PRICE_LEVEL_DEPTH: InstrumentDefinition.BookType
    ORDER_DEPTH: InstrumentDefinition.BookType
    class OptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_OPTION_TYPE: _ClassVar[InstrumentDefinition.OptionType]
        CALL: _ClassVar[InstrumentDefinition.OptionType]
        PUT: _ClassVar[InstrumentDefinition.OptionType]
    UNKNOWN_OPTION_TYPE: InstrumentDefinition.OptionType
    CALL: InstrumentDefinition.OptionType
    PUT: InstrumentDefinition.OptionType
    class OptionStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_OPTIONS_STYLE: _ClassVar[InstrumentDefinition.OptionStyle]
        DEFAULT: _ClassVar[InstrumentDefinition.OptionStyle]
        AMERICAN: _ClassVar[InstrumentDefinition.OptionStyle]
        EUROPEAN: _ClassVar[InstrumentDefinition.OptionStyle]
    UNKNOWN_OPTIONS_STYLE: InstrumentDefinition.OptionStyle
    DEFAULT: InstrumentDefinition.OptionStyle
    AMERICAN: InstrumentDefinition.OptionStyle
    EUROPEAN: InstrumentDefinition.OptionStyle
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_STATE: _ClassVar[InstrumentDefinition.State]
        ACTIVE: _ClassVar[InstrumentDefinition.State]
        PASSIVE: _ClassVar[InstrumentDefinition.State]
    UNKNOWN_STATE: InstrumentDefinition.State
    ACTIVE: InstrumentDefinition.State
    PASSIVE: InstrumentDefinition.State
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_EVENT_TYPE: _ClassVar[InstrumentDefinition.EventType]
        FIRST_TRADE_DATE: _ClassVar[InstrumentDefinition.EventType]
        LAST_TRADE_DATE: _ClassVar[InstrumentDefinition.EventType]
        MATURITY_DATE: _ClassVar[InstrumentDefinition.EventType]
        FIRST_DELIVERY_DATE: _ClassVar[InstrumentDefinition.EventType]
        LAST_DELIVERY_DATE: _ClassVar[InstrumentDefinition.EventType]
        FIRST_NOTICE_DATE: _ClassVar[InstrumentDefinition.EventType]
        LAST_NOTICE_DATE: _ClassVar[InstrumentDefinition.EventType]
        FIRST_HOLDING_DATE: _ClassVar[InstrumentDefinition.EventType]
        LAST_HOLDING_DATE: _ClassVar[InstrumentDefinition.EventType]
        FIRST_POSITION_DATE: _ClassVar[InstrumentDefinition.EventType]
        LAST_POSITION_DATE: _ClassVar[InstrumentDefinition.EventType]
        DELIVERY_START_DATE: _ClassVar[InstrumentDefinition.EventType]
        DELIVERY_END_DATE: _ClassVar[InstrumentDefinition.EventType]
    UNKNOWN_EVENT_TYPE: InstrumentDefinition.EventType
    FIRST_TRADE_DATE: InstrumentDefinition.EventType
    LAST_TRADE_DATE: InstrumentDefinition.EventType
    MATURITY_DATE: InstrumentDefinition.EventType
    FIRST_DELIVERY_DATE: InstrumentDefinition.EventType
    LAST_DELIVERY_DATE: InstrumentDefinition.EventType
    FIRST_NOTICE_DATE: InstrumentDefinition.EventType
    LAST_NOTICE_DATE: InstrumentDefinition.EventType
    FIRST_HOLDING_DATE: InstrumentDefinition.EventType
    LAST_HOLDING_DATE: InstrumentDefinition.EventType
    FIRST_POSITION_DATE: InstrumentDefinition.EventType
    LAST_POSITION_DATE: InstrumentDefinition.EventType
    DELIVERY_START_DATE: InstrumentDefinition.EventType
    DELIVERY_END_DATE: InstrumentDefinition.EventType
    class Schedule(_message.Message):
        __slots__ = ["sessions"]
        SESSIONS_FIELD_NUMBER: _ClassVar[int]
        sessions: _containers.RepeatedCompositeFieldContainer[InstrumentDefinition.TimeSpan]
        def __init__(self, sessions: _Optional[_Iterable[_Union[InstrumentDefinition.TimeSpan, _Mapping]]] = ...) -> None: ...
    class TimeSpan(_message.Message):
        __slots__ = ["timeStart", "timeFinish"]
        TIMESTART_FIELD_NUMBER: _ClassVar[int]
        TIMEFINISH_FIELD_NUMBER: _ClassVar[int]
        timeStart: int
        timeFinish: int
        def __init__(self, timeStart: _Optional[int] = ..., timeFinish: _Optional[int] = ...) -> None: ...
    class Calendar(_message.Message):
        __slots__ = ["events"]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        events: _containers.RepeatedCompositeFieldContainer[InstrumentDefinition.Event]
        def __init__(self, events: _Optional[_Iterable[_Union[InstrumentDefinition.Event, _Mapping]]] = ...) -> None: ...
    class Event(_message.Message):
        __slots__ = ["type", "date"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DATE_FIELD_NUMBER: _ClassVar[int]
        type: InstrumentDefinition.EventType
        date: int
        def __init__(self, type: _Optional[_Union[InstrumentDefinition.EventType, str]] = ..., date: _Optional[int] = ...) -> None: ...
    class SpreadLeg(_message.Message):
        __slots__ = ["marketId", "ratio", "symbol", "longSymbol", "legOptionDelta", "legPrice"]
        MARKETID_FIELD_NUMBER: _ClassVar[int]
        RATIO_FIELD_NUMBER: _ClassVar[int]
        SYMBOL_FIELD_NUMBER: _ClassVar[int]
        LONGSYMBOL_FIELD_NUMBER: _ClassVar[int]
        LEGOPTIONDELTA_FIELD_NUMBER: _ClassVar[int]
        LEGPRICE_FIELD_NUMBER: _ClassVar[int]
        marketId: int
        ratio: int
        symbol: str
        longSymbol: str
        legOptionDelta: float
        legPrice: float
        def __init__(self, marketId: _Optional[int] = ..., ratio: _Optional[int] = ..., symbol: _Optional[str] = ..., longSymbol: _Optional[str] = ..., legOptionDelta: _Optional[float] = ..., legPrice: _Optional[float] = ...) -> None: ...
    class MaturityDate(_message.Message):
        __slots__ = ["year", "month", "day"]
        YEAR_FIELD_NUMBER: _ClassVar[int]
        MONTH_FIELD_NUMBER: _ClassVar[int]
        DAY_FIELD_NUMBER: _ClassVar[int]
        year: int
        month: int
        day: int
        def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...
    class Symbol(_message.Message):
        __slots__ = ["vendor", "symbol", "longSymbol"]
        VENDOR_FIELD_NUMBER: _ClassVar[int]
        SYMBOL_FIELD_NUMBER: _ClassVar[int]
        LONGSYMBOL_FIELD_NUMBER: _ClassVar[int]
        vendor: str
        symbol: str
        longSymbol: str
        def __init__(self, vendor: _Optional[str] = ..., symbol: _Optional[str] = ..., longSymbol: _Optional[str] = ...) -> None: ...
    class PriceFormat(_message.Message):
        __slots__ = ["isFractional", "denominator", "subDenominator", "subFormat"]
        class SubFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            FLAT: _ClassVar[InstrumentDefinition.PriceFormat.SubFormat]
            FRACTIONAL: _ClassVar[InstrumentDefinition.PriceFormat.SubFormat]
            DECIMAL: _ClassVar[InstrumentDefinition.PriceFormat.SubFormat]
        FLAT: InstrumentDefinition.PriceFormat.SubFormat
        FRACTIONAL: InstrumentDefinition.PriceFormat.SubFormat
        DECIMAL: InstrumentDefinition.PriceFormat.SubFormat
        ISFRACTIONAL_FIELD_NUMBER: _ClassVar[int]
        DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
        SUBDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
        SUBFORMAT_FIELD_NUMBER: _ClassVar[int]
        isFractional: bool
        denominator: int
        subDenominator: int
        subFormat: InstrumentDefinition.PriceFormat.SubFormat
        def __init__(self, isFractional: bool = ..., denominator: _Optional[int] = ..., subDenominator: _Optional[int] = ..., subFormat: _Optional[_Union[InstrumentDefinition.PriceFormat.SubFormat, str]] = ...) -> None: ...
    class CurrencyPair(_message.Message):
        __slots__ = ["currency1", "currency2"]
        CURRENCY1_FIELD_NUMBER: _ClassVar[int]
        CURRENCY2_FIELD_NUMBER: _ClassVar[int]
        currency1: str
        currency2: str
        def __init__(self, currency1: _Optional[str] = ..., currency2: _Optional[str] = ...) -> None: ...
    MARKETID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTBOOKTYPES_FIELD_NUMBER: _ClassVar[int]
    BOOKDEPTH_FIELD_NUMBER: _ClassVar[int]
    VENDORID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CFICODE_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGECODE_FIELD_NUMBER: _ClassVar[int]
    MINIMUMPRICEINCREMENT_FIELD_NUMBER: _ClassVar[int]
    CONTRACTPOINTVALUE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    RECORDCREATETIME_FIELD_NUMBER: _ClassVar[int]
    RECORDUPDATETIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONENAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTGROUP_FIELD_NUMBER: _ClassVar[int]
    SYMBOLEXPIRATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGMARKETID_FIELD_NUMBER: _ClassVar[int]
    PRICEFORMAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONSTRIKEPRICEFORMAT_FIELD_NUMBER: _ClassVar[int]
    PRICEDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    QUANTITYDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    ISTRADABLE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    AUXILIARYDATA_FIELD_NUMBER: _ClassVar[int]
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    OPTIONSTRIKE_FIELD_NUMBER: _ClassVar[int]
    OPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONSTYLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONSTRIKEDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    SPREADCODE_FIELD_NUMBER: _ClassVar[int]
    SPREADLEG_FIELD_NUMBER: _ClassVar[int]
    USERDEFINEDSPREAD_FIELD_NUMBER: _ClassVar[int]
    MARKETTIER_FIELD_NUMBER: _ClassVar[int]
    FINANCIALSTATUSINDICATOR_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    CURRENCYPAIR_FIELD_NUMBER: _ClassVar[int]
    EXCHANGESENDSVOLUME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGESENDSHIGH_FIELD_NUMBER: _ClassVar[int]
    EXCHANGESENDSLOW_FIELD_NUMBER: _ClassVar[int]
    EXCHANGESENDSOPEN_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATEDFEEDINSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    OPENOUTCRYINSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SYNTHETICAMERICANOPTIONINSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    BARCHARTEXCHANGECODE_FIELD_NUMBER: _ClassVar[int]
    BARCHARTBASECODE_FIELD_NUMBER: _ClassVar[int]
    VOLUMEDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    BIDOFFERQUANTITYDENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    PRIMARYLISTINGMARKETPARTICIPANTID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONSYMBOL_FIELD_NUMBER: _ClassVar[int]
    CONTRACTMATURITY_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_FIELD_NUMBER: _ClassVar[int]
    COMMODITY_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEID_FIELD_NUMBER: _ClassVar[int]
    PRICESCALINGEXPONENT_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGOPENFEEDMARKETID_FIELD_NUMBER: _ClassVar[int]
    marketId: int
    instrumentType: InstrumentDefinition.InstrumentType
    supportBookTypes: _containers.RepeatedScalarFieldContainer[InstrumentDefinition.BookType]
    bookDepth: int
    vendorId: str
    symbol: str
    description: str
    cfiCode: str
    currencyCode: str
    exchangeCode: str
    minimumPriceIncrement: float
    contractPointValue: float
    schedule: InstrumentDefinition.Schedule
    calendar: InstrumentDefinition.Calendar
    recordCreateTime: int
    recordUpdateTime: int
    timeZoneName: str
    instrumentGroup: str
    symbolExpiration: InstrumentDefinition.MaturityDate
    state: InstrumentDefinition.State
    channel: int
    underlyingMarketId: int
    priceFormat: InstrumentDefinition.PriceFormat
    optionStrikePriceFormat: InstrumentDefinition.PriceFormat
    priceDenominator: int
    quantityDenominator: int
    isTradable: bool
    transactionTime: int
    auxiliaryData: bytes
    symbols: _containers.RepeatedCompositeFieldContainer[InstrumentDefinition.Symbol]
    optionStrike: int
    optionType: InstrumentDefinition.OptionType
    optionStyle: InstrumentDefinition.OptionStyle
    optionStrikeDenominator: int
    spreadCode: str
    spreadLeg: _containers.RepeatedCompositeFieldContainer[InstrumentDefinition.SpreadLeg]
    userDefinedSpread: bool
    marketTier: str
    financialStatusIndicator: str
    isin: str
    currencyPair: InstrumentDefinition.CurrencyPair
    exchangeSendsVolume: bool
    exchangeSendsHigh: bool
    exchangeSendsLow: bool
    exchangeSendsOpen: bool
    consolidatedFeedInstrument: bool
    openOutcryInstrument: bool
    syntheticAmericanOptionInstrument: bool
    barchartExchangeCode: str
    barchartBaseCode: str
    volumeDenominator: int
    bidOfferQuantityDenominator: int
    primaryListingMarketParticipantId: str
    subscriptionSymbol: str
    contractMaturity: InstrumentDefinition.MaturityDate
    underlying: str
    commodity: str
    exchangeId: int
    priceScalingExponent: int
    underlyingOpenfeedMarketId: int
    def __init__(self, marketId: _Optional[int] = ..., instrumentType: _Optional[_Union[InstrumentDefinition.InstrumentType, str]] = ..., supportBookTypes: _Optional[_Iterable[_Union[InstrumentDefinition.BookType, str]]] = ..., bookDepth: _Optional[int] = ..., vendorId: _Optional[str] = ..., symbol: _Optional[str] = ..., description: _Optional[str] = ..., cfiCode: _Optional[str] = ..., currencyCode: _Optional[str] = ..., exchangeCode: _Optional[str] = ..., minimumPriceIncrement: _Optional[float] = ..., contractPointValue: _Optional[float] = ..., schedule: _Optional[_Union[InstrumentDefinition.Schedule, _Mapping]] = ..., calendar: _Optional[_Union[InstrumentDefinition.Calendar, _Mapping]] = ..., recordCreateTime: _Optional[int] = ..., recordUpdateTime: _Optional[int] = ..., timeZoneName: _Optional[str] = ..., instrumentGroup: _Optional[str] = ..., symbolExpiration: _Optional[_Union[InstrumentDefinition.MaturityDate, _Mapping]] = ..., state: _Optional[_Union[InstrumentDefinition.State, str]] = ..., channel: _Optional[int] = ..., underlyingMarketId: _Optional[int] = ..., priceFormat: _Optional[_Union[InstrumentDefinition.PriceFormat, _Mapping]] = ..., optionStrikePriceFormat: _Optional[_Union[InstrumentDefinition.PriceFormat, _Mapping]] = ..., priceDenominator: _Optional[int] = ..., quantityDenominator: _Optional[int] = ..., isTradable: bool = ..., transactionTime: _Optional[int] = ..., auxiliaryData: _Optional[bytes] = ..., symbols: _Optional[_Iterable[_Union[InstrumentDefinition.Symbol, _Mapping]]] = ..., optionStrike: _Optional[int] = ..., optionType: _Optional[_Union[InstrumentDefinition.OptionType, str]] = ..., optionStyle: _Optional[_Union[InstrumentDefinition.OptionStyle, str]] = ..., optionStrikeDenominator: _Optional[int] = ..., spreadCode: _Optional[str] = ..., spreadLeg: _Optional[_Iterable[_Union[InstrumentDefinition.SpreadLeg, _Mapping]]] = ..., userDefinedSpread: bool = ..., marketTier: _Optional[str] = ..., financialStatusIndicator: _Optional[str] = ..., isin: _Optional[str] = ..., currencyPair: _Optional[_Union[InstrumentDefinition.CurrencyPair, _Mapping]] = ..., exchangeSendsVolume: bool = ..., exchangeSendsHigh: bool = ..., exchangeSendsLow: bool = ..., exchangeSendsOpen: bool = ..., consolidatedFeedInstrument: bool = ..., openOutcryInstrument: bool = ..., syntheticAmericanOptionInstrument: bool = ..., barchartExchangeCode: _Optional[str] = ..., barchartBaseCode: _Optional[str] = ..., volumeDenominator: _Optional[int] = ..., bidOfferQuantityDenominator: _Optional[int] = ..., primaryListingMarketParticipantId: _Optional[str] = ..., subscriptionSymbol: _Optional[str] = ..., contractMaturity: _Optional[_Union[InstrumentDefinition.MaturityDate, _Mapping]] = ..., underlying: _Optional[str] = ..., commodity: _Optional[str] = ..., exchangeId: _Optional[int] = ..., priceScalingExponent: _Optional[int] = ..., underlyingOpenfeedMarketId: _Optional[int] = ...) -> None: ...
