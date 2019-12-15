class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        if self.root is None: 
            self.root = Node(val)
            return self.root

        current = self.root
        while True:
            if val >= current.val:
                if current.right is None:
                    current.right = Node(val)
                    return current.right
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = Node(val)
                    return current.left
                else:
                    current = current.left
    
    def binary_search_iter(self,val):
        current = self.root
        while current is not None:
            if current.val == val: return True
            elif val < current.val: current = current.left
            else: current = current.right

        return False

tree = BST()
tree.insert(10)
tree.insert(20)
tree.insert(15)
tree.insert(21)
tree.insert(14)

print(tree.binary_search_iter(14))


# a = Node(10)
# b = Node(5)
# c = Node(15)
# d = Node(3)
# e = Node(7)
# f = Node(17)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# # if elif else
# #  mutually exclude

# def binarySearchRecur(root,val):
#     if root is None: return False
#     if root.val == val: return True

#     elif val < root.val:
#         return binarySearchRecur(root.left,val)
#     else:
#         return binarySearchRecur(root.right,val)


# print(binarySearchRecur(a,7), #true
# binarySearchRecur(a,5), #true
# binarySearchRecur(a,10), #true
# binarySearchRecur(a,16), #false
# binarySearchRecur(a,12)) #false


def binary_search_iter(root,val):
    current = root
    while current is not None:
        if current.val == val: return True
        elif val < current.val: current = current.left
        else: current = current.right

    return False

# print(binary_search_iter(a,7), #true
# binary_search_iter(a,5), #true
# binary_search_iter(a,10), #true
# binary_search_iter(a,16), #false
# binary_search_iter(a,12)) #false