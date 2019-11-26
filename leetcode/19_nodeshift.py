class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None: return None
        dict = {}
        dict[1] = head
        c = 2
        curr = head.next
        while curr:
            dict[c] = curr
            curr = curr.next
            c += 1
        
        if c-1 == 1 and n == 1: return None
        elif c-1 == n: return dict[2]
        elif n >= 1: dict[c-n-1].next = dict[c-n].next
        
        return head