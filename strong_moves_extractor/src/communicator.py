import socket
import requests
from src.endpoints import Endpoint

LOGIN_ENDPOINT = 'user/login'

class Communicator:
    """This class is used to communicate with uci-server by sockets."""

    def __init__(self, address, port, login, password):
        self.address = address
        self.port = port
        self.login = login
        self.password = password #TODO: Do not keep it in plain text

        self.socket = None
        self.uri = 'http://{}:{}'.format(self.address, self.port)
        self.token = None

        try:
            # generate user's token
            self.__login()

            # use sockets
            self.__connect()
        except Exception as e:
            print(e)


    def __del__(self):
        try:
            requests.get('{}{}'.format(self.uri, Endpoint.logout.value), json=payload)
            self.socket.close()
        except:
            pass #TODO


    # TODO: Create custom Exceptions and make a proper use of them.
    def __login(self):
        """Log in to the UCI-Server using rest api to generate user's token"""

        payload = {'login': self.login, 'password': self.password}
        r = requests.post('{}{}'.format(self.uri, Endpoint.login.value), json=payload)

        if r.status_code == 200:
            response = r.json()

            if response.get('success', False):
                self.token = response['token']
                print('User logged in!\ttoken:{}'.format(self.token))
        else:
            raise Exception("Oops! Error on request {}{}.".format(self.uri, Endpoint.login.value))


    def __connect(self):
        """Connect to the sockets (to communicate with UCI-Server)"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.address, self.port))

            print("Successfully connected to the UCI-Server (sockets)!")
        except Exception as e:
            raise Exception("Oops! Can't connect to the UCI-Server (sockets) {}:{}. \n{}".format(self.address, self.port, e))

    def send(self):
        """Send message to the UCI-Server through the socket."""
        pass