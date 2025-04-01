"""2140. Solving Questions With Brainpower

You are given a 0-indexed 2D integer array `questions`
where `questions[i] = [points_i, brainpower_i]`.

The array describes the questions of an exam, where
you have to process the questions in order (i.e.,
starting from question `0`) and make a decision whether
to solve or skip each question. Solving question `i`
will earn you `points_i` points but you will be unable to
solve each of the next `brainpoweri questions. If you
skip question `i`, you get to make the decision on the
next question.

- For example, given `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]`:
  - If question `0` is solved, you will earn `3` points but you will be unable to solve questions `1` and `2`.
  - If instead, question `0` is skipped and question `1` is solved, you will earn `4` points but you will be unable to solve questions `2` and `3`.

Return the maximum points you can earn for the exam.
"""

class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        answer = 0
        dp = [0 for _ in range(len(questions))]

        for i, question in enumerate(questions):
            points = question[0]
            brainpower = question[1]
            # 문제를 풀지 않을 경우
            answer = max(answer, dp[i])
            if i + 1 < len(questions):
                dp[i + 1] = max(dp[i + 1], dp[i])
            # 문제를 풀 경우
            points_after_solving = dp[i] + points
            answer = max(answer, points_after_solving)
            target = i + brainpower + 1
            if target < len(questions):
                dp[target] = max(dp[target], points_after_solving)

        return answer
