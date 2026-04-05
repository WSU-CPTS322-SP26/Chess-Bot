# Mediates between UI events to update GameState
import chess
from core.GameState import GameState
from bots.StockfishBot.StockfishBot import StockfishBot
from bots.PyTorchBot.PyTorchBot import PyTorchBot
import chess.pgn
from pathlib import Path

class GameController:
    def __init__(self, game_state: GameState, mode: str = "PVP", human_color: chess.Color = chess.WHITE):
        self.game_state = game_state
        self.mode = mode # PVP or PVB
        self.human_color = human_color

        self.selected_square = None

        self.bot = None
        if self.mode == "PVBS":
            self.bot = StockfishBot() # create the bot instance if it is selected
        elif self.mode == "PVBH":
            self.bot = PyTorchBot()
        

    def handle_square_click(self, square: chess.Square):
        board = self.game_state.board

        # no human input on bot's turn
        if self.bot and board.turn != self.human_color:
            return False

        if self.selected_square is None:
            piece = board.piece_at(square)
            # Only allow selection if there is a piece and it's that color's turn
            if piece and piece.color == board.turn:
                self.selected_square = square
                self.game_state.messages.append(f"Selected: {chess.square_name(square)}")
            else:
                self.game_state.messages.append("Select a piece of your color.")
            return False

        else:
            # Create a move object from the first click to the second click
            move = chess.Move(self.selected_square, square)
            
            # Check if it's in board.legal_moves
            if move in board.legal_moves:
                board.push(move)
                self.game_state.messages.append(f"Move Executed: {move.uci()}")
                
                # Update the turn in our GameState
                self.game_state.turn = board.turn

                #reset selection after successful move
                self.selected_square = None
                return True
                
            else:
                # If they click another of their own pieces, switch selection instead of failing
                new_piece = board.piece_at(square)
                if new_piece and new_piece.color == board.turn:
                    self.selected_square = square
                    self.game_state.messages.append(f"Switched Selection to: {chess.square_name(square)}")
                    return False

                self.game_state.messages.append("Invalid Move!")
            
            # Always reset selection after a move attempt (pass or fail)
            self.selected_square = None
            return False

    def check_game_end(self):
        outcome = self.game_state.board.outcome()
        # Check for game end
        if outcome:
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

            self.game_state.messages.append(f"{self.game_state.board.result()} {winning_color} by {str(self.game_state.board.outcome().termination).replace('Termination.', '')}")
            
            # tell input handler that game has ended
            return True
    
    def make_bot_move(self):
        if self.bot is None:
            return False

        if self.game_state.board.is_game_over():
            return False

        # Only move if it is bot's turn
        if self.game_state.board.turn != self.human_color:
            move = self.bot.choose_move(self.game_state.board)
            self.game_state.board.push(move)
            self.game_state.turn = self.game_state.board.turn
            bot_name = "Stockfish" if isinstance(self.bot, StockfishBot) else "PyTorch bot"
            self.game_state.messages.append(f"{bot_name} played: {move.uci()}")
            return True

        return False

    #close the bot
    def close(self):
        if self.bot is not None:
            self.bot.close()

    def load_game(self):
        # Define folder 
        pgn_folder = Path("data/pgn")
        #file_path = pgn_folder / "MidwayThroughExample.pgn" # replace with incoming file path
        file_path = pgn_folder / "MidwayTextExample.txt" # replace with incoming file path

        # open file of source pgn
        with open(file_path) as pgn: 
            # read pgn 
            loaded_game = chess.pgn.read_game(pgn)

            # iterate through moves and play them on the board
            board = loaded_game.board()
            for move in loaded_game.mainline_moves():
                board.push(move)

            self.game_state.board = loaded_game.board()
        self.game_state.messages.append(f"Game Loaded")

    
    def save_game(self):
        current_save = chess.pgn.Game()

        # save pgn in folder
        new_pgn = open("data/pgn/local.pgn", "w", encoding="utf-8")
        exporter = chess.pgn.FileExporter(new_pgn)
        current_save.accept(exporter)

        # close file
        new_pgn.close()
        self.game_state.messages.append(f"Game saved")
