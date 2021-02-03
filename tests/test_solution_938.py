from solutions.solution_938 import Solution, TreeNode


def test_range_sum_bst():
    solution = Solution()
    tree = TreeNode()
    for x in [10, 5, 15, 3, 7, 18]:
        tree.insert(x)
    assert solution.rangeSumBST(tree, 7, 15) == 32

    tree = TreeNode()
    for x in [10, 5, 15, 3, 7, 13, 18, 1, 6]:
        tree.insert(x)
    assert solution.rangeSumBST(tree, 6, 10) == 23
