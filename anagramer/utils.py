#!/usr/bin/python3
''' Stream each line of a file '''
def parse(dictionary_file):
    with open(dictionary_file, 'r') as dictionary:
        for word in dictionary:
            yield word.rstrip()

''' Return sorted word as string '''
def normalize(word):
    # NOTE: This normalization function can take a number of forms
    # sorting the word is the simplest to implement however, prime
    # de-factorization is also a valid normalizer.
    # Prefix normalize to prevent collisions with actual word mappings
    return  "fk:" + "".join(sorted(word)) # O(n log n)

