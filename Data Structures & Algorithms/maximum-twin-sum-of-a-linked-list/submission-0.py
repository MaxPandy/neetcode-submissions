# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        maxSum=0
        for i in range(len(res)//2):
            maxSum=max(maxSum,res[i]+res[len(res)-i-1])
        return maxSum