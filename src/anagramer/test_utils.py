from itertools import permutations
from anagramer.utils import normalize, alphabetize

def test_normalize():
    for anagram in permutations("hello"):
        assert normalize("hello") == normalize(anagram)

def test_alphabetize():
    sorted_collection = alphabetize(["apple", "bear", "candy"])
    assert set(sorted_collection) ^ set(["candy", "bear", "apple"]) == set()
    assert alphabetize(None) == None