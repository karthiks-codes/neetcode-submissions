# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer1 = head
        pointer2 = head.next

        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        p = pointer1.next
        previous = None 
        pointer1.next = None

        while p:
            temp = p.next
            p.next = previous
            previous = p
            p = temp

        
        left = head
        right = previous

        while right:
            t1, t2 = left.next, right.next
            left.next = right
            right.next = t1
            left, right = t1, t2

        


        

        
        