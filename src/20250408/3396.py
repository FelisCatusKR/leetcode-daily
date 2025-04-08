"""3396. Minimum Number of Operations to Make Elements in Array Distinct

You are given an integer array `nums`. You need to ensure that the elements in the array are **distinct**. To achieve this, you can perform the following operation any number of times:

- Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.

**Note** that an empty array is considered to have distinct elements. Return the **minimum** number of operations needed to make the elements in the array distinct.

https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct
"""


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        answer = 0
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                break
            nums = nums[3:]
            answer += 1

        return answer


if __name__ == "__main__":
    arr = [6,7,8,9]
    result = Solution().minimumOperations(arr)
    print(result)
