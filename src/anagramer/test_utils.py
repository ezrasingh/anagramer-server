from anagramer.utils import normalize, alphabetize

def test_normalize():
    assert normalize("hello") == "fk:ehllo"

def test_alphabetize():
    sorted_collection = alphabetize(["apple", "bear", "candy"])
    assert set(sorted_collection) ^ set(["candy", "bear", "apple"]) == set()