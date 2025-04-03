"""Maximum Value of an Ordered Triplet II

You are given a 0-indexed integer array `nums`.

Return the maximum value over all triplets of indices
`(i, j, k)` such that `i < j < k`. If all such triplets
have a negative value, return `0`.

The value of a triplet of indices `(i, j, k)` is equal
to `(nums[i] - nums[j]) * nums[k]`.

Constraints:
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`
"""

class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        prefix_max = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix_max[i] = max(prefix_max[i - 1], nums[i - 1])
        suffix_max = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i + 1])
        answer = 0
        for i in range(1, len(nums) - 1):
            answer = max(answer, (prefix_max[i] - nums[i]) * suffix_max[i])
        return answer
