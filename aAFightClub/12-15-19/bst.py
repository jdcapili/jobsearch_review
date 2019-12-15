class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

a = Node(10)
b = Node(5)
c = Node(15)
d = Node(3)
e = Node(7)
f = Node(17)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

