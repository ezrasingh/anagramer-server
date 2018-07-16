from anagramer.utils import normalize, alphabetize

def test_normalize():
    assert normalize("hello") == "fk:ehllo"
