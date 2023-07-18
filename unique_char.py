import re


def find_unique_character(s):
    characters = []
    for word in s.split():
        unique_char = None
        for char in word:
            if word.count(char) == 1:
                unique_char = char
                break
        if unique_char is not None:
            characters.append(unique_char)
    for char in characters:
        if characters.count(char) == 1:
            return char
    return ""


def first_unique_character(word: str) -> str:
    for ch in word:
        if word.count(ch) == 1:
            return ch
    return ""


def find_unique_ch(s: str) -> str:
    return first_unique_character(''.join(first_unique_character(i) for i in re.findall(r"[\w'+#]+", s)))
