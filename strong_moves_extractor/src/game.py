import chess.pgn
import re

games_separator_regex = re.compile(r"(\[.*\]\W)+\n(.*\W(?!\[))+")

class Game:
    """This class is used to manage games loaded from .pgn files."""

    def __init__(self, pgn_filepath):
        self.games = []
        try:
            self.load_games(pgn_filepath)
        except Exception as e:
            print("Oops! Can't load the game: {}".format(e))

    
    def load_games(self, pgn_filepath):
        import io
        with open(pgn_filepath, encoding="utf-8-sig", errors='ignore') as data:
            raw_pgn = data.read()
            pgn_games = games_separator_regex.finditer(raw_pgn)

            for pgn in pgn_games:
                pgn_io = io.StringIO(pgn.string)
                self.games.append(chess.pgn.read_game(pgn_io))

            print(f'"{len(self.games)}" games loaded.')
