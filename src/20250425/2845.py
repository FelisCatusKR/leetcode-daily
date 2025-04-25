from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        d: defaultdict[int, int] = defaultdict(lambda: 0)
        d[0] = 1
        result = 0
        equals = 0
        for num in nums:
            if num % modulo == k:
                equals += 1
            remain = equals % modulo
            needed = (remain - k + modulo) % modulo
            result += d[needed]
            d[remain] += 1
        return result


if __name__ == "__main__":
    nums = [3,2,4]
    modulo = 2
    k = 1
    result = Solution().countInterestingSubarrays(nums, modulo, k)
    print(result)
