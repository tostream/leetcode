class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            prevS,prevE = res[-1]
            curS,curE = intervals[i]
            if curS <= prevE:
                if prevE < curE:
                    res[-1][1] = curE
                if curS <prevS:
                    res[-1][0] = curS
            else:
                res.append([curS,curE])
        return res
