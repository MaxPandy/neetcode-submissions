# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None or not head:
            return None
        dummy=ListNode()
        dummy.next=head
        
        cur=head
        length=0
        while cur:
            length+=1
            cur=cur.next
        index=length-n+1
        print(index)

        prev=dummy
        cur=head
        i=1
        while i<index:
            cur,prev=cur.next,prev.next
            i+=1
        prev.next=cur.next
        return dummy.next
