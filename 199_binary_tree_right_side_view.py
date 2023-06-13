# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # init deque "deck" with root node
        queue = collections.deque([root])

        # iterate through each level
        while queue:
            # init right most node as Null, later we update it's value
            right_most_node = None
            queue_length = len(queue)
            
            # iterate through nodes of current level
            for i in range(queue_length):
                # pop a node and process it
                node = queue.popleft()
                if node:
                    # update right_most_node
                    right_most_node = node
                    # append child nodes of current node to queue in order to process them at the next level
                    queue.append(node.left)
                    queue.append(node.right)
            
            # if right_most_node at this level is not Null then add it to result
            if right_most_node:
                res.append(right_most_node.val)
        
        return res