"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z)
"""

def str_compression(s: str) -> str:
    counter = 0
    res = ""
    for i in range(len(s)-1):
        counter += 1
        if s[i] != s[i + 1]:
            res += s[i] + str(counter)
            counter = 0
    res += s[-1] + str(counter + 1)
    if len(res) > len(s):
        return s
    return res

test1 = 'aabcccccaaa'
print(str_compression(test1))

test1 = 'bbzzzzsasappo'
print(str_compression(test1))

test1 = 'zzzzzzzozzzzzz'
print(str_compression(test1))