# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        beforeHead = ListNode(9999, head) # [ 9999, 1, 2, 3, 4]
        right = head # [9999, right/1, 2, 3, 4]
        left = beforeHead # [left/9999, right/1, 2, 3, 4]

        while n > 0: # we'll be at [left/9999, 1, 2, right/3, 4]
            right = right.next 
            n -= 1
        
        while right:           # [left/9999, 1, 2, right/3, 4] <-- before
            right = right.next # [9999, left/1, 2, 3, right/4] <-- loop one
            left = left.next   # [9999, 1, left/2, 3, 4, right/null] <-- loop two
        
        left.next = left.next.next
        return beforeHead.next