import random
import sys
import os


def clear():
    os.system('clear')


def dictionary():
    with open('/usr/share/dict/words', 'r') as dictionary:
        words = []
        for word in dictionary.readlines():
            words.append(word)
        return words


def difficulty_level():
    level = input("Easy, Medium, or HARD: ")
    if level == "EASY":
        return "easy"
    elif level == "MEDIUM":
        return "medium"
    else:
        return "hard"


def sort_difficulty(words, choice):
    if choice == 'easy':
        return pull_words_min_max(words, 4, 6)
    elif choice == 'medium':
        return pull_words_min_max(words, 6, 8)
    else:
        return pull_words_min_max(words, 8, 99)


def pull_words_min_max(words, min_length, max_length):
    difficulty = []
    for word in words:
        if len(word) >= min_length and len(word) <= max_length:
            difficulty.append(word)
    return difficulty


def pull_rand_word(difficulty):
    return difficulty[random.randrange(0, len(difficulty))]


def pull_guess(bad_guesses, good_guesses, secret_word):
    while True:
        guess = input("Guess a letter: ").lower()
        board(bad_guesses, good_guesses, secret_word)
        if guess == '':
            print("Whoops, operator error")
        elif len(guess) != 1:
            print("One letter at a time!")
        elif guess in bad_guesses or guess in good_guesses:
            print("Duplicate letter!")
        elif not guess.isalpha():
            print("Only letters in this word!")
        else:
            return guess


def board(bad_guesses, good_guesses, secret_word):
    clear()
    print('** Strikes: {}/8 **'.format(len(bad_guesses)))
    print('')
    for guess in bad_guesses:
        print(guess)
    print('\n\n')
    for guess in secret_word:
        if guess in good_guesses:
            print(guess)
        else:
            print(' _ ')
    print('')


def welcome():
    print('\n** Welcome to (no)Hangman!!! **\n')
    start = input("Press enter/return to start or Q to quit: ").lower()
    if start == 'q':
        print("See you next time!")
        sys.exit()
    else:
        return True


def play_again():
    play_again = input("\nPlay again? Y/n ").lower()
    if play_again != 'n':
        clear()
        welcome()
        main()
    else:
        print("\n\n\n\nCatch ya later!\n\n\n\n")
        time.sleep(1.5)
        clear()
        sys.exit()


def main():
    choice = pull_difficulty_level()
    words = pull_all_words()
    difficulty = pull_words_for_difficulty(words, choice)
    secret_word = pull_rand_word(difficulty)
    bad_guesses = []
    good_guesses = []
    board(bad_guesses, good_guesses, secret_word)
    done = False
    while not done:
        guess = pull_guess(bad_guesses, good_guesses, secret_word)
        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for guess in secret_word:
                if guess not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}.".format(secret_word))
                done = True
        elif guess not in secret_word:
            bad_guesses.append(guess)
            if len(bad_guesses) == 8:
                clear()
                print("\nENGHH!")
                print("\nStrike ! You lost!")
                print("\nThe secret word was {}".format(secret_word.upper()))
                done = True
        if done:
            play_again()
        else:
            board(bad_guesses, good_guesses, secret_word)


if __name__ == '__main__':
    clear()
    welcome()
    main()
