from src.game import Game
from src.communicator import Communicator
from src.filter import Filter
from src.saver import Saver
import argparse
import json
import os


def get_headers(game, args):
    headers = []

    if args.headers == "all":
        for header in game.headers:
            tmp = game.headers[header]
            tmp = "[" + header + " " + "\"" + tmp + "\"" + "]"
            headers.append(tmp)
    elif args.headers == "concise":
        selected_headers = ["White", "Black", "Site", "Date"]
        for header in selected_headers:
            tmp = game.headers[header]
            tmp = "[" + header + " " + "\"" + tmp + "\"" + "]"
            headers.append(tmp)

    return headers


def calculate_time_for_messenger(depth):
    if depth < 21:
        return 4
    if depth < 26:
        return 8
    if depth < 32:
        return 13
    return 17


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

games = Game(input_pgn_path).games
filter = Filter()
saver = Saver(output_pgn_path)
time = calculate_time_for_messenger(args.depth)

if os.path.exists(args.config):
    with open(args.config) as json_file:
        config = json.load(json_file)

    for game in games:
        board = game.board()
        headers = get_headers(game, args)
        with Communicator(config) as communicator:
            for move in game.mainline_moves():
                filter.evaluate_position(move, game, board, args, communicator, time)
                if filter.pass_filters(move, game, board, args, communicator, time):
                    saver.save(board.fen(), filter.moves, filter.evaluations, filter.played, headers)
                    print("Writing fen: ", board.fen)
                board.push(move)
        saver.new_game()   
else:
    print("Config file ({}) doesn't exist!".format(args.config))
    exit()
