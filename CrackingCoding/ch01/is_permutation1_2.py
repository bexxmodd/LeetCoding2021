"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

from collections import Counter

def is_permutation(s1: str, s2: str) -> bool:
    a = sorted(s1)
    b = sorted(s2)
    for i, j in zip(a, b):
        if i != j:
            return False
    return True


a1 = "abcdef"
a2 = "defabc"
print(is_permutation(a1, a2))
print(is_permutation(a1, "abdefg"))