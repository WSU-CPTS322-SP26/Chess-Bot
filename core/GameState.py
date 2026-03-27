import chess

class GameState:
    def __init__(self):
        self.reset()
        self.messages = []
        
    def reset(self): # put board into initial state
        self.board = chess.Board()
        self.turn = chess.WHITE
        self.move_history = []
        self.game_over = False

    def snapshot(self): # read only view of game
        
        return {
            "fen": self.board.fen(), # Current game state in line of text
            "turn": self.turn, # Who's current turn
            "legal_moves": list(self.board.legal_moves),
            "is_game_over": self.board.is_game_over()
        }
    