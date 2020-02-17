import asyncio
from src.messengers.messenger import Messenger


class DummyMessenger(Messenger):
    def get_engine_data(self):

        dummy_command = '''ucinewgame
position fen {}
go depth {}
bestmove
'''.format(self.game.board().starting_fen, self.args.depth)

        engine_output_data = asyncio.get_event_loop().run_until_complete(self.send(dummy_command))
        return engine_output_data
