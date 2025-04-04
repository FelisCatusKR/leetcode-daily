"""1123. Lowest Common Ancestor of Deepest Leaves

Given the `root` of a binary tree, return *the lowest common ancestor of its deepest leaves*.

Recall that:
- The node of a binary tree is a leaf if and only if it has no children
- The depth of the root of the tree is `0`. if the depth of a node is `d`, the depth of each of its children is `d + 1`.
- The lowest common ancestor of a set `S` of nodes, is the node `A` with the largest depth such that every node in `S` is in the subtree with root `A`.
"""

from __future__ import annotations


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        answer, _ = self._traverse(root, 0)
        return answer

    def _traverse(
        self, current: TreeNode, depth: int
    ) -> tuple[TreeNode | None, int]:
        if (
            current.left is not None
            and current.left.left is None
            and current.left.right is None
        ) and (
            current.right is not None
            and current.right.left is None
            and current.right.right is None
        ):
            return current, depth + 1
        if current.left is None and current.right is None:
            return current, depth
        elif current.left is None:
            return self._traverse(current.right, depth + 1)
        elif current.right is None:
            return self._traverse(current.left, depth + 1)

        left_deepest, left_deepest_depth = self._traverse(current.left, depth + 1)
        right_deepest, right_deepest_depth = self._traverse(current.right, depth + 1)

        if left_deepest_depth == right_deepest_depth:
            return current, left_deepest_depth
        elif left_deepest_depth > right_deepest_depth:
            return left_deepest, left_deepest_depth
        else:
            return right_deepest, right_deepest_depth


from dataclasses import dataclass

# Definition for a binary tree node.
@dataclass(frozen=True)
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


def create_node_from_arr(arr: list[int], pos: int) -> TreeNode | None: 
    if pos >= len(arr):
        return None
    if arr[pos] == None:
        return None
    left_pos = pos * 2
    right_pos = pos * 2 + 1
    return TreeNode(
        val=arr[pos],
        left=create_node_from_arr(arr, left_pos),
        right=create_node_from_arr(arr, right_pos),
    )


if __name__ == "__main__":
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    arr = [None] + arr
    root = create_node_from_arr(arr, 1)
    result = Solution().lcaDeepestLeaves(root)
    print(result)
