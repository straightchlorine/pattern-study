"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

   3
  / \
9   20
   /  \
  15  7

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(preorder: list[int], inorder: list[int]):
    """
    Recursion seems the way for this problem.

    So basically:
    1. preorder has root first - so we know where to start
    2. inorder gives nodes on left and right for each point

    So in a way preorder gives the depth:
    3 9 20 15 7

    And inorder gives ordering
    9 3 15 20 7

    So basically we know that 9 is on the left from 3, and 20 is on the right
    of the tree just from preorder:
      3
     / \
    9  20

    Then - in a recursive call we can go to 9; to the left - nothing
    so it doesn't have left child, on the right - 3

    here we need lookup i.e. what was added what wasn't. so basically 3 would be the right
    of 9 but we do hashmap[3] and it returns True (let's assume we judge added/not added)

    after checking both - we finish and return the root - it was just 9

    Then we would be finished with left branch

    And second recursive call would go towards right side and we do similar thing
    we find 20 (for now all I have in mind is just for or an indexof call)

    we look for 20 in inorder and we see that on the left there is 15 and right 7
    checks for both 15 and 7 return false - so they werent added - we  can move onward
    """

    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    root_index = inorder.index(root.val)

    # first left side
    root.left = build(
        preorder[1:],
        inorder[:root_index],
    )

    # then right side
    root.right = build(
        preorder[1 + len(inorder[:root_index]) :],
        inorder[root_index + 1 :],
    )

    return root


def solution(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    map = {}
    for index, value in enumerate(inorder):
        map[value] = index

    pre_iter = iter(preorder)

    def dfs(left, right):
        if left >= right:
            return None

        root_val = next(pre_iter)
        root = TreeNode(val=root_val)

        root.left = dfs(left, map[root_val])
        root.right = dfs(map[root_val] + 1, right)

        return root

    return dfs(0, len(preorder))


if __name__ == "__main__":
    solution_a = solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(solution_a)
