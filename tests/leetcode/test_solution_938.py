# import pytest
# from src.solution_938 import Solution, TreeNode


# @pytest.mark.parametrize("test_input,expected", [([10, 5, 15, 3, 7, 18], 32)])
# def test_range_sum_bst_params(test_input, expected):
#     solution = Solution()
#     tree = TreeNode()

#     for x in test_input:
#         tree.insert(x)

#     assert solution.rangeSumBST(tree, 7, 15) == expected


# def test_range_sum_bst():
#     solution = Solution()
#     tree = TreeNode()

#     for x in [10, 5, 15, 3, 7, 18]:
#         tree.insert(x)
#     assert solution.rangeSumBST(tree, 7, 15) == 32

#     tree = TreeNode()
#     for x in [10, 5, 15, 3, 7, 13, 18, 1, 6]:
#         tree.insert(x)
#     assert solution.rangeSumBST(tree, 6, 10) == 23
