import heapq

def max_produc(nums: list) -> int:
    h = heapq()
    for i in nums:
        if i > h[0]:
            h.pop()
            h.push(i)
        if len(h) > 3:
            h.pop()
    total = h.pop()
    for _ in range(len(h)):
        total *= h.pop
    return total



nums = [1, 2, 5, 1, 3, 7, 4, 1, 6]
print(max_produc(nums))