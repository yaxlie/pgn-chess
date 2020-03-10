# pgn-chess
Identify strong, non-trivial moves in a series of chess games from a chess database written to a PGN-compatible file.

# Setup

### UCI-Server
UCI-Server is required.  
You can get it from http://www.cs.put.poznan.pl/mszelag/Software/software.html

!! You have to download a chess engine e.g. [Stockfish 11](https://stockfishchess.org/)

### Running (tested on python 3.7.3)

1. Open console window f.e. Cmder
2. Go to the project localization:
```
cd *path_to_the_project*
``` 
3. Create virtual environment:
```
python -m venv .env
```
4. Activate:
```
.env\Scripts\activate.bat
```
5. Install required libs
```
pip install -r requirements.txt
```
6. Start the program
```
python strong_moves_extractor\strong-moves-extract.py "path_to_input_pgn_file" "path_to_output_pgn_file"
```

All command line parameters are available by setting ```--help``` argument.