# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        aL = bL = 0
        a,b = headA,headB
        while a:
            aL += 1
            a = a.next
        while b:
            bL += 1
            b = b.next
        if aL > bL:
            headA,headB = headB,headA
            
        for _ in range(abs(aL-bL)):
            headB = headB.next
            
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA