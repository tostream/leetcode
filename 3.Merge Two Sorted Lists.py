# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = process = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                process.next=list2
                list2=list2.next
            else:
                process.next=list1
                list1=list1.next
            process = process.next
        if list1:
            process.next = list1
        if list2:
            process.next = list2

        return res.next