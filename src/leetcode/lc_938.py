class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(
        self,
        root: TreeNode | None,
        low: int,
        high: int,
    ) -> int: ...
