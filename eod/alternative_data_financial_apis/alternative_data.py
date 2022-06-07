from eod.alternative_data_financial_apis.sentimental_data_financial_api import SentimentalData


class AlternativeData(SentimentalData):
    def __init__(self, api_key: str, timeout: int):
        SentimentalData.__init__(self, api_key, timeout)