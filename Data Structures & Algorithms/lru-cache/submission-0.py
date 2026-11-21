class ListNode:
    def __init__(self,val=0,key=0):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
       self.cap=capacity
       self.values={}
       self.head,self.tail=ListNode(-1),ListNode(-1)
       self.head.next=self.tail
       self.tail.prev=self.head 

    def place_to_end(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

        node.prev=self.tail.prev
        node.next=self.tail

        self.tail.prev.next=node
        self.tail.prev=node

    def remove_first(self):
        key=self.head.next.key
        self.values.pop(key)
        self.head.next=self.head.next.next
        self.head.next.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        node=self.values[key]
        self.place_to_end(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key].val=value
            node=self.values[key]
            self.place_to_end(node)
        else:
            newNode=ListNode(value,key)
            self.values[key]=newNode

            newNode.prev=self.tail.prev
            newNode.next=self.tail
            self.tail.prev.next=newNode
            self.tail.prev=newNode
            if len(self.values)>self.cap:
                self.remove_first()


        
