# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge the first 2 list, then traverse after each list and add.
        # in order to add, whenever my node is higher or equal, node.next = newonde, newnode.next = next ndoe
        # edge case
        if not lists:
            return None
        
        def mergeLst(l1,l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            tail.next = l1 or l2
            return dummy.next
        
        merged = lists[0]
        for lst in lists[1:]:
            merged = mergeLst(merged, lst)
        
        return merged

        