from src.extractors.extractor import Extractor


class DummyExtractor(Extractor):
    def __init__(self):
        pass

    def get_moves(self, engine_output_data):
        output='\n\t< '
        # print(f'\t< {output.join(engine_output_data)}')
        example_moves = [engine_output_data[-1]]
        return example_moves