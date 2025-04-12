from collections import Counter
from math import factorial
from itertools import product, starmap
from functools import reduce


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        palindrome_freq_set = generate_palindrome_digit_frequency_set(n, k)
        r = map(lambda x: get_valid_permutations_from_tuples(x, n), palindrome_freq_set)
        return sum(r)


def generate_palindrome_digit_frequency_set(
    n: int, k: int
) -> set[tuple[int, int, int, int, int, int, int, int, int, int]]:
    """팰린드롬을 만들 수 있는 숫자 개수 조합을 돌려줍니다.

    반환값은 0부터 9의 숫자가 팰린드롬에 등장하는 횟수를 tuple로 묶은 set입니다.

    Examples:
        예를 들어, n = 2, k = 4인 경우엔 다음과 같은 두 개의 값만 돌아옵니다:

        >>> generate_palindrome_digit_frequency_set(2, 4)
        {(0, 0, 0, 0, 2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 2, 0)}

        이는 두 자리 수에서 4의 배수 팰린드롬을 만들 수 있는 경우가 44와 88로
        각각 "4" 2회 사용, "8" 2회 사용 2가지밖에 없기 때문입니다.
    """
    all_digits = "0123456789"
    if n == 1:
        r = map(lambda x: x, all_digits)
    else:
        # 전체 수를 자리수를 반으로 가른 후, 앞에 들어갈 수를 만들어내고
        # 뒤의 자리는 해당 수의 대칭값을 사용
        prefix_len = n // 2
        prefixes = product(all_digits, repeat=prefix_len)
        # 자리수가 홀수인 경우, 중간 자리 수를 고려해야 함
        if n % 2:
            r = product(prefixes, all_digits)
            r = starmap(lambda x, y: "".join(x) + y + "".join(reversed(x)), r)
        # 자리수가 짝수인 경우엔 중간자리 없이 대칭을 바로 사용
        else:
            r = map(lambda x: "".join(x) + "".join(reversed(x)), prefixes)
    # 첫 자리가 "0"으로 시작하는 경우는 존재할 수 없는 수이므로 필터
    # k로 나누어 떨어지지 않는 경우 또한 조건에서 벗어나므로 필터
    r = filter(lambda x: x[0] != "0" and int(x) % k == 0, r)
    # 해당 수를 구성하는 각 숫자가 얼마나 쓰였는지 `Counter` 클래스를 이용해 계산
    r = map(Counter, r)
    # 0부터 9까지의 숫자가 사용된 횟수를 순서대로 구해서 tuple로 저장
    r = map(lambda x: tuple(x.get(digit, 0) for digit in all_digits), r)
    # 중복인 경우를 걸러내기 위해 `set` 자료형으로 유니크한 조합만을 반환
    return set(r)


def get_valid_permutations_from_tuples(
    t: tuple[int, int, int, int, int, int, int, int, int, int],
    n: int,
) -> int:
    """팰린드롬을 만들 수 있는 숫자의 등장횟수 값을 이용해, 실제 가능한
    good integer 조합 수를 구하는 함수입니다."""
    # 앞자리에 0이 들어가는 경우를 포함, 모든 조합 수는 아래 공식으로 구할 수 있음
    # n! / ( (num_0)! * (num_1)! * ... * (num_9)! )
    total_permutations = reduce(lambda x, y: x // factorial(y), t, factorial(n))
    # 숫자 0이 단 한 번도 사용되지 않은 경우, 불가능한 조합이 없음
    if t[0] == 0:
        invalid_permutations = 0
    # 숫자 0이 사용된 경우, 숫자 0이 맨 앞에 사용된 조합을 계산해 빼야 함
    else:
        r = (v - 1 if i == 0 else v for i, v in enumerate(t))
        invalid_permutations = reduce(lambda x, y: x // factorial(y), r, factorial(n - 1))
    return total_permutations - invalid_permutations


if __name__ == "__main__":
    n = 3
    k = 5
    result = Solution().countGoodIntegers(n, k)
    print(result)
