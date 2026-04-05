import os
from pathlib import Path
import chess
import chess.engine

class StockfishBot:
    def __init__(self):
        path = Path(__file__).resolve().parent / "bin" / "stockfish-windows-x86-64-avx2.exe" # filepath to the stockfish bot
        self.engine = chess.engine.SimpleEngine.popen_uci(str(path)) # open the exe as an engine

    def choose_move(self, board):
        return self.engine.play(board, chess.engine.Limit(time=0.2)).move

    def close(self):
        self.engine.quit()