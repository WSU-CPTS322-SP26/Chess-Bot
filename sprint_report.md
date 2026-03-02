# Sprint x Report (8/26/21 - 9/24/2021)

## What's New (User Facing)
 * A functional PyGame-based user interface capable of rendering a chess board
 * A main menu enabling basic application flow
 * Initial end-to-end wiring between the user interface and game logic

## Work Summary (Developer Facing)
During this sprint, the team completed the core architectural and functional foundations of the chess application. A fully wired PyGame-based user interface was implemented, including a main menu and chess board rendering. The UI was successfully connected to a modular core logic layer built on top of python-chess, enabling structured input handling, move validation, turn management, and state updates. Input from the UI is now correctly translated into core events and applied to the authoritative game state, with results propagated back to the UI. This sprint resulted in a complete, playable chess application framework, establishing a stable base for future AI and machine-learning integration.

## Unfinished Work
If applicable, explain the work you did not finish in this sprint. For issues/user stories in the current sprint that have not been closed, (a) any progress toward completion of the issues has been clearly tracked (by checking the checkboxes of  acceptance criteria), (b) a comment has been added to the issue to explain why the issue could not be completed (e.g., "we ran out of time" or "we did not anticipate it would be so much work"), and (c) the issue is added to a subsequent sprint, so that it can be addressed later.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * URL of issue 1
 * URL of issue 2
 * URL of issue n

 Reminders (Remove this section when you save the file):
  * Each issue should be assigned to a milestone
  * Each completed issue should be assigned to a pull request
  * Each completed pull request should include a link to a "Before and After" video
  * All team members who contributed to the issue should be assigned to it on GitHub
  * Each issue should be assigned story points using a label
  * Story points contribution of each team member should be indicated in a comment
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * URL of issue 1 <<One sentence explanation of why issue was not completed>>
 * URL of issue 2 <<One sentence explanation of why issue was not completed>>
 * URL of issue n <<One sentence explanation of why issue was not completed>>
 
 Examples of explanations (Remove this section when you save the file):
  * "We ran into a complication we did not anticipate (explain briefly)." 
  * "We decided that the feature did not add sufficient value for us to work on it in this sprint (explain briefly)."
  * "We could not reproduce the bug" (explain briefly).
  * "We did not get to this issue because..." (explain briefly)

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [Name of code file 1](https://github.com/your_repo/file_extension)
 * [Name of code file 2](https://github.com/your_repo/file_extension)
 * [Name of code file 3](https://github.com/your_repo/file_extension)
 
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