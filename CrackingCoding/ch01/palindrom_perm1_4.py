"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)
"""

from collections import defaultdict


def palindrome_perm(s: str) -> bool:
    counter = defaultdict(int)
    length = 0
    odd_count = 0
    for i in s:
        if i.isalpha():
            length += 1
            counter[i.lower()] += 1

        if counter[i.lower()] % 2 != 0:
            odd_count += 1
        else:
            odd_count -= 1

    if length % 2 == 0:
        return odd_count == 0
    else:
        return odd_count <= 1


text1 = 'tactcoapapa'
assert palindrome_perm(text1)

text1 = 'Tact Coa'
assert palindrome_perm(text1)

text1 = 'TactbaCoa'
assert palindrome_perm(text1)
