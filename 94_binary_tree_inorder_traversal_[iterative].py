# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        stack = []
        cur = root

        # while cur is pointing at a real node or stack is not empty iterate through tree
        while cur or stack:
            while cur:
                # append current node to stack
                stack.append(cur)
                # go left as long we can, so move current pointer to left
                cur = cur.left

            # at this point cur points at null because we go to the last left leaf (which has no child)
            
            # pop node from stack and assign to cur, then append it's val to result
            cur = stack.pop()
            res.append(cur.val)

            # now we go to right sub-tree and reapeat all above steps
            cur = cur.right

        
        return res