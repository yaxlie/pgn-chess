from src.messengers.dummy_messenger import DummyMessenger
from src.extractors.dummy_extractor import DummyExtractor


class Filter:
    def pass_filters(self, move, game, board, args, communicator):
        messenger = DummyMessenger(game, board, args, communicator.token, communicator.address,
                                   communicator.port)
        extractor = DummyExtractor()
        communicator.extract(messenger, extractor)
        return True