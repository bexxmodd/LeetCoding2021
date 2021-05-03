"""
Given a smaller strings and a bigger string b, design an algorithm to find all permuta­
tions of the shorter string within the longer one. Print the location of each permutation
"""

def all_permutations(b: str, s: str) -> None:
    if len(b) < 4:
        return
    s = sorted(s)
    for i in range(3, len(b)):
        tmp = sorted(b[i-4:i])
        if tmp == s:
            print(i-4, i)

if __name__ == '__main__':
    b = 'cbabadcbbabbcbabaabccbabc'
    s = 'abbc'
    all_permutations(b, s)