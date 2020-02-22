from src.extractors.extractor import Extractor


class BestMovesExtractor(Extractor):
    def __init__(self):
        pass

    def get_moves(self, engine_output_data, solutions):
        moves = []
        evaluations = []

        for i in range(solutions+1, 1, -1):
            data = engine_output_data[-i].split()
            evaluation = data[data.index("cp")+1]
            move = data[data.index("pv")+1]
            moves.append(move)
            evaluations.append(evaluation)
        return moves, evaluations
