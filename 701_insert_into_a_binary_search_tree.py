# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # base case, if there is no node insert new one
        if not root:
            return TreeNode(val)

        if val > root.val:
            # go to right node, because in BST bigger value always must be on right child
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            # go to left node, because in BST smaller value always must be on left child
            root.left = self.insertIntoBST(root.left, val)

        # we do not consider when val = root.val because we are guaranteed that the new val doesn't exist in the BST

        return root