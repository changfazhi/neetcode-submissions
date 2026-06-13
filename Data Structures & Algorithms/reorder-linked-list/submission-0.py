# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # i need to find the middle using fast and slow pointers
        # split the 2 and reverse the 2nd half 
        # merge the 2 linked list and return it
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # now i need to split the 2 list be seperating the next pointers

        l1 = head
        l2 = slow.next
        slow.next = None
        # reverse the l2
        curr = l2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # now prev is the second list
        l2 = prev
        # now need to merge them
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
            tail.next = l2
            tail = tail.next
            l2 = l2.next
        tail.next = l1 or l2
        
        #return dummy.next

