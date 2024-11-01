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
        if not head:
            return None
        
        HashMap = dict()
        curr = head
        while curr:
            HashMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                HashMap[curr].next = HashMap[curr.next]
            if curr.random:
                HashMap[curr].random = HashMap[curr.random]
            curr = curr.next
        
        return HashMap[head]