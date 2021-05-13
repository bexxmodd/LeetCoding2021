def thousand_seperator(n: list) -> str:
    if n < 1000:
        return str(n)

    res = list(str(n))
    i = 3
    while i < len(res):
        if i < len(res):
            res.insert(len(res) - i, '.')
            i += 4
    return ''.join(res)


num1 = 987
num2 = 1234
num3 = 12345
num4 = 123456789

print(thousand_seperator(num1))
print(thousand_seperator(num2))
print(thousand_seperator(num3))
print(thousand_seperator(num4))