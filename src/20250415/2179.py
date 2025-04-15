class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        dp_dict = {}

        for i, num in enumerate(nums1, start=1):
            dp_dict[num] = i

        for i in range(n):
            nums2[i] = dp_dict[nums2[i]]

        left_arr = [0 for _ in range(n)]
        right_arr = [1 for _ in range(n)]
        left_segtree = SegTree(left_arr)
        right_segtree = SegTree(right_arr)
        left_segtree.update(nums2[0] - 1, 1)
        right_segtree.update(nums2[0] - 1, 0)

        result = 0
        for i in range(1, n - 1):
            idx = nums2[i]
            right_segtree.update(idx - 1, 0)
            if idx - 2 >= 0:
                left = left_segtree.query(0, idx -2)
            else:
                left = 0
            right = right_segtree.query(idx, n - 1)
            result += left * right
            left_segtree.update(idx - 1, 1)

        return result


class SegTree:
    n: int
    tree: list[int]

    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.tree = [0 for _ in range(4 * self.n)]
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr: list[int], node: int, start: int, end: int):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node + 1, start, mid)
            self._build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(
        self,
        idx: int,
        val: int,
        node: int = 0,
        start: int | None = None,
        end: int | None = None,
    ):
        if start is None:
            start = 0
            end = self.n - 1
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, 2 * node + 1, start, mid)
            else:
                self.update(idx, val, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(
        self,
        l: int,
        r: int,
        node: int = 0,
        start: int | None = None,
        end: int | None = None,
    ) -> int:
        if start is None:
            start = 0
            end = self.n - 1
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(l, r, 2 * node + 1, start, mid)
        right_sum = self.query(l, r, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum
