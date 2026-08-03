# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while (len(lists)>1):
            merged = []
            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1,l2))
            lists = merged

        return lists[0]
   
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2
        head = None

        if t1 and not t2:
            return t1
        elif t2 and not t1:
            return t2
        elif not t1 and not t2:
            return None
        
        if t1.val < t2.val:
            head = t1
            t1 = t1.next
        else:
            head = t2
            t2 = t2.next

        t3 = head
        while t1 or t2:
            if t2 is None:
                t3.next = t1
                break
            if t1 is None:
                t3.next = t2
                break
            
            if t1.val < t2.val:
                t3.next = t1
                t1 = t1.next
            else:
                t3.next = t2
                t2 = t2.next
            t3 = t3.next
            

        return head