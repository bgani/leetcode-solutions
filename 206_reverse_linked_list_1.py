# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach with Two Pointers T: O(n), S: (1)
        # We start with prev as Null, and curr as head
        prev, curr = None, head

        # until curr = None
        while curr: 
            # shift current to current.next, to do that we need to save curr.next to temp var
            nxt = curr.next

            # set current.next as prev (null)
            curr.next = prev 

            # shift prev to current
            prev = curr

            # shft current to current.next
            curr = nxt

            # return prev because it's gonna be equal to New head
        return prev