class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {timestamp : value}
        else:
            self.store[key].update({timestamp : value})

    def get(self, key: str, timestamp: int) -> str:
        res = self.store.get(key,[])
        if timestamp in res:
            return res[timestamp]
        l=0
        r=len(res)-1
        t_list = list(res.keys())
        ret=""
        while l<=r:
            m = (l+r)//2
            if t_list[m] <=  timestamp:
                ret = res[t_list[m]]
                l = m+1
            else:
                r = m -1 
        return ret
        
##### I figured our this , but TLE
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([value,timestamp ])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        checker = self.store.get(key,[])
        l=0
        r=len(checker)-1
        while l<=r:
            m = (l+r)//2
            if checker[m][1] <=  timestamp:
                res = checker[m][0]
                l = m+1
            else:
                r = m -1 
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)