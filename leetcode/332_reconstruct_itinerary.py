class Solution:
    def findItinerary(self, tickets: List[List[str]], iten = []) -> List[str]:
        itinerary = collections.defaultdict(list)
        
        for orig,dest in sorted(tickets)[::-1]:
            itinerary[orig].append(dest)
        
        route = []
        def travel(airport):
            while itinerary[airport]:
                travel(itinerary[airport].pop())
            route.append(airport)
        
        travel('JFK')
            
        return route[::-1]
        
        