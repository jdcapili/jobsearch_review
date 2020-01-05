# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remainder = 0
        ref = ListNode(None)
        current = ref
        while l1 or l2:
            val_sum = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + remainder
            remainder = 0
            
            if val_sum >= 10: remainder = val_sum // 10
            digit = val_sum % 10
            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if 0 < remainder < 10:
            current.next = ListNode(remainder)
        return ref.next