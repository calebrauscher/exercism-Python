"""Given a word and a list of possible anagrams, select the correct sublist."""

from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """Return sublist of anagrams in candidates

    Args:
        word (str): word containing letters to find anagrams
        candidates (List[str]): list of possible candidates
    """

    return [
        candidate
        for candidate in candidates
        if word.lower() != candidate.lower()
        and sorted(word.lower()) == sorted(candidate.lower())
    ]
