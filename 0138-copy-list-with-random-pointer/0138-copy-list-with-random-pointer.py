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
            return head
        
        hashMap = {None : None}
        cur = head

        while cur:
            hashMap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head

        while cur:
            hashMap[cur].next = hashMap[cur.next]
            hashMap[cur].random = hashMap[cur.random]
        
        return hashMap[head]