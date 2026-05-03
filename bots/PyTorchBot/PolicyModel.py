import torch
import torch.nn as nn


class PolicyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 4096)  # 64x64 move space
        )

    def forward(self, x):
        return self.net(x)