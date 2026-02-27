import chess

class GameState:
    def __init__(self):
        self.board = chess.Board() # pull directly from Python chess
        self.turn = chess.WHITE # start with white
        self.move_history = [] # list to keep track of moves
        self.game_over = False # check for checkmate or stalemate

    def current_player(self):
        return self.turn

    def snapshot(self): # read only view of game
        
        return {
            "fen": self.board.fen(), # Current game state in line of text
            "turn": self.turn, # Who's current turn
            "legal_moves": list(self.board.legal_moves),
            "is_game_over": self.board.is_game_over()
        }
    