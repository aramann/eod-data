from eod.request_handler_class import RequestHandler


class SentimentalData(RequestHandler):
    def __init__(self, api_key: str, timeout: int):
        self.URL_HISTORICAL_MARKET_CAP = 'https://eodhistoricaldata.com/api/sentiments/'
        super().__init__(api_key, timeout)

    def get_sentimental_data(self, symbols: list, **query_params):
        """
        Get aggregated sentiment data for list for multiple tickers

        Parameters
        ----------
        symbols : list
            List of tickers to analyse.
        **query_params :
            query parameters.

        Returns
        -------
        dict
            .

        """

        self.endpoint = self.URL_HISTORICAL_MARKET_CAP + '?s=' + ','.join(symbols)
        return super().handle_request(self.endpoint, query_params)