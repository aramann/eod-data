from eod.request_handler_class import RequestHandler


class HistoricalMarketCapitalization(RequestHandler):
    def __init__(self, api_key: str, timeout: int):
        self.URL_HISTORICAL_MARKET_CAP = 'https://eodhistoricaldata.com/api/historical-market-cap/'
        super().__init__(api_key, timeout)

    def get_historical_market_cap(self, symbol: str, **query_params):
        """
        Get historical data for the requested stock.

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.

        Returns
        -------
        dict
            historical data.

        """

        self.endpoint = self.URL_HISTORICAL_MARKET_CAP + symbol.upper()
        return super().handle_request(self.endpoint, query_params)
