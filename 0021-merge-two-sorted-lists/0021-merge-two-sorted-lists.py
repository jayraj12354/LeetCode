# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1,list2)
        node1=list1
        node2=list2
        head=ListNode(0)
        copy=head

        while node1 and node2:
            print("h1111",node1.val,node2.val)
            if node1.val<node2.val:
                head.next=node1
                node1=node1.next
            else:
                head.next=node2
                node2=node2.next

            head=head.next

        if node1:
            head.next=node1
        if node2:
            head.next=node2

        return copy.next
    