MOD = 1_000_000_007

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        m = min(n, 14)
        dp = [[0] * (m + 1) for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][1] = 1
            j = 2
            while i * j <= maxValue:
                for k in range(1, m):
                    dp[i * j][k + 1] += dp[i][k]
                j += 1
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i % MOD
        inverse_factorial = [1] * n
        inverse_factorial[n - 1] = pow(factorial[n - 1], MOD - 2, MOD)
        for i in range(n-1, 0, -1):
            inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD
        res = 0
        f_n1 = factorial[n - 1]
        for i in range(1, maxValue + 1):
            for k in range(1, m + 1):
                res = (res + dp[i][k] * f_n1 % MOD * inverse_factorial[k - 1] % MOD * inverse_factorial[n - k] % MOD) % MOD
        return res
