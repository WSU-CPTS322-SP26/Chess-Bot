from pathlib import Path
import random
import torch
import chess

from bots.PyTorchBot.ValueModel import ValueModel
from bots.PyTorchBot.PolicyModel import PolicyModel


class PyTorchBot:
    def __init__(self, value_model_path=None, policy_model_path=None, epsilon=0.1, top_k=5):
        self.device = torch.device("cpu")

        self.value_model = ValueModel().to(self.device)
        self.policy_model = PolicyModel().to(self.device)

        self.value_model.eval()
        self.policy_model.eval()

        self.epsilon = epsilon
        self.top_k = top_k

        if value_model_path:
            path = Path(value_model_path)
            if path.exists():
                self.value_model.load_state_dict(torch.load(path, map_location=self.device))

        if policy_model_path:
            path = Path(policy_model_path)
            if path.exists():
                self.policy_model.load_state_dict(torch.load(path, map_location=self.device))

    def board_to_tensor(self, board: chess.Board):
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
            if piece:
                val = piece_map[piece.piece_type]
                if piece.color == chess.BLACK:
                    val = -val
                arr[square] = float(val)

        return arr.unsqueeze(0).to(self.device)

    def move_to_index(self, move: chess.Move):
        return move.from_square * 64 + move.to_square

    def evaluate(self, board: chess.Board):
        if board.is_checkmate():
            return -9999.0 if board.turn == chess.WHITE else 9999.0

        if board.is_stalemate() or board.is_insufficient_material():
            return 0.0

        with torch.no_grad():
            x = self.board_to_tensor(board)
            return self.value_model(x).item()

    def rank_moves_with_policy(self, board: chess.Board):
        legal_moves = list(board.legal_moves)

        if not legal_moves:
            return []

        with torch.no_grad():
            x = self.board_to_tensor(board)
            scores = self.policy_model(x).squeeze(0)

        ranked = []
        for move in legal_moves:
            idx = self.move_to_index(move)
            ranked.append((move, scores[idx].item()))

        ranked.sort(key=lambda x: x[1], reverse=True)
        return [m for m, _ in ranked]

    def choose_move(self, board: chess.Board):
        legal_moves = list(board.legal_moves)

        if not legal_moves:
            return None

        if random.random() < self.epsilon:
            return random.choice(legal_moves)

        ranked_moves = self.rank_moves_with_policy(board)
        candidate_moves = ranked_moves[:self.top_k]

        best_move = None

        if board.turn == chess.WHITE:
            best_score = float("-inf")
            for move in candidate_moves:
                board.push(move)
                score = self.evaluate(board)
                board.pop()

                if score > best_score:
                    best_score = score
                    best_move = move
        else:
            best_score = float("inf")
            for move in candidate_moves:
                board.push(move)
                score = self.evaluate(board)
                board.pop()

                if score < best_score:
                    best_score = score
                    best_move = move

        return best_move

    def save_value_model(self, path):
        torch.save(self.value_model.state_dict(), path)

    def save_policy_model(self, path):
        torch.save(self.policy_model.state_dict(), path)

    def close(self):
        pass