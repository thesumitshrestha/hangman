# Hangman Project

import random


# Random Word from words.txt file
def getRandomWord():
    return random.choice(open('words.txt').read().split())


# Play Game
def play_game(answer, username):
    print("-------------------")
    print(f"Welcome {username}")
    print("Let's Play Hangman.")
    print("-------------------")
    lives_remaining = 0
    guessed_letters = []
    answer_progress = list("_" * len(answer))
    while lives_remaining <= 7:
        guess_char = input('Guess a letter: ').strip()
        if len(guess_char) > 1:
            print('Invalid Letter!')
            print('Try again!')

        elif guess_char not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')

        elif guess_char in guessed_letters:
            print("Oops! You already guessed ", guess_char)
            print('Letter guessed: ', ",".join(guessed_letters))
            print('\n')

        else:
            if guess_char in answer:
                print('The guess was RIGHT!!')
                hangman_hanged(lives_remaining, answer, username)
                guessed_letters.append(guess_char)
                correct_answer = progress_words(
                    guess_char, answer, answer_progress)
                print("Progress: ", progress_words(
                    guess_char, answer, answer_progress))
                print('Letter guessed:', ",".join(guessed_letters))
                if correct_answer == answer:
                    print(f"HOORAYYYY! {username}, YOU WON!!!")
                    print("---------------------------")
                    print("\n")
                    play_again(username)
                print('\n')

            elif guess_char not in answer:
                print('The guess was WRONG!!')
                lives_remaining += 1
                guessed_letters.append(guess_char)
                hangman_hanged(lives_remaining, answer, username)
                print("Progress: ", progress_words(
                    guess_char, answer, answer_progress))
                print('Letter guessed:', ",".join(guessed_letters))
                print('\n')


# Play
def play_again(username):
    play_again = input('''Do you want to play again?
                            (Y) - Yes
                            (N) - No
                        ''').lower()
    if play_again == 'y':
        game_menu(username)

    elif play_again == 'n':
        quit_program(username)
    else:
        quit_program(username)


# Quit Game
def quit_program(username):
    print('Quitting...')
    print(f'Thank You {username}. Have a Good Day')
    exit()


# Display Guess Letter
def guess_letters(guessed_letters):
    guessed_letters += "," + guessed_letters
    return guessed_letters


# Progress Words
def progress_words(guess_char, answer, progress):
    n = 0
    while n < len(answer):
        if guess_char == answer[n]:
            progress[n] = guess_char
            n += 1
        else:
            n += 1

    return "".join(progress)


# Hangman Hanged
def hangman_hanged(lives_remaining, answer, username):
    if lives_remaining == 0:
        print('''
                 |---+
                     |
                     |
                     |''')
        print("Lives left: 7")

    elif lives_remaining == 1:
        print('''
                 |---+
                 O   |
                     |
                     |''')
        print("Lives left: 6")

    elif lives_remaining == 2:
        print('''
                 |---+
                 O   |
                 |   |
                     |
        ''')
        print("Lives left: 5")

    elif lives_remaining == 3:
        print('''
                 |---+
                 O   |
                /|   |
                     |
        ''')
        print("Lives left: 4")

    elif lives_remaining == 4:
        print('''
                 |---+
                 O   |
                /|\  |
                     |
        ''')

        print("Lives left: 3")

    elif lives_remaining == 5:
        print('''
                 |---+
                 O   |
                /|\  |
                     |
            ''')
        print("Lives left: 2")

    elif lives_remaining == 6:
        print('''
                 |---+
                 O   |
                /|\  |
                /    |
        ''')
        print("Lives left: 1")

    else:
        print('''
                 |---+
                 O   |
                /|\  |
                / \  |
        ''')
        print(f'Sorry {username}, You are hanged!!')
        print('GAME OVER!!!')
        print("The secret word was ", answer)
        print("---------")
        play_again(username)


# Game Menu
def game_menu(username):
    print(f'__________ Hi {username} ____________')
    print('''-------- WELCOME TO HANGMAN --------

                 |---+
                 O   |
                /|\  |
                / \  |

            (I) for Instruction
            (P) to Play Game
            (Q) to Quit
        ----------------------------------------
    ''')
    answer = getRandomWord()
    while True:
        user_choice = input('Enter your choice: ').lower()

        if user_choice == 'i':
            print(open('instructions.txt').read())

        elif user_choice == 'p':
            play_game(answer, username)

        elif user_choice == 'q':
            quit_program(username)

        else:
            print('Make a correct choice!')


# Main
def main():
    username = input("Please enter your name: ").capitalize()
    game_menu(username)


# Main Program Executes
main()
