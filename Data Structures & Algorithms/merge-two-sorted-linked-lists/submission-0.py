class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy stays at the start, tail moves forward
        dummy = ListNode()
        tail = dummy
        
        curr1, curr2 = list1, list2
        
        # Only loop while BOTH have nodes
        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next # Move our pointer forward
            
        # If one list is finished, just attach the rest of the other list
        tail.next = curr1 if curr1 else curr2
        
        # Return the start (skipping the empty dummy node)
        return dummy.next