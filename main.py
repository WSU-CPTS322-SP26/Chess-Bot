from ui.window import GameWindow
from core.game_state import GameState

def main():
    state = GameState()
    window = GameWindow(state)

    running = True
    while running:
        events = window.poll_events()

        for event in events:
            if event.__class__.__name__ == "QuitEvent":
                running = False
            else:
                window.handle_event(event)

        window.render()

if __name__ == "__main__":
    main()