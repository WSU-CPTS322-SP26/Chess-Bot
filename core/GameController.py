# Mediates between UI events to update GameState

import chess
from core.GameState import GameState

class GameController:
    def __init__(self, game_state: GameState, mode: str = "PVP", human_color: chess.Color = chess.WHITE):
        self.game_state = game_state
        self.mode = mode # PVP or PVB
        self.human_color = human_color

        self.selected_square = None

    def handle_square_click(self, square: chess.Square):
        board = self.game_state.board

        if self.selected_square is None:
            piece = board.piece_at(square)
            # Only allow selection if there is a piece and it's that color's turn
            if piece and piece.color == board.turn:
                self.selected_square = square
                print(f"Selected: {chess.square_name(square)}")
            else:
                print("Select a piece of your color.")

        else:
            # Create a move object from the first click to the second click
            move = chess.Move(self.selected_square, square)
            
            # Check if it's in board.legal_moves
            if move in board.legal_moves:
                board.push(move)
                print(f"Move Executed: {move.uci()}")
                
                # Update the turn in our GameState
                self.game_state.turn = board.turn
                
            else:
                # If they click another of their own pieces, switch selection instead of failing
                new_piece = board.piece_at(square)
                if new_piece and new_piece.color == board.turn:
                    self.selected_square = square
                    print(f"Switched Selection to: {chess.square_name(square)}")
                    return # Skip the reset below

                print("Invalid Move!")
            
            # Always reset selection after a move attempt (pass or fail)
            self.selected_square = None

  