
class Saver:
    def save(self, fen, moves, evaluations, played, headers, filename):
        with open(filename + '.pgn', 'w+') as pgn:
            for header in headers:
                pgn.write(header)
            pgn.write("[FEN \"" + fen + "\"")
            halfmove = fen[-2:]

            best_move = halfmove + ". " + moves[0] + " {" + evaluations[0] + "}"
            if played == 0:
                best_move += "{G}"

            next_moves = ""
            for i in range(1, len(moves)):
                next_moves += "(" + halfmove + ". " + moves[i] + " {" + evaluations[i] + "}"
                if i == played:
                    next_moves += "{G}"
                next_moves += "}"

            pgn.write(best_move + " " + next_moves + " *")