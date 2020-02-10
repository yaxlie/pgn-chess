import abc

class Extractor(abc.ABC):
    @abc.abstractmethod
    def get_moves(self, engine_output_data):
        """Analyze, extract and return strong moves from engine's output data"""
        pass
