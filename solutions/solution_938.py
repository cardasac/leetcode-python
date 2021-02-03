"""Binary search tree sum between nodes."""
from typing import List


class TreeNode:
    """Node used for a binary search tree."""

    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """Insert node into the tree.

        :param data: The value to pass to the node
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)

            if data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:  # used for the root node
            self.data = data


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        range_sum: int = 0
        stack: List[TreeNode] = [root]

        while stack:
            node: TreeNode = stack.pop()

            if node:
                if low <= node.data <= high:
                    range_sum += node.data

                if low < node.data:
                    stack.append(node.left)

                if high > node.data:
                    stack.append(node.right)

        return range_sum

        # def dfs(node):
        #     if not node: return 0
        #     if node.val < L: return dfs(node.right)
        #     elif node.val > R: return dfs(node.left)
        #     else: return dfs(node.left) + dfs(node.right) + node.val
        # return dfs(root)

        # if root == None: return 0
        # if root.val > R: return self.rangeSumBST(root.left, L, R)
        # if root.val < L: return self.rangeSumBST(root.right, L, R)
        # return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(
        #     root.right, L, R)

        # def dfs(node):
        #     if node:
        #         if L <= node.val <= R:
        #             self.ans += node.val
        #         if L < node.val:
        #             dfs(node.left)
        #         if node.val < R:
        #             dfs(node.right)
        #
        # self.ans = 0
        # dfs(root)
        # return self.ans
