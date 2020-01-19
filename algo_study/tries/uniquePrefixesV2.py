# input = ["zebra", "dog", "duck", "dogs", "dove"]
#  output = ["z", "dog", "du", "dogs", "dov"]
# from collections import namedtuple

# Edge = namedtuple('Edge', "node count")

class Node:
    def __init__(self):
        self.children = {}
        self.isTerminal = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for idx,char in enumerate(word):
            if char not in cur.children:
                node = Node()
                # initialize char with a list of node and count as elements
                cur.children[char] = [node,0]
            # increment count
            cur.children[char][1]+=1
            # set current node to 1st element of cur.children[char](which is a node)
            cur = cur.children[char][0]
            # if it's the last letter set node's isTerminal to True
            if idx == len(word)-1: cur.isTerminal = True
        

        return self.root
    
    # regular print Trie method
    # prints out words in the trie, (isTerminal is True)
    def printTrie(self, root,cur = ""):
        # print accumulated cur if end of word is detected
        if root.isTerminal: print(cur)
        # only return if there are no more children
        if len(root.children) == 0: return

        # iterate through the children which is an object
        for child in root.children:
            # concat child/letter to current substring
            nxtCur = cur + child
            # move to next node
            nxtNode = root.children[child][0]
            # recursive call to go to next node
            self.printTrie(nxtNode,nxtCur)
    
    def UniquePrefixes(self, curRoot,cur = ""):
        # curRoot is a list with two elements

        # separated count from root
        count = curRoot[1]
        root = curRoot[0]

        # if count is 1, print accumulated cur
        if count == 1:
            print(cur)
            return
        # if end of word is detected, print accumulated cur.
        if root.isTerminal: print(cur)

        # iterate through root's children
        for child in root.children:
            # increment current substring with child
            nxtCur = cur + child
            # getting next node
            nxtNode = root.children[child] 
            # recursive call for unique prefixes
            self.UniquePrefixes(nxtNode,nxtCur)

test = Trie()
test.insert("zebra")
test.insert("zygote")
test.insert("dog")
test.insert("dogs")
test.insert("dove")
test.printTrie(test.root)
print("---------------")
test.UniquePrefixes([test.root,0])