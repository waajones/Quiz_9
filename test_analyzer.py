import pytest
from analyzer import convert, count_words, count_chars, count_unique_words, find_most_common_word, average_word_length


def test_count_words_basic_sentence():
    text = "Hello, world! This is a test."
    assert count_words(text) == 6


def test_count_words_empty_string():
    assert count_words("") == 0


def test_count_chars_excluding_spaces():
    text = "a b c!"
    assert count_chars(text) == 4


def test_count_chars_including_spaces():
    text = "a b c!"
    assert count_chars(text, include_spaces=True) == 6


def test_find_most_common_word_simple():
    text = "apple banana apple orange banana apple"
    assert find_most_common_word(text) == "apple"


def test_find_most_common_word_empty():
    assert find_most_common_word("") is None


def test_count_unique_words_with_punctuation():
    text = "Hello, hello!! HELLO??? world."
    assert count_unique_words(text) == 2


def test_average_word_length_simple():
    text = "Hi there"
    assert average_word_length(text) == pytest.approx(3.5)


def test_average_word_length_empty():
    assert average_word_length("") == 0.0