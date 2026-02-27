from dataclasses import dataclass

@dataclass
class MoveIntentEvent:
    from_square: int   # 0–63 (python-chess indexing)
    to_square: int

@dataclass
class QuitEvent:
    pass