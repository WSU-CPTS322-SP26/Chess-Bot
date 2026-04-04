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
                self.game_state.messages.append(f"Selected: {chess.square_name(square)}")
            else:
                self.game_state.messages.append("Select a piece of your color.")

        else:
            # Create a move object from the first click to the second click
            move = chess.Move(self.selected_square, square)
            
            # Check if it's in board.legal_moves
            if move in board.legal_moves:
                board.push(move)
                self.game_state.messages.append(f"Move Executed: {move.uci()}")
                
                # Update the turn in our GameState
                self.game_state.turn = board.turn
                
            else:
                # If they click another of their own pieces, switch selection instead of failing
                new_piece = board.piece_at(square)
                if new_piece and new_piece.color == board.turn:
                    self.selected_square = square
                    self.game_state.messages.append(f"Switched Selection to: {chess.square_name(square)}")
                    return # Skip the reset below

                self.game_state.messages.append("Invalid Move!")
            
            # Always reset selection after a move attempt (pass or fail)
            self.selected_square = None

    def check_game_end(self):

        # Check for game end
        if self.game_state.board.outcome():

            # if termination info needed, get here
            # self.game_state.board.outcome().termination

            # winning color
            if self.game_state.board.outcome().winner == None:
                # Draw
                winning_color = ""
            elif self.game_state.board.outcome().winner:
                # white wins
                winning_color = "White"
            else:
                # Black wins
                winning_color = "Black"

            self.game_state.messages.append(f"{self.game_state.board.result()} {winning_color} by {str(self.game_state.board.outcome().termination).replace("Termination.", "")}")
            
            # tell input handler that game has ended
            return True

  