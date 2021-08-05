# Given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.


from string import ascii_lowercase

letters = {letter: str(i) for i, letter in enumerate(ascii_lowercase, start=1)}


def alphabet_position(text):
    return ' '.join([letters[chars] for chars in text.lower() if chars in letters])
