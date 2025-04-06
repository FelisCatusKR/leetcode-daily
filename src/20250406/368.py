"""368. Largest Divisible Subset

Given a set of distinct positive integers `nums`, return the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

- `answer[i] % answer[j] == 0`, or
- `answer[j] % answer[i] == 0`

If there are multiple solutions, return any of them."""


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        dp = [1 for _ in range(len(nums))]
        prev = [-1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        answer = []
        for i in range(len(nums) - 1, -1, -1):
            tmp = [nums[i]]
            j = prev[i]
            while j != -1:
                tmp = [nums[j]] + tmp
                j = prev[j]
            if len(tmp) > len(answer):
                answer = tmp
        return answer


if __name__ == "__main__":
    arr = [4,8,10,240]
    result = Solution().largestDivisibleSubset(arr)
    print(result)
