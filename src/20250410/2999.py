class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        upper_limit = str(finish)
        lower_limit = str(start - 1)
        upper_length = len(upper_limit)
        lower_length = len(lower_limit)
        upper_count = 0
        lower_count = 0
        if len(s) <= upper_length:
            dp = [[-1 for _ in range(2)] for _ in range(upper_length)]
            upper_count = self._traverse(0, 1, upper_limit, s, limit, upper_length, dp)
        if len(s) <= lower_length:
            dp = [[-1 for _ in range(2)] for _ in range(lower_length)]
            lower_count = self._traverse(0, 1, lower_limit, s, limit, lower_length, dp)
        return upper_count - lower_count

    def _traverse(self, idx: int, tight: int, num_str: str, suffix: str, limit: int, num_length: int, dp: list[list[int]]) -> int:
        if idx == num_length:
            return 1
        if dp[idx][tight] != -1:
            return dp[idx][tight]
    
        lower_bound = 0
        count = 0

        if tight:
            upper_bound = min(limit, int(num_str[idx]))
        else:
            upper_bound = limit
        suffix_start_idx = num_length - len(suffix)
        if suffix_start_idx <= idx:
            lower_bound = int(suffix[idx - suffix_start_idx])
            upper_bound = min(upper_bound, int(suffix[idx - suffix_start_idx]))
        for i in range(lower_bound, upper_bound + 1):
            count += self._traverse(idx + 1, tight and (i == int(num_str[idx])), num_str, suffix, limit, num_length, dp)
        dp[idx][tight] = count
        return count
