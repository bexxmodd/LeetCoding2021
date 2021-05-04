# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer, but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.

Example:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, 
            with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
            It doesn't matter what you leave beyond the returned length.
"""

def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) < 3:
        return len(nums)
    
    i = 0
    while i + 2 < len(nums):
        if nums[i + 2] == nums[i]:
            nums.pop(i + 2)
        else:
            i += 1
    return len(nums)