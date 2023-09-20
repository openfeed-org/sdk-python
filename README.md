# Openfeed SDK for Python

This SDK encapuslates the openfeed proto objects and faciliates client connections to openfeed servers.

![Build](https://github.com/openfeed-org/sdk-python/workflows/PyPI%20and%20TestPyPI/badge.svg)

![PyPI](https://img.shields.io/pypi/v/openfeed?label=PyPI%20)

## Installation

```
pip install openfeed
```

## Example Usage

```python
import openfeed

# new client with credentials
of_client = openfeed.OpenfeedClient("username", "password")

# optional state handlers
of_client.on_error = lambda x: print("Error:", x)
of_client.on_connected = lambda x: print("Connected")
of_client.on_disconnected = lambda x: print("Disconnected")

# attach a global message handler
of_client.on_message = lambda x: print("Global Message:", x)

# sub to markets by symbol
def on_message(msg):
    print("Market Data: ", msg)

of_client.add_symbol_subscription("AAPL", callback=on_message)

# sub to markets by exchange
of_client.add_exchange_subscription("NYSE", callback=on_message)

of_client.start()
```

### Expected Output

```log
of-client: Connected
of-client: Market Data:  subscriptionResponse
of-client: Market Data:  marketSnapshot
of-client: Market Data:  marketUpdate
of-client: Market Data:  marketUpdate
```

### Openfeed Documentation

* [https://docs.barchart.com/openfeed](https://docs.barchart.com/openfeed)

## Subscription Types

Openfeed supports many levels of [subscription types](https://docs.barchart.com/openfeed/#/proto?id=subscriptiontype).

### OHLC

```python
of_client.add_exchange_subscription(["NYSE"], callback=on_message, subscription_type=["OHLC"])
```

```
{
  marketId: 5389879102616877808
  symbol: "AAPL"
  open {
    price: 1205600
  }
  high {
    price: 1205600
  }
  low {
    price: 1205247
  }
  close {
    price: 1205490
  }
  volume: 43635
  priceVolume: 5259897.1422
  numberTrades: 224
  tradeDate: 20201116
  transactionTime: 1605547921000000000
  openStartTime: 1605547885850000000
  closeEndTime: 1605547920964000000
}
```
