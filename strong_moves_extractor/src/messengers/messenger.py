import abc
import websockets
import asyncio
from src.endpoints import Endpoint

timeout = 2 # in seconds

# Primitive version... TODO: Long-lived connection with events
# https://pypi.org/project/websocket_client/
class Messenger(abc.ABC):
    def __init__(self, token, address, port):
        self.token = token
        self.address = address
        self.port = port

    async def send(self, msg):
        """Send a message through websockets"""

        headers = {"Authorization": "Bearer {}".format(self.token)}
        url = 'ws://{}:{}{}'.format(self.address, str(self.port), Endpoint.sockets.value)

        try:
            print('\nSending message...')
            async with websockets.connect(url, extra_headers=headers) as websocket:
                await websocket.send(msg)
                print(f"\n\t> {msg}")

                response = []

                # TODO: Long-lived connection with events
                while True:
                    try:
                        r = await asyncio.wait_for(websocket.recv(), timeout=timeout)
                        if len(r) == 0:
                            break
                        else:
                            response.append(r)
                    except asyncio.TimeoutError:
                        break

                return response

        except Exception as e:
            raise Exception("\nOops! Can't send the message through websockets {}. \n{}".format(url, e))


    @abc.abstractmethod
    def get_engine_data(self):
        """Send instructions through sockets and get data to extract some moves"""

        pass
