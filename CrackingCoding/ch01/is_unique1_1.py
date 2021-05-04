"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

def is_unique(s: str) -> bool:
    s_set = set(s)
    return len(s) == len(s_set)

def is_unique2(s: str) -> bool:
    x = sorted(s)
    for i in range(1, len(x)):
        if x[i-1] == x[i]:
            return False
    return True


text1 = "axybcdefg"
text2 = "aghbopcdbe"
print(is_unique(text1))
print(is_unique(text2))

print(is_unique(text1))
print(is_unique(text2))