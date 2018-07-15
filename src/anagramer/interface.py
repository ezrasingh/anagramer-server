#!/usr/bin/python3
''' Interface for searching and sorting dictionary for anagrams '''
import time
from anagramer import cache
from anagramer.utils import parse, normalize, alphabetize, run_in_background
try:
    import CPickle as pickle
except ImportError:
    import pickle

''' Filename of local English dictionary '''
EN_US = 'en-us.dict'

''' Key of runtime-cache history '''
CACHE_HISTORY = 'cache:history'

''' Create a one-to-many relationship; each word maps to a list of anagrams '''
@run_in_background
def sort(dictionary):
    start_time = time.time()
    cache_history = cache.get(CACHE_HISTORY)
    # Setup lookup table for words that should be marked as already cached
    if cache_history:
        should_cache = pickle.loads(bytes(cache_history))
    else:
        # NOTE: should_cache will be used to circumvent reading an entire Redis list within the algorithm.
        # Since Redis list are implemented as Linked List they have O(n) read complexity
        # With a seprate lookup table implemented as Python dict with O(1) read complexity,
        # we can map which words were registered as anagrams for a particular normalized value(i.e foreign key) 
        # This allows us to avoid redundant operations on words already sorted
        should_cache = {}
    # Prepare Redis for bulk operation
    pipe = cache.pipeline()
    print("Sorting dictionary...")
    for word in parse(dictionary):
        foreign_key = normalize(word)
        # Check to see if word was not already cached
        if not cache.get(word):
            # Setup normalized word as a foreign key between word and anagrams
            pipe.set(word, foreign_key)
            # Update lookup table
            should_cache.update({ foreign_key : dict() })
    print("Sorting complete!")
    print("Generating anagram maps...")
    # Loop through English dictionary; treat each word as a potential anagram
    for anagram in parse(EN_US):
        foreign_key = normalize(anagram)
        # Determine if we should cache this anagram
        if foreign_key in should_cache:
            # Check if anagram was marked as already cached
            if anagram not in should_cache[foreign_key]:
                # Append the anagram to the container for this particular foreign key
                pipe.lpush(foreign_key, anagram)
                # Update lookup table to mark this anagram as previously cached
                should_cache[foreign_key].update({ anagram : True })
    print("Anagram mapping complete!")
    print("Persisting to cache...")
    # Save cache history, so that next time we know which anagrams where already cached
    pipe.set(CACHE_HISTORY, pickle.dumps(should_cache))
    # Push Redis operations in bulk
    pipe.execute()
    # Runtime in seconds
    runtime = time.time() - start_time
    print("Sorted in: {:,}s".format(int(round(runtime))))

''' Search for word anagrams; return organized list or None '''
def search(word):
    foregin_key = cache.get(word)
    if foregin_key:
        collector = []
        for index in range(cache.llen(foregin_key)):
            # Append to collector in UTF-8 format
            collector.append(cache.lindex(foregin_key, index).decode('utf-8'))
        return alphabetize(collector)
    else:
        # Requested word non existent in the available dictionary
        return None
