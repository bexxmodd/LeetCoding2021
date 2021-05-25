def abacaba(n: int) -> str:
    alphabet = 'bcdefghijklmnopqrstuvwxyz'
    res = 'a'
    for i in range(n):
        res += alphabet[i] + res
    return res
    

print("a" == abacaba(0))
print("aba" == abacaba(1))
print("abacaba" == abacaba(2))
print("abacabadabacaba" == abacaba(3))
print("abacabadabacabaeabacabadabacaba" == abacaba(4))

print(abacaba(25))