import random
import sys
import os


def clear():
    os.system('clear')


# pull dictionary
def get_dictionary():
    with open("/usr/share/dict/words", 'r') as f:
        words = []
        for word in f.readlines():
            words.append(word)
        return words


# assign easy medium hard
def assign_difficulty():
    assign_difficulty = input("Choose difficulty: easy, medium, or hard: ")
    if assign_difficulty == 'easy':
        return 'easy'
    elif assign_difficulty == 'medium':
        return 'medium'
    else:
        return 'hard'


# define length of easy medium hard
def word_length(words, choice):
    if choice == 'easy':
        return length_list(words, 4, 6)
    elif choice == 'medium':
        return length_list(words, 6, 8)
    else:
        return length_list(words, 8, 99)


# put words into lists
def length_list(words, min_length, max_length):
    assign_difficulty = []
    for word in words:
        if len(word) >= min_length and len(word) <= max_length:
            assign_difficulty.append(word)
    return assign_difficulty


# randomize words
def randomize_words(difficulty):
    return difficulty[random.randrange(0, len(difficulty))]


# would you like to play question
def start_game():
    print("   Welcome to The Mystery Word Game   ")
    start = input("Press enter/return to play or Q to quit: ")
    if start.lower() == 'q':
        print("Goodbye!")
        sys.exit()
    else:
        return True


# show length of word
# for correct guess show letter in word, for incorrect guess assign a strike(8)
def game_board(bad_guesses, good_guesses, secret_word):
    clear()
    print('Strikes: {}/8'.format(len(bad_guesses)))
    print('')
    for guess in bad_guesses:
        print(guess, end='')
    print('\n\n')
    for guess in secret_word:
        if guess in good_guesses:
            print(guess, end='')
        else:
            print(' _ ', end='')
    print('')


# ask for a guess, no duplicates/numbers/multiple letters/blank space
def get_guess(bad_guesses, good_guesses, secret_word):
    while True:
        guess = input("Guess a letter: ").lower()
        game_board(bad_guesses, good_guesses, secret_word)
        if guess == '':
            print("Try a different letter")
        elif len(guess) != 1:
            print("Only one letter at a time!")
        elif guess in bad_guesses or guess in good_guesses:
            print("Already tried that one, try again")
        elif not guess.isalpha():
            print("Only letters in this word")
        else:
            return guess


# ask to play again
def play_again():
    play_again = input("Do you want to play again?  Y/n").lower()
    if play_again != 'n':
        clear()
        main()
    else:
        print("Maybe next time")
        clear()
        sys.exit()


def main():
    good_guesses = []
    bad_guesses = []
    choice = assign_difficulty()
    words = get_dictionary()
    difficulty = word_length(words, choice)
    secret_word = randomize_words(difficulty)
    game_board(bad_guesses, good_guesses, secret_word)
    done = False
    while not done:
        guess = get_guess(bad_guesses, good_guesses, secret_word)
        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for guess in secret_word:
                if guess not in good_guesses:
                    found = False
            if found:
                print("You Win!")
                print("The secret word was {}".format(secret_word))
                done = True
        elif guess not in secret_word:
            bad_guesses.append(guess)
            if len(bad_guesses) == 8:
                clear()
                print("You lost!")
                print("The secret_word was {}".format(secret_word))
                done = True
            if done:
                play_again()
        else:
            game_board(bad_guesses, good_guesses, secret_word)


if __name__ == '__main__':
    clear()
    start_game()
    main()
