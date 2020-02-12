import asyncio
from src.messengers.messenger import Messenger


class DummyMessenger(Messenger):
    def get_engine_data(self):
        engine_output_data = asyncio.get_event_loop().run_until_complete(self.send("Here you want to send the game to recieve data to explore from chess engine"))
        return engine_output_data
