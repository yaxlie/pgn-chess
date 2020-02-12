import socket
import requests
from src.helpers import get_url_groups
from src.endpoints import Endpoint
from src.extractors.extractor import Extractor

class Communicator:
    """This class is used to communicate with uci-server by sockets."""

    def __init__(self, config):
        self.url = config.get('url')
        self.protocol, self.address, self.port = get_url_groups(self.url)
        self.login = config.get('login')
        self.password = config.get('password')
        self.engine = config.get('engine')

        self.socket = None
        self.token = None

        try:
            self.__login()
            self.__engine_start()
            self.__connect()
        except Exception as e:
            print(e)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        try:
            self.__engine_stop()
            self.socket.close()
            self.__logout()

            print('\n---------\n')
        except Exception as e:
            print(e)

    # TODO: Create custom Exceptions and make a proper use of them.
    def __login(self):
        """Log in to the UCI-Server using rest api to generate user's token"""

        payload = {'login': self.login, 'password': self.password}
        r = requests.post('{}{}'.format(self.url, Endpoint.login.value), json=payload)

        if r.status_code == 200:
            response = r.json()

            if response.get('success', False):
                self.token = response['token']
                print('\nUser logged in!\ttoken:{}'.format(self.token))
        else:
            raise Exception("\nOops! Error on request {}{}.".format(self.url, Endpoint.login.value))


    def __logout(self):
        r = requests.get('{}{}'.format(self.url, Endpoint.logout.value))

        if r.status_code == 200:
            print('User has been logged out')
        else:
            raise Exception("\nOops! Can't log out.")


    def __connect(self):
        """Connect to the sockets (to communicate with UCI-Server)"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.address, self.port))

            print("\nSuccessfully connected to the UCI-Server (sockets)!")
        except Exception as e:
            raise Exception("\nOops! Can't connect to the UCI-Server (sockets) {}:{}. \n{}".format(self.address, self.port, e))
    

    def __engine_start(self):
        payload = {'engine': self.engine.get('name')}
        headers = {"Authorization": "Bearer {}".format(self.token)}

        r = requests.post('{}{}'.format(self.url, Endpoint.engine_start.value), json=payload, headers=headers)

        if r.status_code == 200:
            response = r.json()

            print('\nServer response: {}'.format(response.get('info')))
        else:
            raise Exception("Oops! Server has some problems starting the chess engine.")


    def __engine_stop(self):
        payload = {'engine': self.engine.get('name')}
        headers = {"Authorization": "Bearer {}".format(self.token)}

        r = requests.post('{}{}'.format(self.url, Endpoint.engine_stop.value), json=payload, headers=headers)

        if r.status_code == 200:
            response = r.json()

            print('\nServer response: {}'.format(response.get('info')))
        else:
            raise Exception("\nOops! Server has some problems stopping the chess engine.")


    def send(self):
        """Send message to the UCI-Server through the socket."""
        pass


    def extract(self, extractor:Extractor):
        engine_output_data = None #TODO: get output from engine (Stockfish)

        moves = extractor.get_moves(engine_output_data)
        print('\n---\nThose are some sick moves: \n{}\n---'.format(moves))