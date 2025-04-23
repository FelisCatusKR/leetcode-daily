from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(list)
        for num in range(1, n + 1):
            d[get_sum_of_digits(num)].append(num)
        result_arr = [0] * 10_001
        max_size = 0
        for v in d.values():
            group_size = len(v)
            result_arr[group_size] += 1
            max_size = max(max_size, group_size)
        return result_arr[max_size]


def get_sum_of_digits(num: int) -> int:
    s = str(num)
    return sum(int(digit) for digit in s)



if __name__ == "__main__":
    n = 14
    result = Solution().countLargestGroup(n)
    print(result)
