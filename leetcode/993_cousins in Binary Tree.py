class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        print(x,y)
        queue = {root.val: [None,root]}
        while queue:
            if x in queue and y in queue and queue[x][0] != queue[y][0]: return True
            if x in queue and y not in queue or y in queue and x not in queue: return False
            if x in queue and y in queue and queue[x][0] == queue[y][0]: return False
            
            
            temp = {}
            for key in queue:
                node = queue[key][1]
                parent = node.val
                if node.left: temp[node.left.val] = [parent, node.left]
                if node.right: temp[node.right.val] = [parent, node.right]
            queue = temp
        
        return False