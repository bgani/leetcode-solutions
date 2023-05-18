# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return root

        if key > root.val:
            # if key is greater than current node's val go to right node
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # if key is smaller than current node's val go to left node
            root.left = self.deleteNode(root.left, key)
        else:
            # base case with 0 or 1 child
            # if left node is null return right node, and it will replace found node with right child of found node
            # if right node is null return left node, and it will replace found node with left child of found node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # case with 2 children nodes
            # find the min value form right sub-tree and assign it's value to to found node
            cur = root.right
            while cur.left:
                cur = cur.left 
            root.val = cur.val

            # now we need to delete found min value from right sub-tree, because we copied it's value to found "key" node
            # we pass current val as a "search key" which is equal to "min value"
            # at the end it will assign "min value" node as null (base case with 0 and 1 child)
            root.right = self.deleteNode(root.right, root.val)
        
        return root
