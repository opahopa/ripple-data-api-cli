# ripple-data-api-cli

Simple API client for [Ripple Data API](https://developers.ripple.com/data-api.html)

Current functionality limited to plotting the chart of transactions count in time for specified address

Settings are directly in `main.py`:

* `timeframe_days`: timeframe
* `type`: transaction type Enum [types](https://developers.ripple.com/transaction-types.html)
* `amount_limit`: transactions value upper limit in XRP