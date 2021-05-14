# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digits = 0
        ten_d = 0
        temp = head
        while temp:
            temp = temp.next
            digits +=1
            
        while head:
            ten_d = ten_d + head.val*(2**(digits-1))
            head = head.next
            digits = digits - 1
        return ten_d
        
