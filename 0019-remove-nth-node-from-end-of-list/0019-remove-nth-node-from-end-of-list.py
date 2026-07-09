# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        arr=[head]
        def f(node):
            if not node:
                return 0

            ret=f(node.next)

            if ret +1== n and node==head :
                arr[0]= node.next

            if ret==n:
                if node.next.next:
                    node.next=node.next.next
                else:
                    node.next=None
                    
            return ret+1

        f(head)
        return arr[0]

