"""1863. Sum of All Subset XOR Totals

The **XOR total** of an array is defined as the bitwise `XOR` of **all its elements**, or `0` if the array is **empty**.

- For example, the **XOR total** of the array `[2,5,6]` is `2 XOR 5 XOR 6 = 1`.

Given an array `nums`, return *the **sum** of all **XOR totals** for every **subset** of `nums`*. 

**Note**: Subsets with the **same** elements should be counted **multiple** times.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

https://leetcode.com/problems/sum-of-all-subset-xor-totals
"""

from functools import reduce
from itertools import combinations


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0] 
        answer = sum(nums)
        for com_len in range(2, len(nums) + 1):
            for com_nums in combinations(nums, com_len):
                answer += reduce(lambda x, y: x ^ y, com_nums)
        return answer


if __name__ == "__main__":
    arr = [3,4,5,6,7,8]
    result = Solution().subsetXORSum(arr)
    print(result)
