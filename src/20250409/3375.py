"""3375. Minimum Operations to Make Array Values Equal to K

You are given an integer array `nums` and an integer `k`.

An integer `h` is called **valid** if all values in the array that are **strictly greater** than `h` are *identical*.

For example, if `nums = [10, 8, 10, 8]`, a **valid** integer is `h = 9` because all `nums[i] > 9` are equal to 10, but 5 is not a **valid** integer.

You are allowed to perform the following operation on `nums`:

- Select an integer `h` that is *valid* for the **current** values in `nums`.
- For each index `i` where `nums[i] > h`, set `nums[i]` to `h`.

Return the **minimum** number of operations required to make every element in `nums` **equal** to `k`. If it is impossible to make all elements equal to `k`, return -1.

https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k
"""

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        smallest = nums[0]
        if smallest < k:
            return -1

        nums = set(nums)
        if smallest == k:
            return len(nums) - 1
        else:
            return len(nums)


if __name__ == "__main__":
    arr = [2,1,2]
    k = 2
    result = Solution().minOperations(arr, k)
    print(result)
