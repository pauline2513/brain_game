from src.cli import welcome_func
from src.engine import run_game
from src.games.geometric_progression import geometric_progression
from src.games.least_common_multiple import least_common_multiple


def main():
    name = welcome_func()
    while True:
        print("Choose game mode (enter the number from 1 to 3):\n"
              "1: least common multiple\n"
              "2: geometric progression\n"
              "3: exit")
        game_mode = input("Your game mode: ").strip()
        if game_mode == '1':
            run_game(least_common_multiple, name)
        elif game_mode == '2':
            run_game(geometric_progression, name)
        elif game_mode == '3':
            print(f"Goodbye, {name}!")
            return
        else:
            game_mode = input("Try again: ").strip()


if __name__ == "__main__":
    main()
