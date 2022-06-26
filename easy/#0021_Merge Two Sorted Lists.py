# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        head = None
        
        while list1!=None and list2!=None :
            tmp = list1 if list1.val<=list2.val else list2
            
            if list1.val>list2.val:
                list2 = list2.next
            else:
                list1 = list1.next
            
            if head==None:
                head = dummy = tmp
            else:
                dummy.next = tmp
                dummy = dummy.next

        if list1 or list2:
            if head==None:
                head = dummy = list1 if list1 else list2
            else:
                dummy.next = list1 if list1 else list2
                dummy = dummy.next
     
        return head
