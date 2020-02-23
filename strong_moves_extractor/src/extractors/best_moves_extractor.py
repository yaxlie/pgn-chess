from src.extractors.extractor import Extractor


class BestMovesExtractor(Extractor):
    def __init__(self):
        pass

    def get_moves(self, engine_output_data, solutions, played_move):
        moves = []
        evaluations = []

        for i in range(solutions+1, 1, -1):
            data = engine_output_data[-i].split()
            if "cp" in data:
                evaluation = data[data.index("cp")+1]
            else:
                evaluation = 10000
            if 'pv' in data:
                move = data[data.index("pv")+1]
            else:
                move = played_move.uci()
            moves.append(move)
            evaluations.append(evaluation)
        return moves, evaluations
