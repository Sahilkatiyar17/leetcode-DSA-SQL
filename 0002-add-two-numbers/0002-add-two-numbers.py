# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        left=dummy
        carry=0
        cur1,cur2=l1,l2
        while cur1 or cur2 or carry:
            cur1_val=cur1.val if cur1!=None else 0
            cur2_val=cur2.val if cur2!=None else 0
            output= cur1_val + cur2_val + carry
            carry = output // 10
            output = output % 10


            left.next=ListNode(output)
            left=left.next
            cur1= cur1.next if cur1 else None
            cur2= cur2.next if cur2 else None
        
        return dummy.next
            
        