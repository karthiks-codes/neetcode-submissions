# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        minusOneNode = None
        currentNode = head
        

        while currentNode:
            temporaryNode = currentNode.next
            currentNode.next = minusOneNode
            minusOneNode = currentNode
            currentNode = temporaryNode

        return minusOneNode


        

            



        



        


        

        

        