# time: O(n) | space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        curr = head

        # while element is not null
        while curr:
            # temporary variable 
            nxt = curr.next
            
            curr.next = prev

            # shift pointers
            prev = curr
            curr = nxt
        
        return prev
