# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        first, second = head, prev

        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1,tmp2
        
        return head



    
