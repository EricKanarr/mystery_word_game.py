import random
import sys
import os


def clear():
    os.system('clear')


def get_dictionary():
    with open('/usr/share/dict/words', 'r') as f:
        words = []
        for word in f.readlines():
            words.append(word)
        return words


def easy_words(word_list):
    easy_word_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_word_list.append(word)
    return easy_word_list


def medium_words(word_list):
    medium_word_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 8:
            medium_word_list.append(word)
    return medium_word_list


def hard_words(word_list):
    hard_word_list = []
    for word in word_list:
        if len(word) >= 8:
            hard_word_list.append(word)
    return hard_word_list


def randomize(word_list):
    correct_word = random.choice(word_list)
    return correct_word


def display_word(word, guesses):
    progress_display = []
    for letter in word:
        if letter in guesses:
            progress_display.append(letter)
        else:
            progress_display.append('_')
    progress_display = ' '.join(progress_display)
    progress_display = progress_display.upper()
    return progress_display


def is_word_complete(word, guesses):
    progress = display_word(word, guesses)
    if '_' in progress:
        return False
    else:
        return True


def get_level():
    level = input("Choose a difficulty, easy, medium or hard.\n")
    level = level.lower()
    if level == 'easy':
        answer = randomize(easy_words)
    elif level == 'medium':
        answer = randomize(medium_words)
    else:
        answer = randomize(hard_words)
    return answer


def gameplay(answer):
    guesses = []
    fails = 0
    print("Mystery word has {} letters.".format(len(answer)))
    while is_word_complete(answer, guesses) == False:
        this_guess = (input("Okay, take a guess!\n")).lower()
        if len(this_guess) > 1:
            print("One letter only.")
        elif this_guess not in guesses:
            if this_guess not in answer:
                print("Nope, try again.")
                fails += 1
            else:
                print("Nice!")
        else:
            print("You already guessed that!")
        guesses.append(this_guess)
        print(display_word(answer, guesses))
        print("These are your guesses so far: {}".format(guesses))
        print("You have {} guesses left.\n".format(8 - fails))
        if fails >= 8:
            break
    if fails >= 8:
        play_again_lose = input(("Word was {}, RE to replay.".format(answer)))
        play_again_lose.lower()
        if play_again_lose == 'yes':
            return main()
        else:
            print("Okay, have a nice day!")
    else:
        play_again_win = input("You won! Play again?  Press enter/return")
        play_again_win.lower()
        if play_again_win == '':
            clear()
            main()
        else:
            print("Bye Bye!")
            clear()
            sys.exit()


def welcome():
    print('  The Mystery Game   ')
    start = input("Press enter/return to start or Q to quit: ").lower()
    if start == 'q':
        print("Bye Bye!")
        sys.exit()
    else:
        return True


def main():
    welcome()
    answer = get_level()
    return gameplay(answer)


if __name__ == '__main__':
    clear()
    main()
