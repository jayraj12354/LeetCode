# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head=ListNode(0)
        copy=head
        while  lists:
            smallNode=[None,None]
            i=0
            # parr=[]
            # print(smallNode,lists)
            # print()
            while i<len(lists):
                if lists[i] and (not(smallNode[0]) or lists[i].val<smallNode[0].val  ):
                    smallNode=[lists[i],i]
                elif not(lists[i]):
                    # parr.append(i)
                    lists.pop(i)
                    continue
                i+=1
            # print(smallNode,lists,"hiiiiii",len(lists))
            # print()
            # print()

            if not lists:
                break
            head.next=smallNode[0]
            lists[smallNode[1]]=lists[smallNode[1]].next
            head=head.next
            # for j in parr:
            #     lists.pop(j)

        return copy.next




        