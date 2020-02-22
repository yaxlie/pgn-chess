from src.extractors.extractor import Extractor


class BestMovesExtractor(Extractor):
    def __init__(self):
        pass

    def get_moves(self, engine_output_data, solutions):
        moves = []
        evaluations = []

        for i in range(solutions+1, 1, -1):
            data = engine_output_data[-i].split()
            if "cp" in data:
                evaluation = data[data.index("cp")+1]
            else:
                evaluation = 10000
            move = data[data.index("pv")+1]
            moves.append(move)
            evaluations.append(evaluation)
        return moves, evaluations
