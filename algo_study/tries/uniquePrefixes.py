# input = ["zebra", "dog", "duck", "dogs", "dove"]
# output = ["z","dog", "du", "dogs", "dov"]

class Node:
    def __init__(self, char):
        self.char = char
        self.next = None
        self.end_of_word = False

class Trie:
    