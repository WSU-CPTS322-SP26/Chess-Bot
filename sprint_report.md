# Sprint 1 Report (2/01/2026 - 3/01/2026)

## What's New (User Facing)
 * A functional PyGame-based user interface capable of rendering a chess board
 * A main menu enabling basic application flow
 * Initial end-to-end wiring between the user interface and game logic

## Work Summary (Developer Facing)
During this sprint, the team completed the core architectural and functional foundations of the chess application. A fully wired PyGame-based user interface was implemented, including a main menu and chess board rendering. The UI was successfully connected to a modular core logic layer built on top of python-chess, enabling structured input handling, move validation, turn management, and state updates. Input from the UI is now correctly translated into core events and applied to the authoritative game state, with results propagated back to the UI. This sprint resulted in a complete, playable chess application framework, establishing a stable base for future AI and machine-learning integration.

## Unfinished Work
Declaring checkmate and game end will be added to the next sprint instead. 

## Completed Issues/User Stories
N/A: Not many issues that could not be self-completed

 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/3#issue-4009818235 "We decided that as for this sprint, this feature did not need to be completed since it did not add much to the main sprint 1 goal"


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [main.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/main.py)
 * [MainMenu.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/ui/MainMenu.py)
 * [InputHandler.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/ui/InputHandler.py)
 * [BoardDisplay.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/ui/BoardDisplay.py)
 * [GameState.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/core/GameState.py)
 * [GameController.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/core/GameState.py)

## Retrospective Summary
Here's what went well:
  * Functioning board that is fully playable.
  * Although it's simple it's aesthetically pleasing and easy to understand as well as navigate. 
  * Move validation is tested and working correctly. 
 
Here's what we'd like to improve:
   * A way to display moves selected and moves made. Currently all the information about move validation and updates about piece locations are only displayed in the terminal. 
   * Menu UI.
   * Bigger window for actual gameplay containing spaces for more information.
  
Here are changes we plan to implement in the next sprint:
   * Plan to add status update displaying current status eg. Checkmate, check, tie, draw.
   * Display the move validation information in the same window as the board.
   * Improved menu UI. Perhaps more color, cleaner fonts, etc. 