class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        distinct_nums = len(set(nums))
        nums_set = set()
        result = 0
        for i in range(len(nums)):
            result += traverse(nums, distinct_nums, nums_set, i)
        return result


def traverse(nums: list[int], distinct_nums: int, nums_set: set[int], cur_pos: int):
    result = 0
    cur_num = nums[cur_pos]
    is_added = False
    if cur_num not in nums_set:
        nums_set.add(cur_num)
        is_added = True
    if len(nums_set) == distinct_nums:
        result += 1
    if cur_pos != len(nums) - 1:
        result += traverse(nums, distinct_nums, nums_set, cur_pos + 1)
    if is_added:
        nums_set.remove(cur_num)
    return result



if __name__ == "__main__":
    nums = [1,3,1,2,2]
    result = Solution().countCompleteSubarrays(nums)
    print(result)
