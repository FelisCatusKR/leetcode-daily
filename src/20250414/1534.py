from itertools import combinations, starmap


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        r = starmap(lambda i, j, k: _check_if_triplet_is_good(i, j, k, a, b, c), combinations(arr, 3))
        return sum(r)


def _check_if_triplet_is_good(num_i, num_j, num_k, a, b, c) -> int:
    if abs(num_i - num_j) > a:
        return 0
    if abs(num_j - num_k) > b:
        return 0
    if abs(num_i - num_k) > c:
        return 0
    return 1


if __name__ == "__main__":
    arr = [3,0,1,1,9,7]
    a = 7
    b = 2
    c = 3
    result = Solution().countGoodTriplets(arr, a, b, c)
    print(result)
