# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        reverse = prev # preserve reserve to reverse later
        copy = reverse # copy would be used to traverse
        prev = None
        # reverse is the head of the reversed list
        # prev is now the previous node of the reversed list
        if n == 1:
            reverse = reverse.next

        else:
            for i in range(n-1):
                prev = copy
                copy = copy.next
            
            
            # now copy is at the node i want to remove
            # however in order to remove i need to keep track of the node previous in order to link the nodes
            prev.next = copy.next
                

        # now i gotta reverse it back
        curr = reverse
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


        