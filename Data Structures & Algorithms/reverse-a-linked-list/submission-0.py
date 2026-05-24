# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(prev, head):
        if head:
            if head.next:
                nex = head.next
                head.next = prev
                return Solution.rev(head, nex)
            else:
                head.next = prev
                return head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #store curr.next
        #make curr.next = prev
        #recursively call through next
        if head == None:
            return head
        
        return Solution.rev(None, head)
       

    

            

        