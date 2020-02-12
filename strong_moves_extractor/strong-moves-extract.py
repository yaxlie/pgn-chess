from src.game import Game
from src.communicator import Communicator
from src.extractors.example_extractor import ExampleExtractor
import argparse
import json
import os

parser = argparse.ArgumentParser(description='Analyze non-trivial chess moves.')
parser.add_argument('-e', '--config', help='path to UCI Server configuration file (relative or absolute)', default="uciServer.json", type=str)

# Can't be -h due to conflicts (Why?) TODO:fix
parser.add_argument('-hd', '--headers', help='what headers should be put to output PGN file (all, concise, minimal)', default="minimal", type=str)
parser.add_argument('-cp', '--centipawns', help='min. required cp (centipawns) difference between best and second best move shown by the engine', default=50, type=int)
parser.add_argument('-d', '--depth', help='min engine search depth for best and second best move shown by the engine (in multivariation mode)', default=30, type=int)
parser.add_argument('-n', '--variations-number', help='number of variations in multi-variation mode', default=2, type=int)
parser.add_argument('args', nargs='*') # Input and output .PGN file path
args = parser.parse_args()

input_pgn_path = args.args[0] if len(args.args) > 0 else None
output_pgn_path = args.args[1] if len(args.args) > 1 else None

game = Game(input_pgn_path)


if os.path.exists(args.config):
    with open(args.config) as json_file:
        config = json.load(json_file)

    with Communicator(config) as communicator:
        communicator.extract(ExampleExtractor())
else:
    print("Config file ({}) doesn't exist!".format(args.config))
    exit()
    