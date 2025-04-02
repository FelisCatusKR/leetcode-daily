"""2873. Maximum Value of an Ordered Triplet I

You are given a 0-indexed integer array `nums`.

Return the maximum value over all triplets of indices
`(i, j, k)` such that `i < j < k`. If all such triplets
have a negative value, return `0`.

The value of a triplet of indices `(i, j, k)` is equal
to `(nums[i] - nums[j]) * nums[k]`.

Constraints:
- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 10^6`
"""

class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        answer = 0
        for k in range(2, len(nums)):
            for j in range(1, k):
                for i in range(0, j):
                    answer = max(answer, (nums[i] - nums[j]) * nums[k])
        return answer
