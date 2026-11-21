class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


class LinkedList:
    
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=self.head
    
    def get(self, index: int) -> int:
        curr=self.head.next
        i=0
        while curr:
            if i==index:
                return curr.val
            i+=1
            curr=curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node=ListNode(val)
        new_node.next=self.head.next
        self.head.next=new_node
        if new_node.next is None:
            self.tail=new_node

    def insertTail(self, val: int) -> None:
        tail_node=ListNode(val)
        self.tail.next=tail_node
        self.tail=tail_node

    def remove(self, index: int) -> bool:
        curr=self.head
        i=0
        while curr and i!=index:
            curr=curr.next
            i+=1
        if curr and curr.next:
            if curr.next==self.tail:
                self.tail=curr
            curr.next=curr.next.next
            return True
        return False
            

    def getValues(self) -> List[int]:
        curr=self.head
        result=[]
        while curr.next:
            curr=curr.next
            result.append(curr.val)
        return result
