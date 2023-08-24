from uzwords import words
from difflib import get_close_matches
#import magic_filter
def checkWord(word,words=words):
    word = word.lower()
    matches = set(get_close_matches(word,words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'н' in word:
        word = word.replace('н','х')
        matches.update(get_close_matches(word,words))
    elif 'х' in word:
        word = word.replace('х','н')
        matches.update(get_close_matches(word,words))

    return {'available':available, 'matches':matches}
