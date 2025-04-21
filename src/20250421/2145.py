class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        maximum = 0
        minimum = 0
        current = 0
        for diff in differences:
            current += diff
            minimum = min(minimum, current)
            maximum = max(maximum, current)
            if maximum - minimum > upper - lower:
                return 0
        return (upper - lower) - (maximum - minimum) + 1


if __name__ == "__main__":
    differences = [1,-3,4]
    lower = 1
    upper = 6
    result = Solution().numberOfArrays(differences, lower, upper)
    print(result)
