"""
Say that you are traveler on a 2D grid. You begin in the top-left corner and your goal is
to travel to the bottom-right corner. Yopu man only movve down or right.

In how many ways can you travel to the goal on a grid with dimensions n x m?

where 0 <= m, n <= 1000
"""

def grid_traveler(n: int, m: int, memo: dict={}) -> int:
    key = str(n) + ',' + str(m)

    # are the arguments in the memo
    if key in memo:
        return memo[key]

    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0

    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[key]

    

print(grid_traveler(2, 3)) # 3
print(grid_traveler(3 ,3)) # 6
print(grid_traveler(18, 18)) # 2333606220