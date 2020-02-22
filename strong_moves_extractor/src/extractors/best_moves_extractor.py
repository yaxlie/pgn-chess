from src.extractors.extractor import Extractor


class BestMovesExtractor(Extractor):
    def __init__(self):
        pass

    def get_moves(self, engine_output_data, solutions):
        moves = []
        evaluations = []

        for i in range(solutions+1, 1, -1):
            evaluation = engine_output_data[-i].split()[9]
            move = engine_output_data[-i].split()[19]
            moves.append(move)
            evaluations.append(evaluation)
        return moves, evaluations
