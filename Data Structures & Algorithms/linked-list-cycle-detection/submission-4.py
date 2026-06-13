# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # i will need a fast and slow pointer
        # the fast pointer will be moving at twice the speed of the slow pointer
        # i will need the fast pointer to lap the slow pointer - > if lap means True else it is false

        #initial_value = head.val
        fast = head
        slow = head
        if not head:
            return False
            
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow.val == fast.val:
                return True
        
        return False
        
        