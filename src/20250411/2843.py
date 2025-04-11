class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        dp = self._prepare()
        return len(list(filter(lambda x: x >= low and x <= high, dp)))

    def _prepare(self) -> list[int]:
        dp = []
        # case 1: n = 1
        for target_sum in range(1, 10):
            dp.append(target_sum * 10 + target_sum)
        # case 2: n = 2
        for target_sum in range(1, 19):
            largest_last_num = min(9, target_sum)
            smallest_last_num = max(0, target_sum - 9)
            last = [x * 10 + (target_sum - x) for x in range(smallest_last_num, largest_last_num + 1)]
            largest_first_num = min(9, target_sum)
            smallest_first_num = max(1, target_sum - 9)
            first = [n * 10 + (target_sum - n) for n in range(smallest_first_num, largest_first_num + 1)]
            for item in first:
                dp.extend([item * 100 + x for x in last])
        return dp


if __name__ == "__main__":
    print(Solution()._prepare())
