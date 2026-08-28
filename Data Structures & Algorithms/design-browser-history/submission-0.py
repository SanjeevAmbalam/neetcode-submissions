class Node:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(val=homepage)

    def visit(self, url: str) -> None:
        newNode = Node(val=url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.prev:
                return self.curr.val
            else:
                self.curr = self.curr.prev 
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.next:
                return self.curr.val
            else:
                self.curr = self.curr.next 
        return self.curr.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)