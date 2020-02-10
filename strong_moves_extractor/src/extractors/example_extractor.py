from src.extractors.extractor import Extractor\


class ExampleExtractor(Extractor):
    def __init__(self):
        pass

    def get_moves(self, engine_output_data):
        example_moves = ['a2a3', 'a2a4', 'b2b3', 'b2b4']
        return example_moves