# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # write the reverse helper function
        def reverseLst(lst):
            curr = lst
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev # changing the direction of the link
                prev = curr # advancing pointer
                curr = temp # advancing pointer
            return prev # prev is the start of the reversed linked list
        counter = 1
        curr = head
        prev = None
        while curr:
            if counter == 1:
                # need to consider if the prev node before start need to disconnect
                # means i need a prev curr
                start = curr
                # if have prev, means that this is in the middle
                # so i need to disconnect the links before my start
                # so i put prev.next = None ??
                beforeStart = None
                if prev:
                    beforeStart = prev # node before start
                checkNode = start # check k nodes infront
                enough = True
                for _ in range(k):
                    if checkNode == None:
                        enough = False
                        break
                    checkNode = checkNode.next
                if not enough:
                    break
                prev = curr # advancing my prev pointer to curr
                curr = curr.next # advancing my curr pointer to the next
                counter += 1
                continue
            if counter == k:
                nextPointer = curr.next
                curr.next = None
                if beforeStart:
                    beforeStart.next = None
                revLst = reverseLst(start)
                # traverse the reversed linked list to find the last node and connect
                revPointer = revLst
                while revPointer.next:
                    revPointer = revPointer.next
                if beforeStart:
                    beforeStart.next = revLst # connecting the node before revLst to revLst
                else:
                    head = revLst
                revPointer.next = nextPointer # connect the last node to the next node
                counter = 1
                prev = revPointer
                curr = nextPointer
            else:
                prev = curr
                curr = curr.next
                counter += 1
        return head

        