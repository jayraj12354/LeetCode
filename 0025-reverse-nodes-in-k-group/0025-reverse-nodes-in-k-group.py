# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        demo=ListNode(0)
        def f(lishead,n,num,k,lasthead):
            if num==n//k:
                if lasthead:
                    lasthead.next=lishead
                return 

            i=0
            curr=lishead
            prev=None
            while i<k and curr:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
                i+=1
            lasthead.next=prev
            f(curr,n,num+1,k,lishead)

        found=False
        newhead=None
        node=head
        n=0
        while node:
            n+=1
            if n==k:
                newhead=node
            node=node.next

        f(head,n,0,k,demo)

        return newhead
            
        

        