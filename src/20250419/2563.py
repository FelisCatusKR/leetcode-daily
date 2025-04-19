class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        end = len(nums) - 1
        nums.sort()
        result = 0
        for i in range(len(nums)):
            left = _lower_bound(nums, i + 1, end, lower - nums[i])
            right = _lower_bound(nums, i + 1, end, upper - nums[i] + 1)
            result += right - left
        return result

def _lower_bound(nums: list[int], low: int, high: int, element: int):
    while low <= high:
        mid = low + ((high - low) // 2)
        if nums[mid] >= element:
            high = mid - 1
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    nums = [0,1,7,4,4,5]
    lower = 3
    upper = 6
    result = Solution().countFairPairs(nums, lower, upper)
    print(result)
