from src.game import Game
from src.communicator import Communicator
from src.extractors.example_extractor import ExampleExtractor
import argparse

parser = argparse.ArgumentParser(description='Analyze non-trivial chess moves.')
parser.add_argument('-i', '--input-pgn', help='Input .PGN file path', type=str)
parser.add_argument('-l', '--login', help='Login to the UCI-Server', default="test", type=str)
parser.add_argument('-p', '--password', help='Password to the UCI-Server', default="111111", type=str)
parser.add_argument('-a', '--address', help='Address of UCI-Server', default="localhost", type=str)
parser.add_argument('--port', help='Port of UCI-Server', default=80, type=int)

args = parser.parse_args()

game = Game(args.input_pgn)

communicator = Communicator(args.address, args.port, args.login, args.password)
communicator.extract(ExampleExtractor())
    