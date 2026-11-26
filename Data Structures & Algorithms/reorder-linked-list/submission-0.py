# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        def reverse(head):
            if not head or not head.next:
                return head
            newHead=reverse(head.next)
            head.next.next=head
            head.next=None
            return newHead

        second=reverse(slow.next)
        slow.next=None
        first=head
        
        while second:
            n1,n2=first.next,second.next
            first.next=second
            second.next=n1
            first,second=n1,n2


        

        
    