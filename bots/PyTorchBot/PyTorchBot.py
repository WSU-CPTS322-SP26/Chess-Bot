from pathlib import Path
import random
import torch
import torch.nn as nn
import chess


class TinyChessNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)


class PyTorchBot:
    def __init__(self, model_path=None, epsilon=0.1):
        self.device = torch.device("cpu")
        self.model = TinyChessNet().to(self.device)
        self.model.eval()

        self.epsilon = epsilon  # random move chance for variety

        if model_path:
            model_path = Path(model_path)
            if model_path.exists():
                self.model.load_state_dict(torch.load(model_path, map_location=self.device))

    def board_to_tensor(self, board: chess.Board):
        """
        Encoding:
        64 squares, each square is one number:
          white pawn   = 1
          white knight = 2
          white bishop = 3
          white rook   = 4
          white queen  = 5
          white king   = 6
          black pieces are negative
          empty = 0
        """
        piece_map = {
            chess.PAWN: 1,
            chess.KNIGHT: 2,
            chess.BISHOP: 3,
            chess.ROOK: 4,
            chess.QUEEN: 5,
            chess.KING: 6,
        }

        arr = torch.zeros(64, dtype=torch.float32)

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                value = piece_map[piece.piece_type]
                if piece.color == chess.BLACK:
                    value = -value
                arr[square] = float(value)

        return arr.unsqueeze(0).to(self.device)  # shape: [1, 64]

    def evaluate(self, board: chess.Board) -> float:
        # quick hard rules so it behaves sensibly
        if board.is_checkmate():
            return -9999.0 if board.turn == chess.WHITE else 9999.0
        if board.is_stalemate() or board.is_insufficient_material():
            return 0.0

        with torch.no_grad():
            x = self.board_to_tensor(board)
            score = self.model(x).item()
        return score

    def choose_move(self, board: chess.Board):
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return None

        # small randomness so it doesn't always play the same line
        if random.random() < self.epsilon:
            return random.choice(legal_moves)

        best_move = None

        if board.turn == chess.WHITE:
            best_score = float("-inf")
            for move in legal_moves:
                board.push(move)
                score = self.evaluate(board)
                board.pop()

                if score > best_score:
                    best_score = score
                    best_move = move
        else:
            best_score = float("inf")
            for move in legal_moves:
                board.push(move)
                score = self.evaluate(board)
                board.pop()

                if score < best_score:
                    best_score = score
                    best_move = move

        return best_move

    def save(self, path):
        torch.save(self.model.state_dict(), path)

    def close(self):
        pass