from src.messengers.best_moves_messenger import BestMovesMessenger
from src.extractors.best_moves_extractor import BestMovesExtractor


class Filter:
    def __init__(self):
        self.moves = None
        self.evaluations = None
        self.played = 0

    def clean(self):
        self.moves = None
        self.evaluations = None
        self.played = 0

    def pass_filters(self, move, game, board, args, communicator):

        self.clean()

        messenger = BestMovesMessenger(game, board, args, communicator.token, communicator.address,
                                   communicator.port)
        extractor = BestMovesExtractor()
        engine_output_data = messenger.get_engine_data(args.variations_number)
        self.moves, self.evaluations = extractor.get_moves(engine_output_data, args.variations_number)

        print('\n---\nBest move: \n{}\n---'.format(self.moves))
        print('\n---\nEval: \n{}\n---'.format(self.evaluations))

        return True
