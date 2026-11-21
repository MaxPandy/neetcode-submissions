class ListNode:
    def __init__(self, val=0,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0

    def get(self, index: int) -> int:
        i=0
        p=self.head
        while i<=index and p:
            p=p.next
            i+=1
        if p and p.next:
            return p.val
        return -1



    def addAtHead(self, val: int) -> None:
        temp=self.head.next
        self.head.next=ListNode(val,self.head,temp)
        temp.prev=self.head.next
        self.size+=1

    def addAtTail(self, val: int) -> None:
        temp=self.tail.prev
        self.tail.prev=ListNode(val,temp,self.tail)
        temp.next=self.tail.prev
        self.size+=1 

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size<index:
            return
        elif self.size==index:
            self.addAtTail(val)
        else:
            p=self.head
            i=0
            while i<index:
                p=p.next
                i+=1
            temp=p.next
            p.next=ListNode(val,p,temp)
            temp.prev=p.next
            self.size+=1
            

    def deleteAtIndex(self, index: int) -> None:
        if self.size<=index:
            return
        else:
            p=self.head
            i=0
            while i<=index:
                p=p.next
                i+=1
            temp=p.next
            p.prev.next=temp
            temp.prev=p.prev
            self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)