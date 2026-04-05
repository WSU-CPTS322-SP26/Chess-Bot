# Sprint 2 Report (3/02/2026 - 4/04/2026)

## What's New (User Facing)
 * A panel that displays moves with a load, save and return to menu button
 * Two added bot gamemodes playing against stockfish and our homemade bot
 * Improved quality of life UI improvements including game result indication


## Work Summary (Developer Facing)
Added two bots: our homemade PyTorch bot and Stockfish Bot and added load and save game via PGN files with a dedicated folder 
with PGNs. 

## Unfinished Work
Save game will be put onto next sprint.

## Completed Issues/User Stories
 * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/5
 * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/14
 * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/13

 
## Incomplete Issues/User Stories
Here are links to issues we worked on but did not complete in this sprint:

   * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/6 
   The save game had been harder than expected and does not fully function as intended
   * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/12
   The additional UI appearance was not necessary in the main focus of the bot so this issue has been delayed
   * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/16 
   This unexpected game logic issue appeared was unexpected before more games were testted, so we did not have time to look further into this issue
   * https://github.com/WSU-CPTS322-SP26/Chess-Bot/issues/17
   Load game works but does not have the functionality we would like and needs to be looked over more

 


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
* [StockfishBot.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/bots/StockfishBot/StockfishBot.py)
 * [PyTorchBot.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/bots/PyTorchBot/PyTorchBot.py)
 * [main.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/main.py)
 * [MainMenu.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/ui/MainMenu.py)
 * [InputHandler.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/ui/InputHandler.py)
 * [BoardDisplay.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/ui/BoardDisplay.py)
 * [GameState.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/core/GameState.py)
 * [GameController.py](https://github.com/WSU-CPTS322-SP26/Chess-Bot/blob/main/core/GameState.py)
 


## Retrospective Summary
Here's what went well:
  * Bot with chess.engine was implemented smoothly
  * Load game easily continued play from a pgn file
  * 
 
Here's what we'd like to improve:
   * Thorough chess game logic
   * 
   * 
  
Here are changes we plan to implement in the next sprint:
   * Improved PyTorch chess bot logic
   * Fix outlier game logic
   * 