def welcome(name):
    return f"Hello {name} and welcome to the World Of Games(WoG)." \
           f"Here you can find many cool games to play."


def load_game():
    choice = 4
    difficulty = 6
    while 1 > choice or choice > 3:
        try:
            choice = int(input("Please choose a game to play:\n"
                               "1. Memory Game\n"
                               "2. Guess Game\n"
                               "3. Currency Roulette\n"))
        except Exception as ex:
            print("Incorrect Input")

    while 1 > difficulty or difficulty > 5:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
        except Exception as ex:
            print("Incorrect Input")
