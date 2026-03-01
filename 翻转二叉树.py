# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:  # 如果为 None就不存在 left和 right，所以要先判断为空的条件
            return root
        left = self.invertTree(root.left)  # 递归
        right = self.invertTree(root.right)  # 递归
        root.left, root.right = right, left
        return root
