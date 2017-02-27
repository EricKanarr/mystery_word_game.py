import random
import sys
import os


def clear():
    os.system('clear')


def dictionary():
    with open('/usr/share/dict/words', 'r') as f:
        words = []
        for word in f.readlines():
            words.append(word)
        return words


def categories():
    level = input("Choose easy, medium or hard: ")
    if level == "easy":
        return "easy"
    elif level == "medium":
        return "medium"
    else:
        return "hard"


def word_length(words, choice):
    if choice == 'easy':
        return min_max_length(words, 4, 6)
    elif choice == 'medium':
        return min_max_length(words, 6, 8)
    else:
        return min_max_length(words, 8, 99)


def min_max_length(words, min_length, max_length):
    difficulty = []
    for word in words:
        if len(word) >= min_length and len(word) <= max_length:
            difficulty.append(word)
    return difficulty


def randomize(difficulty):
    return difficulty[random.randrange(0, len(difficulty))]


def pull_guess(bad_guesses, good_guesses, mystery_word):
    while True:
        guess = input("Guess a letter: ").lower()
        board(bad_guesses, good_guesses, mystery_word)
        if guess == '':
            print("Enter a letter")
        elif len(guess) != 1:
            print("Only one letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("Duplicate, try again!")
        elif not guess.isalpha():
            print("Letters Only!")
        else:
            return guess


def welcome():
    print('   The Mystery Word Game   ')
    start = input("Press enter/return to start or Q to quit: ").lower()
    if start == 'q':
        print("Bye Bye!")
        sys.exit()
    else:
        return True


def board(bad_guesses, good_guesses, mystery_word):
    clear()
    print('Strikes: {}/8'.format(len(bad_guesses)))
    print('')
    for guess in bad_guesses:
        print(guess, end='')
    print('\n\n')
    for guess in mystery_word:
        if guess in good_guesses:
            print(guess, end='')
        else:
            print(' _ ', end='')
    print('')


def play_again():
    play_again = input("Play again? Y/n ").lower()
    if play_again != 'n':
        clear()
        welcome()
        main()
    else:
        print("Bye Bye")
        clear()
        sys.exit()


def main():
    choice = categories()
    words = dictionary()
    difficulty = word_length(words, choice)
    mystery_word = randomize(difficulty)
    bad_guesses = []
    good_guesses = []
    board(bad_guesses, good_guesses, mystery_word)
    done = False
    while not done:
        guess = pull_guess(bad_guesses, good_guesses, mystery_word)
        if guess in mystery_word:
            good_guesses.append(guess)
            found = True
            for guess in mystery_word:
                if guess not in good_guesses:
                    found = False
            if found:
                print("Winner Winner!")
                print("The secret word was {}.".format(mystery_word))
                done = True
        elif guess not in mystery_word:
            bad_guesses.append(guess)
            if len(bad_guesses) == 8:
                clear()
                print("Nope!")
                print("Game Over!")
                print("\nThe mystery word was {}".format(mystery_word.upper()))
                done = True
        if done:
            play_again()
        else:
            board(bad_guesses, good_guesses, mystery_word)


if __name__ == '__main__':
    clear()
    welcome()
    main()
