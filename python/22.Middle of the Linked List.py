# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        count = 0
        while result:
            count+=1
            result = result.next
        mid = count // 2
        j=0
        while j < mid:
            j+=1
            head= head.next
        return head