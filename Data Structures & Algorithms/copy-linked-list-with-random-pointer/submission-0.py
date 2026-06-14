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
        # should use a hashmap in order to store node.val:node.random
        # i should iterate thru the head first in order to get all the random nodes into the hashmap

        # traverse head to fill up my dict
        dictMap = {None: None}
        curr = head
        while curr:
            dictMap[curr] = Node(curr.val)
            curr = curr.next
        
        # dictmap is all filled up, i know all the nodes associated with their respecitive random 
        # now i need to create a deep copy
        dummy2 = dictMap[head]
        tail = dummy2
        curr = head
        while curr:

            tail = dictMap[curr]
            tail.random = dictMap[curr.random] # wire up random pointers
            tail.next = dictMap[curr.next] # wire up next pointers
            curr = curr.next # advance my created linked list forward
            tail = tail.next
            
        return dummy2

        