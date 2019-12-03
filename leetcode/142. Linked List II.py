class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return None
        fast = slow = head
        c_l = 0
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            c_l += 1
            if fast is slow: break
            if fast is None or slow is None or fast.next is None: return None
        fast = slow = head
        for _ in range(c_l):
            fast = fast.next    
        while fast != slow:
            fast = fast.next
            slow = slow.next     
        return fast