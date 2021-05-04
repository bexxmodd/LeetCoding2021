# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3730/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        res = []
        for n in nums:
            total += n
            res.append(total)
        return res
