"""
Given two sorted arrays, find the number of elements in common. The arrays are the same length
and each has all distinct elements.

Let's start with a good example. We'll underline the elements in common.
    A: 13 27 35 40 49 55 59
    B: 17 35 39 40 55 58 60
    ------------------------
    result: 35 40 55
"""

def common_elements(A: list, B: list) -> list:
    a_set = set(A)
    return [i for i in B if i in a_set]


print(common_elements([13, 27, 35, 40, 49, 55, 59],
                [17, 35, 39, 40, 55, 58, 60]))