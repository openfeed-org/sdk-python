# Openfeed SDK for Python

This SDK encapuslates the openfeed proto objects and faciliates client connections to openfeed servers.

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

## Known Issues

* https://github.com/protocolbuffers/protobuf/issues/1491