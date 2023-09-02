class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        res = []
        def distance(x,y):
            return [((x**2)+(y**2)),x,y]
        def result(res_arr):
            return [[y,z] for x,y,z in res_arr]
        for i in points:
            res.append(distance(i[0],i[1]))
        
        return result(heapq.nsmallest(k, res))
       