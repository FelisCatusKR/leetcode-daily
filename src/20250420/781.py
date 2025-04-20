class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        answers.sort(reverse=True)
        result = answers[0] + 1
        prev = answers[0]
        prev_sum = answers[0]
        for i in range(1, len(answers)):
            if answers[i] == prev and prev_sum == 0:
                result += answers[i] + 1
                prev_sum = answers[i]
            elif answers[i] == prev:
                prev_sum -= 1
            else:
                prev = answers[i]
                result += answers[i] + 1
                prev_sum = answers[i]
        return result


if __name__ == "__main__":
    answers = [0,0,1,1,1]
    result = Solution().numRabbits(answers)
    print(result)
