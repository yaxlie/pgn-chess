import chess.pgn

class Game:
    """This class is used to manage games loaded from .pgn files."""

    def __init__(self, pgn_filepath):
        self.game = None

        try:
            self.load_game(pgn_filepath)
        except Exception as e:
            print("Oops! Can't load the game: {}".format(e))

    
    def load_game(self, pgn_filepath):
        pgn = open(pgn_filepath)
        self.game = chess.pgn.read_game(pgn)

        print('"{}" [{}] - game loaded.'.format(self.game.headers['Event'], self.game.headers['Date']))
