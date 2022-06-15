import websocket
import json
from threading import Thread
import time


class RealTimeData:
    def __init__(self, api_key: str, endpoint: str, symbols: list):
        super().__init__()
        self.__URL_REAL_TIME_DATA = 'wss://ws.eodhistoricaldata.com/ws/'
        self.__api_key = api_key
        if endpoint not in ['us', 'us-quote', 'index', 'forex', 'crypto']:
            raise ValueError("Endpoint is invalid")
        self.__endpoint = endpoint
        self.__symbols = symbols

        self.__socket = None
        self.__message = None
        self.__stop = False
        self.__new_message = False
        self.__main = None
        self.__keepalive = None

    def start(self):
        """
        Starts socket connection and keeps it alive
        """
        self.__main = Thread(target=self.__go)
        self.__main.daemon = True
        self.__keepalive = Thread(target=self.__keepalive_func)
        self.__keepalive.daemon = True
        self.__main.start()

    def close(self):
        """
        Closes socket connection
        """
        self.__disconnect()
        self.__main.join()

    def is_new_message(self):
        """
        Checks if new message is available
        :return: Boolean
        """
        return self.__new_message

    def get_message(self):
        """
        Gets message from socket
        :return: message
        """
        self.__new_message = False
        return self.__message

    def __go(self):
        self.__connect()
        self.__listen()
        self.__disconnect()

    def __keepalive_func(self, interval=30):
        while self.__socket.connected:
            self.__socket.ping('keepalive')
            time.sleep(interval)

    def __connect(self):
        self.__socket = websocket.create_connection(self.__URL_REAL_TIME_DATA + self.__endpoint + '/?api_token=' +
                                                    self.__api_key)
        self.__socket.send(''
                         '{"action": "subscribe",'
                         ' "symbols": "' + ','.join(self.__symbols) + '"}'
                           )

    def __disconnect(self):
        self.__stop = True
        self.__socket.close()

    def __listen(self):
        self.__keepalive.start()
        while not self.__stop:
            data = self.__socket.recv()
            if data != "":
                msg = json.loads(data)
            else:
                msg = {}
            self.__message = msg
            self.__new_message = True
