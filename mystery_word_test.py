# not sure how to start this file
from mystery_word_game.py import word_length
from mystery_word_game.py import randomize
from mystery_word_game.py import board
from mystery_word_game.py import main


def test_range_easy():
    assert word_length(['ballerina', 'dude', 'erasers'], 4, 6) == ['dude']


def test_range_medium():
    assert word_length(['ballerina', 'dude', 'erasers'], 6, 8) == ['erasers']


def test_range_hard():
    assert word_length(['ballerina', 'dude', 'eraser'], 8, 99) == ['ballerina']


def test_display_word():
    word = "toxicity"
    assert board(word, []) == "_ _ _ _ _ _ _ _"
    assert board(word, ['q']) == "_ _ _ _ _ _ _ _"
    assert board(word, ['x']) == "_ _ _ _ _ _ _ _"
    assert board(word, ['c']) == "_ _ _ _ _ _ _ _"
    assert board(word, ['q', 'c']) == "_ _ _ _ _ _ _ _"
    assert board(word, ['q', 'c', 'y']) == "_ _ _ _ _ _ _ _"


def test_complete_word():
    word = "dude"
    assert not main(word, [])
    assert not main(word, ['d'])
    assert not main(word, ['d', 'u'])
    assert main(word, ['d', 'u', 'e'])


def test_randomize_words():
    assert randomize(['dude', 'erasers', 'scope', 'range'])
