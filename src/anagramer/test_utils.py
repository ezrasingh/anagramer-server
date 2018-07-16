from itertools import permutations
from anagramer.utils import normalize, alphabetize

def test_normalize():
    # prime hash = 23(h) * 2(e) * 31(l) * 31(l) * 7(o)
    prime_hash = bytes(309442)
    for anagram in permutations("hello"):
        assert normalize("hello") == normalize(anagram) == prime_hash

def test_alphabetize():
    sorted_collection = alphabetize(["apple", "bear", "candy"])
    assert set(sorted_collection) ^ set(["candy", "bear", "apple"]) == set()