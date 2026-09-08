class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def blocked(self, top_sandwich):
        curr = self.head
        size = 0
        while curr:
            # true if no students with same preference as top sandwich
            if curr.val == top_sandwich: return False
            curr = curr.next
        return True

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        newNode = Node(-1)
        self.head = self.tail = newNode
        remaining_student_count = len(students)
        sandwiches_index = 0
        for i in range(len(students)):
            newNode = Node(students[i])
            self.tail.next = newNode
            self.tail = self.tail.next
        
        self.head = self.head.next
        number_of_rotations = 0
        while True:
            # modified sandwiches
            if len(sandwiches) == 0: return 0
            #if self.blocked(sandwiches[0]):
            if number_of_rotations == remaining_student_count:
                return remaining_student_count
            if sandwiches[sandwiches_index] == self.head.val:
                sandwiches_index += 1
                number_of_rotations = 0
                self.head = self.head.next
                remaining_student_count -= 1
            else:
                self.tail.next = self.head
                self.tail = self.tail.next
                self.head = self.head.next
                self.tail.next = None
                number_of_rotations += 1


