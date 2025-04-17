from itertools import combinations


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        result = 0
        combs = combinations(enumerate(nums), r=2)
        for first, second in combs:
            i, num_i = first
            j, num_j = second
            if num_i == num_j and (i * j) % k == 0:
                result += 1
        return result


if __name__ == "__main__":
    arr = [3,1,2,2,2,1,3]
    k = 2
    result = Solution().countPairs(arr, k)
    print(result)
