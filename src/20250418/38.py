class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        while n := n - 1:
            new = ""
            prev = result[0]
            prev_count = 1
            for i in range(1, len(result)):
                if result[i] == prev:
                    prev_count += 1
                    continue
                new += f"{prev_count}{prev}"
                prev = result[i]
                prev_count = 1
            new += f"{prev_count}{prev}"
            result = new
        return result


if __name__ == "__main__":
    for n in range(1, 5):
        result = Solution().countAndSay(n)
        print(result)
