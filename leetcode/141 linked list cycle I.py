class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        fast,slow = head.next.next, head.next
        
        def findcycle(fnode, snode):
            if not fnode or not fnode.next: return False
            if fnode is snode: return True
            
            fnode = fnode.next.next
            snode = snode.next
            
            return findcycle(fnode,snode)
        
        return findcycle(fast,slow)