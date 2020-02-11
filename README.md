# pgn-chess
Analyze non-trivial chess moves

# Setup

### UCI-Server
UCI-Server is required.  
You can get it from http://www.cs.put.poznan.pl/mszelag/Software/software.html

### Windows (tested on python 3.7.3)

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
python strong_moves_extractor\strong-moves-extract.py "path_to_pgn_file"
```

### Linux

todo

