# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=ListNode(0)
        first=head
        second=head.next
        prev.next=first
        newhead=prev
        while first and second:
            prev.next=second

            first.next=second.next
            second.next=first
            prev=prev.next.next

            first=first.next
            if first:
                second=first.next
            else:
                second=None

        return newhead.next

        

        