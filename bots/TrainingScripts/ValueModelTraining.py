import pandas as pd
import torch
import torch.nn as nn
import chess

# Create neural network for training
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


def board_to_tensor(board):
    piece_map = {
        chess.PAWN: 1,
        chess.KNIGHT: 2,
        chess.BISHOP: 3,
        chess.ROOK: 4,
        chess.QUEEN: 5,
        chess.KING: 6,
    }

    arr = torch.zeros(64)

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            val = piece_map[piece.piece_type]
            if piece.color == chess.BLACK:
                val = -val
            arr[square] = val

    return arr


def normalize(cp):
    # simple scaling
    return max(-1.0, min(1.0, cp / 300.0))

# start grabbing data
print("Loading data...")
df = pd.read_parquet(r"C:\Users\lmart\OneDrive\Desktop\train-00000-of-00017.parquet")

# take a smaller sample
df = df.sample(50000)

model = TinyChessNet()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

print("Training...")

for epoch in range(3):  # keep small
    total_loss = 0

    for row in df.itertuples():
        board = chess.Board(row.fen)

        # skip mates (already knows for the next move)
        if row.mate is not None:
            continue

        x = board_to_tensor(board)
        y = normalize(row.cp)

        if board.turn == chess.BLACK:
            y = -y

        x = x.unsqueeze(0)
        y = torch.tensor([[y]], dtype=torch.float32)

        pred = model(x)
        loss = loss_fn(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, loss: {total_loss:.2f}")

# save model
torch.save(model.state_dict(), "model.pt")
print("Saved model.pt")