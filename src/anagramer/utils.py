#!/usr/bin/python3
import threading

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

''' Alphabetize with respect to second letter '''
def alphabetize(collection):
    # NOTE: Since en-us.dict is already alphabetized and the sort algorithm is top down
    # and anagram insertions are head-first (e.g lpush'ed into linked list) items should
    # already be in a completely alphabetized arrangement, however an insert that is
    # an update to the cache may not guarantee this arrangement.
    return collection

''' Simple decorator for running a function asynchronously '''
def run_in_background(func):
    def wrapper(*args, **kwargs):
        threading.Thread(target=func, args=args, kwargs=kwargs).start()
    return wrapper
