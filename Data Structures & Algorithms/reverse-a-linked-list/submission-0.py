# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        cur = head
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
        newHead = head
        while stack:
            t = stack.pop()
            head.val = t
            head = head.next

        return newHead


        

        

        