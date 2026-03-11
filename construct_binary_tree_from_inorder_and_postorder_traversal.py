"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:

    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(inorder: list[int], postorder: list[int]):
    """
    Okay let's do this one properly

    1. we do the map of the inorder - as in the previous case
    2. postorder has the root at the end and if we get the root of the inorder
    (it's id) then postorder[1: 1 + left_size] is the left and
    postorder[1 + left_size:] would be the right

    So what we need is appropriate left size for the arrays which are getting smaller

    postorder[:left_size]

    So let's go with the proper way and not slice but start the boundaries
    left and right would be the starts and ends of the left side

    so for the left tree it would be
    0, left_size
    and for the right
    left_size, len(inorder/postorder)

    """

    map = {}
    for index, value in enumerate(inorder):
        map[value] = index

    def dfs(left, right):
        if left >= right:
            return None

        root_val = postorder.pop()
        root = TreeNode(val=root_val)

        root.right = dfs(map[root_val] + 1, right)
        root.left = dfs(left, map[root_val])

        return root

    return dfs(0, len(postorder))


if __name__ == "__main__":
    solution_a = solution([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(solution_a)
