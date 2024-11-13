"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}
        
        if not head:
            return head
        
        curr = head
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                hashMap[curr].random = hashMap[curr.random]
            if curr.next:
                hashMap[curr].next = hashMap[curr.next]
            curr = curr.next
        
        print(head)
        
        return hashMap[head]