from src.game import Game
import argparse

parser = argparse.ArgumentParser(description='Analyze non-trivial chess moves.')
parser.add_argument('-i', '--input-pgn', help='input .PGN file path', type=str)

args = parser.parse_args()

game = Game(args.input_pgn)