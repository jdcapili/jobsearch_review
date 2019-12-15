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

# if elif else
#  mutually exclude

def binarySearchRecur(root,val):
    if root is None: return False
    if root.val == val: return True

    elif val < root.val:
        return binarySearchRecur(root.left,val)
    else:
        return binarySearchRecur(root.right,val)


print(binarySearchRecur(a,7)) #true
print(binarySearchRecur(a,5)) #true
print(binarySearchRecur(a,10)) #true
print(binarySearchRecur(a,16)) #false
print(binarySearchRecur(a,12)) #false
