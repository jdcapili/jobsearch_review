# input = ["zebra", "dog", "duck", "dogs", "dove"]
#  output = ["z", "dog", "du", "dogs", "dov"]

class Node:
    def __init__(self):
        self.children = {}
        self.isTerminal = False