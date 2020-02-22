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
        depth = 4
        eps = 150

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

    def get_int_file(self, file):
        if file == 'a':
            return 0
        if file == 'b':
            return 1
        if file == 'c':
            return 2
        if file == 'd':
            return 3
        if file == 'e':
            return 4
        if file == 'f':
            return 5
        if file == 'g':
            return 6
        if file == 'h':
            return 7

    def simple_gain_or_exchange_filter(self, move, board):
        if board.is_capture(move):
            m = board.lan(move)
            if len(m) == 5:
                starting_file = self.get_int_file(m[0])
                starting_rank = int(m[1])-1
                start_square = chess.square(starting_file, starting_rank)

                ending_file = self.get_int_file(board.lan(move)[3])
                ending_rank = int(board.lan(move)[4]) - 1
                end_square = chess.square(ending_file, ending_rank)

            elif len(m) == 6:

                if m[-1] == '+' or m[-1] == '#':

                    starting_file = self.get_int_file(m[0])
                    starting_rank = int(m[1])-1
                    start_square = chess.square(starting_file, starting_rank)

                    ending_file = self.get_int_file(board.lan(move)[3])
                    ending_rank = int(board.lan(move)[4]) - 1
                    end_square = chess.square(ending_file, ending_rank)
                else:
                    starting_file = self.get_int_file(m[1])
                    starting_rank = int(m[2]) - 1
                    start_square = chess.square(starting_file, starting_rank)

                    ending_file = self.get_int_file(board.lan(move)[4])
                    ending_rank = int(board.lan(move)[5]) - 1
                    end_square = chess.square(ending_file, ending_rank)

            elif len(m) == 7:
                starting_file = self.get_int_file(m[1])
                starting_rank = int(m[2]) - 1
                start_square = chess.square(starting_file, starting_rank)

                ending_file = self.get_int_file(board.lan(move)[4])
                ending_rank = int(board.lan(move)[5]) - 1
                end_square = chess.square(ending_file, ending_rank)

            else:
                raise Exception("LAN length > 7?")

            my_piece = board.piece_at(start_square)
            enemy_piece = board.piece_at(end_square)

            if self.is_worse_or_equal(my_piece, enemy_piece):
                return False
            return True
        return True

    def pass_filters(self, move, game, board, args, communicator):
        if self.min_difference_filter(args):
            if self.simple_capture_filter(move, board):
                if self.simple_gain_or_exchange_filter(move, board):
                    if self.difference_between_depth_filter(args, move, board, communicator, game):
                        return True
        return False

    def is_worse_or_equal(self, my_piece, enemy_piece):
        my_score = 0
        enemy_score = 0

        if my_piece.piece_type == 1:
            my_score = 0
        elif my_piece.piece_type == 2 or my_piece.piece_type == 3:
            my_score = 1
        elif my_piece.piece_type == 4:
            my_score = 2
        elif my_piece.piece_type == 5:
            my_score = 3

        if enemy_piece.piece_type == 1:
            enemy_score = 0
        elif enemy_piece.piece_type == 2 or enemy_piece.piece_type == 3:
            enemy_score = 1
        elif enemy_piece.piece_type == 4:
            enemy_score = 2
        elif enemy_piece.piece_type == 5:
            enemy_score = 3

        if my_score > enemy_score:
            return False
        return True
