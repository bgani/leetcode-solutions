# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # return null if target doesn't exits, return current root if we found target)
        if root is None or val == root.val:
            return root
        
        # recursive call of searchBST depending serach val might be on righ or left node
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val: 
            return self.searchBST(root.left, val)