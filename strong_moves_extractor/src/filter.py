import chess
from src.messengers.best_moves_messenger import BestMovesMessenger
from src.extractors.best_moves_extractor import BestMovesExtractor


class Filter:
    def __init__(self):
        self.moves = None
        self.evaluations = None
        self.played = -1

    def clean(self):
        self.moves = None
        self.evaluations = None
        self.played = -1

    def check_played_move(self, move):
        for i in range(0, len(self.moves)):
            if chess.Move.from_uci(self.moves[i]) == move:
                self.played = i
                break

    def evaluate_position(self, move, game, board, args, communicator):
        self.clean()

        messenger = BestMovesMessenger(game, board, args, communicator.token, communicator.address,
                                       communicator.port)
        extractor = BestMovesExtractor()
        engine_output_data = messenger.get_engine_data(args.variations_number, args.depth)
        self.moves, self.evaluations = extractor.get_moves(engine_output_data, args.variations_number)

        self.check_played_move(move)

        print('\n---\nBest move: \n{}\n---'.format(self.moves))
        print('\n---\nEval: \n{}\n---'.format(self.evaluations))

    def min_difference_filter(self, args):
        if (int(self.evaluations[0]) - int(self.evaluations[1])) < args.centipawns:
            return False
        return True

    def difference_between_depth_filter(self, args, move, board, communicator, game):
        depth = 6
        eps = 100

        board.push(chess.Move.from_uci(self.moves[0]))
        messenger = BestMovesMessenger(game, board, args, communicator.token, communicator.address,
                                       communicator.port)
        extractor = BestMovesExtractor()
        engine_output_data = messenger.get_engine_data(1, depth)
        m, e = extractor.get_moves(engine_output_data, 1)
        print(m[0], " ", e[0])

        board.pop()

        if (int(self.evaluations[0]) + int(e[0])) > eps:
            return True

        return False

    def simple_capture_filter(self, move, board):
        if board.is_capture(move):
            board.push(move)
            for m in board.legal_moves:
                if m.uci()[-2:] == move.uci()[-2:]:
                    board.pop()
                    return True
            board.pop()
            return False
        return True

    def pass_filters(self, move, game, board, args, communicator):
        if self.min_difference_filter(args):
            if self.simple_capture_filter(move, board):
                if self.difference_between_depth_filter(args, move, board, communicator, game):
                    return True
        return False
