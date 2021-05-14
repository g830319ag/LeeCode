# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_len(self, l):
        l_len = 0
        while(l):
            l_len += 1
            l = l.next
        return l_len
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_len = self.get_len(l1)
        l2_len = self.get_len(l2)
        
        if l2_len > l1_len:
            step = l2_len
        else:
            step = l1_len
          
        result = ListNode(0)
        temp = result
        while step:
            temp.next = ListNode(0)
            temp = temp.next
            if step<=l1_len:
                temp.val += l1.val
                l1 = l1.next
            if step<=l2_len:
                temp.val += l2.val
                l2 = l2.next
            step -= 1
        
        
        temp = result
        while temp:
            if_add = temp.next
            while if_add and if_add.val == 9:
                if_add = if_add.next
            if if_add and if_add.val>9:
                while temp != if_add:
                    temp.val += 1
                    temp = temp.next
                    temp.val -= 10
            else:
                temp = if_add
        if result.val:
            return result
        else:
            return result.next
