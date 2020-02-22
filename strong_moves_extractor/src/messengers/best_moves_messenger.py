import asyncio
from src.messengers.messenger import Messenger


class BestMovesMessenger(Messenger):
    def get_engine_data(self, solutions, depth):

        best_move_command = '''ucinewgame
position fen {}
setoption name MultiPV value {}
go depth {}'''.format(self.board.fen(), solutions, depth)

        engine_output_data = asyncio.get_event_loop().run_until_complete(self.send(best_move_command))
        return engine_output_data
