from collections import defaultdict


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        dp_dict = defaultdict[int, int](lambda: 0)
        result = 0
        left = 0
        for num in nums:
            k -= dp_dict[num]
            dp_dict[num] += 1
            while k <= 0:
                dp_dict[nums[left]] -= 1
                k += dp_dict[nums[left]]
                left += 1
            result += left
        return result


if __name__ == "__main__":
    nums = [3,1,4,3,2,2,4]
    k = 2
    result = Solution().countGood(nums, k)
    print(result)
