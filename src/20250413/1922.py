class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007

        # 짝수/홀수 인덱스의 개수 계산
        even_positions = (n + 1) // 2
        odd_positions = n // 2

        # 짝수 자리수는 5가지 경우가 존재 (0, 2, 4, 6, 8)
        # 홀수 자리수는 4가지 경우가 존재 (2, 3, 5, 7)
        # 각각의 자리수의 개수만큼 제곱을 계산하여 반환
        return (self.fast_power(5, even_positions, MOD) * 
                self.fast_power(4, odd_positions, MOD)) % MOD

    def fast_power(self, base: int, power: int, mod: int) -> int:
        """(base ^ power) % mod 연산을 제곱을 이용해 빠르게 계산합니다."""
        result = 1
        while power > 0:
            # 지수가 홀수인 경우, 결과값에 밑을 미리 곱해줌
            if power % 2 == 1:
                result = (result * base) % mod

            # 밑을 제곱한 후 지수를 절반으로 낮춤
            base = (base * base) % mod
            power //= 2

        return result


if __name__ == "__main__":
    n = 5
    result = Solution().countGoodNumbers(n)
    print(result)
