"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
"""

def one_away(s1: str, s2: str) -> bool:
    i, j = 0, 0
    edit = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            edit += 1
            if len(s1) > len(s2):
                i += 1
            elif len(s1) < len(s2):
                j += 1
        
        i += 1
        j += 1
        if edit > 1:
            return False
    return True


print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bae'))