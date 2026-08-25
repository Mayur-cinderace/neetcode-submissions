class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
       self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            req = ""
            val = self.store[key]
            n = len(val)
            mid = n//2
            l = 0
            r = n-1
            while (l <= r):
                if val[mid][1] == timestamp:
                    return val[mid][0]
                if (val[mid][1] < timestamp):
                    req = val[mid][0]
                    l = mid+1
                else:
                    r = mid-1
                mid = (l+r)//2
        return req


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)