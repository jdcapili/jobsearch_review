class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

two = ListNode(2)
four = ListNode(4)
three = ListNode(3)
two.next = four
four.next = three
# 2 -> 4 -> 3

five = ListNode(5)
six = ListNode(6)
four_ = ListNode(4)
five.next = six
# six.next = four_
# 5 -> 6 -> 4

def printList(l):
    if not l: return
    print(l.val)
    printList(l.next)

def addTwoNumbers(l1,l2):
    curr1 = l1
    curr2 = l2
    carry = 0
    dummy = ListNode(None)
    res = dummy

    while curr1 or curr2:
        v1 = curr1.val if curr1 else 0
        v2 = curr2.val if curr2 else 0
        sum = v1 + v2 + carry
        carry = sum // 10
        digit = sum % 10
        nextNode = ListNode(digit)

        res.next = nextNode
        res = res.next

        if curr1: curr1 = curr1.next
        if curr2: curr2 = curr2.next

    if carry == 1: res.next = ListNode(carry)
    return dummy.next

def addTwoNumbersRecursive(l1,l2,carry = 0):
    if l1 is None and l2 is None:
        if carry == 1: return ListNode(carry)
        else: return None
    
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    sum = v1 + v2 + carry
    carry = sum // 10
    digit = sum % 10
    nextNode = ListNode(digit)
    nextNode.next = addTwoNumbersRecursive(
        l1.next if l1 else l1,
        l2.next if l2 else l2,
        carry
    )
    return nextNode

printList(addTwoNumbersRecursive(two,five))

# time: o(n), where n is longest linked list
# space: o(n+1) where n is longest linked list