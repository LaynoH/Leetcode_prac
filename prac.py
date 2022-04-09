# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
from decimal import Decimal
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        dummy = None
        carry = 0
        while l1!=None or l2!=None :
            sumnum = carry
            if l1!=None:
                sumnum+= l1.val
                l1 = l1.next
            if l2!=None:
                sumnum+= l2.val
                l2 = l2.next    
            tmp = ListNode(sumnum % 10)
            carry = sumnum//10
            
            if head==None:
                head = dummy = tmp
            else:
                dummy.next = tmp
                dummy = dummy.next
        
        if carry!=0:
            dummy.next = ListNode(carry)
        
        return head
