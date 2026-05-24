# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists( self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2 == None:
            if list1==None and list2!= None:
                return list2
            else:
                return list1

        val1 = list1.val
        val2 = list2.val
        if min(val1, val2) == val1:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        curr = head

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if min(val1, val2) == val1:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        #in case one list runs out
        if list1:
                curr.next = list1
        if list2:
            curr.next = list2

        return head
