# Graphs
# collection of nodes and edges with unique paths between nodes
# can have no root


# Adjacency-list
# {
#     A:[B,C],
#     B:[D],
#     C:[D],
#     D:[]
# }

# rb hashes == js objects == py dictionaries

# adj_list = {
#     "a": ["b", "c"] ,
#     "b": ["d"],
#     "c": ["d"],
#     "d": []
# }



# def depth_first(neighbors, start, visited = None):
#     if visited == None:
#         visited = set()


#     if start in visited:
#         return
    
#     visited.add(start)

#     print(start)

    
#     for next_neighbor in neighbors[start]:
#         depth_first(neighbors, next_neighbor, visited)


# depth_first(adj_list, 'a')
# print('------')
# depth_first(adj_list, 'a')

# SCOPE
# 1. A function in python CAN access variables declared outside of it.
# 2. If a function declares a variable, it cannot be accessed outside of that function.
# 3. A block CAN access variables declared outside.
# 4. If a block declared a variable, it can be accessed outside of the block.

foo = 'potato'

def bar():
    print(foo)

bar()