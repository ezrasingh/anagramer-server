#!/usr/bin/python3
import graphene
from anagramer.interface import sort, search
from anagramer.utils import alphabetize

# Initialize dictionary and anagram mappings
sort('dictionary.txt')

''' Basic GraphQL query API for requesting anagrams '''
class AnagramQuery(graphene.ObjectType):
    anagrams = graphene.List(
        # Input argument must be a string
        word=graphene.NonNull(graphene.String),
        # Retrun List of Strings
        of_type=graphene.String
    )

    def resolve_anagrams(self, context, word):
        return alphabetize(search(word))

schema = graphene.Schema(query=AnagramQuery)
