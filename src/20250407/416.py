"""416. Partition Equal Subset Sum

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

Constraints:
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

https://leetcode.com/problems/partition-equal-subset-sum
"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_of_nums = sum(nums)
        if sum_of_nums % 2 == 1:
            return False
        target = sum_of_nums // 2

        dp = [False for _ in range(target + 1)]
        for num in nums:
            if num > target:
                continue
            for i in range(target, -1, -1):
                if not dp[i] or i + num > target:
                    continue
                dp[i + num] = True
            dp[num] = True

        return dp[target]


if __name__ == "__main__":
    arr = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
    result = Solution().canPartition(arr)
    print(result)
