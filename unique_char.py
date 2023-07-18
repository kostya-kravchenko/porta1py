__all__ = ['find_unique_ch', 'find_unique_character']

import re

text = """
The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"
"""

text = "C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup R# R++"


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
