# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        correct = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if correct or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                correct += 1
        return True