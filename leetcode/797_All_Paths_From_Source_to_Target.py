class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def travel(point, graph, path=[]):
            if len(graph[point]) is 0:
                res.append(path+[point])
                return
            for spot in graph[point]:
                travel(spot, graph, path+[point])
        
        travel(0, graph)
        return res
            