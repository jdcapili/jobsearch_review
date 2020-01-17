# input = ["zebra", "dog", "duck", "dogs", "dove"]
#  output = ["z", "dog", "du", "dogs", "dov"]

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
                cur.children[char] = node

            cur = cur.children[char]
            if idx == len(word)-1: cur.isTerminal = True
        

        return self.root
    
    def printTrie(self, root,cur = ""):
        print(cur)
        if len(root.children) == 0: 
            print(cur)
            return
        for child in root.children:
            nxtCur = cur + child
            nxtNode = root.children[child]
            self.printTrie(nxtNode,nxtCur)

test = Trie()
test.insert("zebra")
test.insert("zygote")
test.insert("dog")
test.insert("dove")
test.printTrie(test.root)