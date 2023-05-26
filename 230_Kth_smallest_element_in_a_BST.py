# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # number elements we visited, (n == k) is our base case
        stack = [] # we iteratively push nodes to stack, which will help us to pop elements in increasing order
        cur = root # current node that we are visiting


        while cur or stack: # while cur is not null and stack is not empty
            while cur:
                stack.append(cur)
                # go left as much we can
                cur = cur.left

            cur = stack.pop() # pop most recent and assign it to cur
            n += 1
            if(n == k): # we found k th element
                return cur.val

            # now we can go to left sub-tree
            cur = cur.right