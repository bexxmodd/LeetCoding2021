# https://leetcode.com/problems/lucky-numbers-in-a-matrix/submissions/

from collections import defaultdict

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        maxs = defaultdict(int)
        mins = defaultdict(int)
        for row in matrix:
            mins[min(row)] = row.index(min(row))
            for i in range(len(row)):
                if row[i] > maxs[i]:
                    maxs[i] = row[i]
        for i in mins.keys():
            if i >= maxs[mins[i]]:
                res.append(i)
        return res