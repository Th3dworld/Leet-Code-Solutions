class TimeMap:

    def __init__(self):
        self.HashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.HashMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0,len(self.HashMap[key])-1
        res =""
        while l<=r:
            m = (l + r) //2 
            if self.HashMap[key][m][1] == timestamp:
                return self.HashMap[key][m][0]
            elif self.HashMap[key][m][1] > timestamp:
                r = m - 1
            else:
                res = self.HashMap[key][m][0]
                l = m + 1
                
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)