class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
        
    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head
        if not new_head.next:
            self.tail = new_head
        
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr=self.head
        for i in range(index):
            if curr.next:
                curr=curr.next
            else:
                return False
        if not curr.next:
            return False
        
        if curr.next == self.tail:
            self.tail = curr
        curr.next = curr.next.next
        
        return True

        
    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next