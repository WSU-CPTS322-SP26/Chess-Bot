
# Machine Learning Chess Bot

## Project summary

### One-sentence description of the project

A Python-based chess application that allows a human player to play against an automated chess bot, combining a graphical user interface with rule-based game logic and future machine-learning–driven decision making.

### Additional information about the project

This project is a semester-long software engineering effort developed as part of CptS 322 – Software Engineering Principles I at Washington State University. The goal is to design and implement a complete chess application featuring a clean graphical interface, full chess rules enforcement, and an AI-controlled opponent.

The system is being developed incrementally over multiple sprints. Initial work focuses on building a stable UI, core game architecture, and integration with an existing chess rules engine. Later phases introduce AI inference, search algorithms, and optional machine-learning–based evaluation models. Emphasis is placed on modular design, separation of concerns, and maintainability.

## Installation

### Prerequisites

Before installing and running this project, ensure you have the following installed:
- Python 3.10 or newer
- pip (Python package manager)
- git
- A system capable of running PyGame

### Add-ons

This project currently uses the following third-party libraries
- pygame: Used for rendering UI, handling window creation, drawing chess board, and processing user input
- python-chess: Used for chess board representation, legal move generation, move validation, and detection of game-end

Note: Machine learning libraries (e.g., PyTorch) are planned for later sprints but are not yet required to run current prototype.

### Installation Steps

1. Clone repository
  - git clone https://github.com/WSU-CPTS322-SP26/Chess-Bot
2. Install required Python packages
  - pip install pygame python-chess
  - pip install torch
3. Install Stockfish Bot .exe into /bots/StockfishBot/bin
4. Run the application
  - python main.py


## Functionality

Current Functionality
- Application launches successfully via main.py
- Graphical window rendered using PyGame
- Chess board rendered as an 8x8 grid with alternating colors
- Clean separation between UI rendering and application initialization
- Chess bot game modes play


## Known Problems

TODO: Describe any known issues, bugs, odd behaviors or code smells. 
Provide steps to reproduce the problem and/or name a file or a function where the problem lives.

When mapping board squares to chess objects:

The pygame library starts its origin in the top left of the board. This created a weird interaction during the initial implementation because squares were being designated from the wrong parts of the board. After understanding this nuance, a small change (rank = 7 - row ) flipped the board vertically allowing the board to start in the correct position when creating square objects. We will have to be mindful of this small detail if we decide to manipulate this implementation in some way.

When playing a game, pawn promotion will be considered an invalid move and will not allow piece promotion


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Additional Documentation

Sprint Report 2: sprint_report2.md

Chess pieces recieved from: https://commons.wikimedia.org/wiki/File:Chess_Pieces_Sprite.svg

Demo Video

Sprint 1: Isaac Shim - https://youtu.be/Nu-bxFxZKjs

Sprint 2: Lyndell Martin, Johnny Huang - https://youtu.be/6S5otcZksos

## License

This project is released under the MIT License.

See the LICENSE.txt file for full license details.