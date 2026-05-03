import random
from pathlib import Path

import chess
import chess.pgn
import torch
import torch.nn as nn
import torch.optim as optim


BASE_DIR = Path(__file__).resolve().parent

PGN_PATH = BASE_DIR.parent / "TrainingData" / "lichess_db_standard_rated_2016-12.pgn"

SAVE_PATH = BASE_DIR.parent / "policy_model.pt"

MAX_POSITIONS = 50000
EPOCHS = 5
BATCH_SIZE = 256
LR = 0.001


class PolicyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 4096)
        )

    def forward(self, x):
        return self.net(x)


def board_to_tensor(board: chess.Board):
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
            value = piece_map[piece.piece_type]
            if piece.color == chess.BLACK:
                value = -value
            arr[square] = float(value)

    return arr


def move_to_index(move: chess.Move):
    return move.from_square * 64 + move.to_square


def load_training_data():
    X = []
    y = []

    with open(PGN_PATH, "r", encoding="utf-8", errors="ignore") as pgn:
        while len(X) < MAX_POSITIONS:
            game = chess.pgn.read_game(pgn)

            if game is None:
                break

            board = game.board()

            for move in game.mainline_moves():
                X.append(board_to_tensor(board))
                y.append(move_to_index(move))

                board.push(move)

                if len(X) >= MAX_POSITIONS:
                    break

    return torch.stack(X), torch.tensor(y, dtype=torch.long)


def train():
    print("Loading training data...")
    X, y = load_training_data()
    print(f"Loaded {len(X)} positions")

    model = PolicyModel()
    optimizer = optim.Adam(model.parameters(), lr=LR)
    loss_fn = nn.CrossEntropyLoss()

    for epoch in range(EPOCHS):
        indices = list(range(len(X)))
        random.shuffle(indices)

        total_loss = 0.0
        batches = 0

        for start in range(0, len(X), BATCH_SIZE):
            batch_indices = indices[start:start + BATCH_SIZE]

            xb = X[batch_indices]
            yb = y[batch_indices]

            optimizer.zero_grad()
            outputs = model(xb)
            loss = loss_fn(outputs, yb)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            batches += 1

        avg_loss = total_loss / batches
        print(f"Epoch {epoch + 1}/{EPOCHS}, Loss: {avg_loss:.4f}")

    torch.save(model.state_dict(), SAVE_PATH)
    print(f"Saved policy model to {SAVE_PATH}")


if __name__ == "__main__":
    train()