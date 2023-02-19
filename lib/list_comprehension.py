#!/usr/bin/env python3

#  create lists using list comprehensions


# returns a list of all of the even elements of a sequence of integers
def return_evens(num_list):
    return [num for num in num_list if not num % 2 ]

# returns a list of sentence strings with exclamation marks at the end
def make_exclamation(sentence_list):
    return [f"{string}!" for string in sentence_list]