# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        res = dummy = ListNode(-101)
        
        while curr:
            if curr.val != dummy.val:
                dummy.next = curr
                dummy = dummy.next
            else:
                dummy.next = None
            curr = curr.next
        return res.next