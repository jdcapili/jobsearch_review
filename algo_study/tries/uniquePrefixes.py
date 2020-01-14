# input = ["zebra", "dog", "duck", "dogs", "dove"]
# output = ["z","dog", "du", "dogs", "dov"]

class Node:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, string):
        cur = self.root

        for idx,char in enumerate(string):
            if char in cur.children:
                cur = cur.children[char]
            else:
                node = Node(char)
                cur.children[char] = node
                cur = cur.children[char]

            if idx == len(string) -1: cur.end_of_word = True

    def printChildren(self,root,cur=""):
        if not root.children: 
            print(cur + root.char)
            return
        cur += root.char
        for child in root.children.values():
            self.printChildren(child,cur)
    
a = Trie()
a.insert("zebra")
a.insert("zygote")
a.insert("dog")
a.printChildren(a.root)
