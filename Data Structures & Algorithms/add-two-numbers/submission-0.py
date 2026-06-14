# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # needing constant space means that i cannot create a new linked list
        # i need to reverse it and find the num for list 1 and list 2
        # then i will sum the 2 nums 
        # i overwrite one of the list and return the head???

        total = 0

        curr1 = l1
        prev1 = None
        while curr1:
            temp1 = curr1.next # saving curr1.next
            curr1.next = prev1 # reversing the link
            prev1 = curr1 # advancing pointers
            curr1 = temp1
        # prev1 is reversed l1
        sum1 = []
        while prev1:
            sum1.append(prev1.val)
            prev1 = prev1.next

        sum1 = "".join(str(x) for x in sum1)
        sum1 = int(sum1)

        curr2 = l2
        prev2 = None
        while curr2:
            temp2 = curr2.next # saving curr2.next
            curr2.next = prev2 # reversing the link
            prev2 = curr2 # advancing pointers
            curr2 = temp2
        # prev2 is reversed l2
        sum2 = []
        while prev2:
            sum2.append(prev2.val)
            prev2 = prev2.next

        sum2 = "".join(str(y) for y in sum2)
        sum2 = int(sum2)

        total = sum1 + sum2
        total = reversed(str(total))
        total = list(total)
        n = len(total)

        dummy = ListNode()
        tail = dummy
        curr = l1
        # i need to be creating new nodes in order to link
        for i in range(n):
            tail.val = total[i]
            if i < n-1:
                tail.next = ListNode()
                tail = tail.next
            else:
                tail.next = None        
        return dummy


