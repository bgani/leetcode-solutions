# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque() 
        # add root to deque ("deck")
        q.append(root)

        while q:
            queueLength = len(q)
            # init level (sub array)
            level = []
            for i in range(queueLength):
                # pop first node from decque and process it
                node = q.popleft()
                if node:
                    # add value to level 
                    level.append(node.val)
                    # add child nodes to deque
                    if node.left:
                        q.append(node.left)
                    if node.right: 
                        q.append(node.right)
            # make sure that level is not empty before adding to result
            if level: 
                res.append(level)
        
        return res
