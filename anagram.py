"""Given a word and a list of possible anagrams, select the correct sublist."""

from typing import List, Counter
from collections import Counter


def find_anagrams(word: str, candidates: List[str]):
    """Return sublist of anagrams in candidates

    Args:
        word (str): word containing letters to find anagrams
        candidates (List[str]): list of possible candidates
    """
    letter_count = Counter(word)
    anagrams = []
    for candidate in candidates:
        candidate_count = Counter(candidate)
        if letter_validator(letter_count, candidate_count):
            anagrams.append(candidate)

    return anagrams


def letter_validator(word: Counter, candidate: Counter):
    """Return True if Candidate contains required letters from word

    Args:
        word (Counter): given word
        candidate (Counter): word being check to see if it is an anagram
    """
    for letter in candidate:
        if candidate.get(letter) <= word.get(letter, 0):
            return False
        else:
            candidate[letter] -= 1
    return True


candidates = ["hello", "world", "zombies", "pants"]
print(find_anagrams("diaper", candidates))
