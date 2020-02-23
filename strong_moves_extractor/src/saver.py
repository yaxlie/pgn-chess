import os

class Saver:

    def __init__(self, path):
        self.path = path
        
        if not os.path.exists(path):
            with open(os.path.join(path), 'w'):
                pass
    
    def new_game(self):
        with open(self.path, 'a+') as pgn:
            pgn.write("\n")

    def save(self, fen, moves, evaluations, played, headers):
        with open(self.path, 'a+') as pgn:
            for header in headers:
                pgn.write(header + '\n')
            pgn.write("[FEN \"" + fen + "\"]")
            halfmove = fen[-2:]

            best_move = halfmove + ". " + moves[0] + " {" + evaluations[0] + "}"
            if played == 0:
                best_move += "{G}"

            next_moves = ""
            for i in range(1, len(moves)):
                next_moves += "(" + halfmove + ". " + moves[i] + " {" + evaluations[i] + "}"
                if i == played:
                    next_moves += "{G}"
                next_moves += ")"

            pgn.write(best_move + " " + next_moves + " *\n")