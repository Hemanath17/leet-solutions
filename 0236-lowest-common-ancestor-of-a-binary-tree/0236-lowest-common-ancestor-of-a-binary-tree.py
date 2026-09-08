# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left_result = self.lowestCommonAncestor(root.left,p,q)
        right_result = self.lowestCommonAncestor(root.right,p,q)
        if left_result is not None and right_result is not None:
            return root
        if left_result is not None:
            return left_result
        if right_result is not None:
            return right_result
        return None