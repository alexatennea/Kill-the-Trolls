from classes.gamewindow import GameWindow
from classes.gameplay import play_game

def main():
    game_window = GameWindow()
    game_window.write("Welcome to Troll Slayer!\n\n")
    play_game(game_window.write, game_window.read, game_window)
    game_window.mainloop()

if __name__ == "__main__":
    main()