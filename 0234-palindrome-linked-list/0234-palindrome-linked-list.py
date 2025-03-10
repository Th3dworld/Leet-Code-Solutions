# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first,second = head,prev
        while first and second:
            if first.val != second.val: return False
            first = first.next
            second = second.next
        
        return True