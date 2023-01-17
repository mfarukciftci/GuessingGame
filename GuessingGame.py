import random


def play_game():
    text = "Welcome to our game. Would you like to play with us? So lets start? Numbers are between 1 and 10."
    print(text)
    total_guess = 0
    total_games = 0
    no = {"no", "okay", 0, "hello"}

    def statics():
        print(f"""
            total game : {total_games}
            total gueses : {total_guess}
            Guess/game : {guess_game}

            """)

    while True:
        computer = random.randrange(1, 10)
        guess = 0
        total_games += 1
        while True:
            user = int(input("Please write number: "))

            if user < computer:
                guess += 1
                print("It's higher")
            elif user > computer:
                guess += 1
                print("It's lower")
            elif computer == user:
                guess += 1
                print(f"Congralations, You got it in {guess} right")
                total_guess += guess
                break
            else:
                print("Plesea right a number")

        more_game = input("Do you wanna play 1 more game?:(Type no for quit. ) ")
        more_game.lower()

        if more_game in no:
            guess_game = total_guess / total_games
            print("Thank you for playing.")
            statics()
            break
        else:
            continue


play_game()

