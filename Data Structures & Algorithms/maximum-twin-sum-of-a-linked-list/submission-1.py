# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev,cur=None,slow
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        res=0
        start,end=head,prev
        while end:
            res=max(res,start.val+end.val)
            start=start.next
            end=end.next
        return res