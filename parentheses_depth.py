from collections import deque

def max_depth(s: str) -> int:
    depth = 0
    stack = deque()

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) > 0:
            stack.pop()
        if len(stack) > depth:
            depth = len(stack)
    return depth


print(max_depth('(a(b)c)'))
print(max_depth('( )'))
print(max_depth('( (a) ( (t) ( )b( (yy) )g) )'))
