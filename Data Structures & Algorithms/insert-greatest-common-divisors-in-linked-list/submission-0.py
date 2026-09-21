# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a: int, b: int):
        if a == b:
            return a
        elif a > b:
            return self.gcd(a - b, a)
        else:
            return self.gcd(b - a, a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        temp2 = head.next

        while temp1 and temp2:
            c = self.gcd(temp1.val, temp2.val)
            node = ListNode(c, None)
            temp1.next = node
            node.next = temp2
            temp1 = temp2
            temp2 = temp2.next




        return head

        