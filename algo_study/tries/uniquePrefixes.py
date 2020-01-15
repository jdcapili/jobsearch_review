# input = ["zebra", "dog", "duck", "dogs", "dove"]
# output = ["z","dog", "du", "dogs", "dov"]

class Node:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.count = 0
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
                
            cur.count += 1    

            if idx == len(string) -1: cur.end_of_word = True

    def printChildren(self,root,cur=""):
        if not root.children:
            root.count += 1 
            print(cur + root.char)
            return
        root.count += 1
        cur += root.char
        for child in root.children.values():
            print(child.char)

            self.printChildren(child,cur)

def uniquePrefixes(words):
    trie = Trie()

    for word in words:
        trie.insert(word)

    res = []

    def check_for_prefix(root,cur=""):

        if not root: return
        if root.count == 1:
            res.append(cur+root.char)
            return    
        elif root.end_of_word == True:
            res.append(cur+root.char)
        cur += root.char
        for child in root.children.values():
            check_for_prefix(child,cur)

    check_for_prefix(trie.root)
    return res




    
given = ["zebra", "dog", "duck", "dogs", "dove"]
print(uniquePrefixes(given))